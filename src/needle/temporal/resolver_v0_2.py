from __future__ import annotations

from calendar import monthrange
from copy import deepcopy
from datetime import date, datetime, timedelta, timezone
from typing import Any

from needle.temporal.resolver import (
    status_on as status_on_v0_1,
    status_on_perspective as status_on_perspective_v0_1,
)


class TemporalPrecisionError(ValueError):
    pass


def _parse_instant(value: str) -> datetime:
    candidate = value[:-1] + "+00:00" if value.endswith("Z") else value
    parsed = datetime.fromisoformat(candidate)
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise TemporalPrecisionError(
            "INSTANT values must include an explicit UTC offset"
        )
    return parsed.astimezone(timezone.utc)


def _add_months(value: datetime, months: int) -> datetime:
    month_index = value.month - 1 + months
    year = value.year + month_index // 12
    month = month_index % 12 + 1
    day = min(value.day, monthrange(year, month)[1])
    return value.replace(year=year, month=month, day=day)


def _apply_instant_offset(value: datetime, offset: dict[str, Any]) -> datetime:
    amount = int(offset["value"])
    unit = offset["unit"]
    if unit == "MINUTES":
        return value + timedelta(minutes=amount)
    if unit == "HOURS":
        return value + timedelta(hours=amount)
    if unit == "DAYS":
        return value + timedelta(days=amount)
    if unit == "MONTHS":
        return _add_months(value, amount)
    if unit == "YEARS":
        try:
            return value.replace(year=value.year + amount)
        except ValueError:
            return value.replace(month=2, day=28, year=value.year + amount)
    raise TemporalPrecisionError(f"unsupported instant offset unit: {unit}")


def _entity_condition(assertion: dict[str, Any], context: dict[str, Any]) -> bool | None:
    condition = assertion["scope"].get("entity_condition")
    if not condition:
        return True
    entity = context.get("entity", {})
    attribute = condition["attribute"]
    if attribute not in entity:
        return None
    if condition["operator"] == "IN":
        return str(entity[attribute]) in set(condition["values"])
    raise TemporalPrecisionError(
        f"unsupported entity condition: {condition['operator']}"
    )


def _guard_allows_instant(
    value: datetime,
    guard: dict[str, Any] | None,
) -> bool:
    if not guard:
        return True
    if guard["precision"] != "INSTANT":
        raise TemporalPrecisionError(
            "INSTANT assertion cannot use a DATE guard without conversion evidence"
        )
    other = _parse_instant(guard["instant"])
    op = guard["operator"]
    if op == "BEFORE":
        return value < other
    if op == "ON_OR_BEFORE":
        return value <= other
    if op == "AFTER":
        return value > other
    if op == "ON_OR_AFTER":
        return value >= other
    raise TemporalPrecisionError(f"unsupported temporal guard: {op}")


def _trigger_instant(
    assertion: dict[str, Any],
    context: dict[str, Any],
) -> tuple[datetime | None, str | None]:
    if assertion.get("normalized_instant"):
        return _parse_instant(assertion["normalized_instant"]), None

    trigger = assertion["trigger"]
    if trigger["kind"] == "ABSOLUTE_INSTANT":
        return _parse_instant(trigger["instant"]), None
    if trigger["kind"] != "RELATIVE_EVENT":
        raise TemporalPrecisionError(
            "INSTANT assertion requires ABSOLUTE_INSTANT or RELATIVE_EVENT"
        )

    event_key = trigger["event_key"]
    raw = context.get("events", {}).get(event_key)
    if raw is None:
        return None, event_key
    value = _apply_instant_offset(_parse_instant(raw), trigger["offset"])
    if not _guard_allows_instant(value, trigger.get("guard")):
        return None, None
    return value, None


def _relevant(
    assertion: dict[str, Any],
    *,
    dimension: str,
    subject_keys: set[str],
) -> bool:
    return (
        assertion["dimension"] == dimension
        and bool(subject_keys.intersection(assertion["scope"]["applies_to"]))
    )


def upgrade_v0_1_assertion(assertion: dict[str, Any]) -> dict[str, Any]:
    upgraded = deepcopy(assertion)
    upgraded["precision"] = "DATE"
    upgraded.setdefault("normalized_instant", None)
    return upgraded


def _downgrade_date_assertion(assertion: dict[str, Any]) -> dict[str, Any]:
    if assertion.get("precision") != "DATE":
        raise TemporalPrecisionError("cannot downgrade non-DATE assertion")
    downgraded = deepcopy(assertion)
    downgraded.pop("precision", None)
    downgraded.pop("normalized_instant", None)
    guard = downgraded.get("trigger", {}).get("guard")
    if isinstance(guard, dict) and "precision" in guard:
        if guard["precision"] != "DATE":
            raise TemporalPrecisionError(
                "DATE assertion cannot use an INSTANT guard"
            )
        guard.pop("precision", None)
    return downgraded


def resolve_boundary_at(
    assertions: list[dict[str, Any]],
    *,
    dimension: str,
    boundary: str,
    subject_keys: set[str],
    precision: str,
    context: dict[str, Any] | None = None,
) -> dict[str, Any]:
    context = context or {}
    relevant = [
        item
        for item in assertions
        if _relevant(item, dimension=dimension, subject_keys=subject_keys)
        and item["boundary"] == boundary
    ]

    mismatched = [
        item["assertion_id"]
        for item in relevant
        if item.get("precision") != precision
    ]
    if mismatched:
        return {
            "state": "MIXED_PRECISION_UNRESOLVED",
            "precision": precision,
            "value": None,
            "assertion_ids": mismatched,
        }

    if precision == "DATE":
        downgraded = [_downgrade_date_assertion(item) for item in assertions]
        result = __import__(
            "needle.temporal.resolver",
            fromlist=["resolve_boundary"],
        ).resolve_boundary(
            downgraded,
            dimension=dimension,
            boundary=boundary,
            subject_keys=subject_keys,
            context=context,
        )
        if "date" in result:
            result = {**result, "value": result.get("date")}
        return {**result, "precision": "DATE"}

    if precision != "INSTANT":
        raise TemporalPrecisionError(f"unsupported precision: {precision}")

    applicable: dict[str, tuple[dict[str, Any], datetime]] = {}
    pending: list[dict[str, str]] = []

    for assertion in relevant:
        condition = _entity_condition(assertion, context)
        if condition is False:
            continue
        if condition is None:
            pending.append({
                "assertion_id": assertion["assertion_id"],
                "missing": "entity_condition",
            })
            continue

        value, missing_event = _trigger_instant(assertion, context)
        if missing_event:
            pending.append({
                "assertion_id": assertion["assertion_id"],
                "missing": missing_event,
            })
            continue
        if value is None:
            continue
        applicable[assertion["assertion_id"]] = (assertion, value)

    overridden: set[str] = set()
    for assertion, _ in applicable.values():
        if assertion["scope"]["mode"] in {"OVERRIDE", "CONDITIONAL_OVERRIDE"}:
            overridden.update(assertion["scope"]["overrides_assertion_ids"])

    survivors = [
        (assertion, value)
        for assertion_id, (assertion, value) in applicable.items()
        if assertion_id not in overridden
    ]

    pending_override = [
        item
        for item in pending
        if next(
            a for a in assertions
            if a["assertion_id"] == item["assertion_id"]
        )["scope"]["mode"] == "CONDITIONAL_OVERRIDE"
    ]
    if pending_override:
        return {
            "state": "CONTEXT_REQUIRED",
            "precision": "INSTANT",
            "value": None,
            "fallbacks": [
                {
                    "assertion_id": assertion["assertion_id"],
                    "instant": value.isoformat(),
                }
                for assertion, value in survivors
                if assertion["scope"]["mode"] == "DEFAULT"
            ],
            "missing": pending_override,
        }

    boundaries = {
        (value, bool(assertion.get("inclusive", True)))
        for assertion, value in survivors
    }
    if not survivors:
        return {
            "state": "NOT_ASSERTED",
            "precision": "INSTANT",
            "value": None,
            "assertion_ids": [],
        }
    if len(boundaries) > 1:
        return {
            "state": "CONFLICTING",
            "precision": "INSTANT",
            "value": None,
            "assertion_ids": [a["assertion_id"] for a, _ in survivors],
            "instants": sorted({v.isoformat() for v, _ in boundaries}),
            "inclusive_values": sorted({inc for _, inc in boundaries}),
        }

    value, inclusive = next(iter(boundaries))
    return {
        "state": "RESOLVED",
        "precision": "INSTANT",
        "value": value.isoformat(),
        "instant": value.isoformat(),
        "inclusive": inclusive,
        "assertion_ids": [a["assertion_id"] for a, _ in survivors],
    }


def status_at(
    assertions: list[dict[str, Any]],
    *,
    dimension: str,
    subject_keys: set[str],
    precision: str,
    at_value: str,
    context: dict[str, Any] | None = None,
) -> dict[str, Any]:
    context = context or {}
    if precision == "DATE":
        relevant = [
            item
            for item in assertions
            if _relevant(item, dimension=dimension, subject_keys=subject_keys)
        ]
        if any(item.get("precision") != "DATE" for item in relevant):
            return {
                "state": "MIXED_PRECISION_UNRESOLVED",
                "active": None,
                "precision": "DATE",
            }
        result = status_on_v0_1(
            [_downgrade_date_assertion(item) for item in assertions],
            dimension=dimension,
            subject_keys=subject_keys,
            on_date=at_value,
            context=context,
        )
        return {**result, "precision": "DATE", "valid_value": at_value}

    if precision != "INSTANT":
        raise TemporalPrecisionError(f"unsupported precision: {precision}")

    query = _parse_instant(at_value)
    start = resolve_boundary_at(
        assertions,
        dimension=dimension,
        boundary="START",
        subject_keys=subject_keys,
        precision="INSTANT",
        context=context,
    )
    end = resolve_boundary_at(
        assertions,
        dimension=dimension,
        boundary="END",
        subject_keys=subject_keys,
        precision="INSTANT",
        context=context,
    )

    if (
        start["state"] == "MIXED_PRECISION_UNRESOLVED"
        or end["state"] == "MIXED_PRECISION_UNRESOLVED"
    ):
        return {
            "state": "MIXED_PRECISION_UNRESOLVED",
            "active": None,
            "precision": "INSTANT",
            "start": start,
            "end": end,
        }
    if start["state"] == "CONTEXT_REQUIRED" or end["state"] == "CONTEXT_REQUIRED":
        return {
            "state": "CONTEXT_REQUIRED",
            "active": None,
            "precision": "INSTANT",
            "start": start,
            "end": end,
        }
    if start["state"] == "CONFLICTING" or end["state"] == "CONFLICTING":
        return {
            "state": "CONFLICTING",
            "active": None,
            "precision": "INSTANT",
            "start": start,
            "end": end,
        }
    if start["state"] == "NOT_ASSERTED":
        return {
            "state": "NOT_ASSERTED",
            "active": None,
            "precision": "INSTANT",
            "start": start,
            "end": end,
        }

    start_value = _parse_instant(start["instant"])
    active = (
        query >= start_value
        if start.get("inclusive", True)
        else query > start_value
    )
    if end["state"] == "RESOLVED":
        end_value = _parse_instant(end["instant"])
        active = active and (
            query <= end_value
            if end.get("inclusive", True)
            else query < end_value
        )

    return {
        "state": "RESOLVED",
        "active": active,
        "precision": "INSTANT",
        "valid_value": query.isoformat(),
        "start": start,
        "end": end,
    }


def status_at_perspective(
    assertions: list[dict[str, Any]],
    *,
    dimension: str,
    subject_keys: set[str],
    valid_time: dict[str, str],
    perspective: str = "EX_POST_LEGAL_EFFECT",
    source_cutoff_time: dict[str, str] | None = None,
    context: dict[str, Any] | None = None,
) -> dict[str, Any]:
    context = context or {}
    precision = valid_time["precision"]
    value = valid_time["date"] if precision == "DATE" else valid_time["instant"]

    if precision == "DATE":
        cutoff = None
        if source_cutoff_time is not None:
            if source_cutoff_time["precision"] != "DATE":
                return {
                    "state": "SOURCE_PRECISION_UNRESOLVED",
                    "active": None,
                    "precision": "DATE",
                }
            cutoff = source_cutoff_time["date"]
        result = status_on_perspective_v0_1(
            [_downgrade_date_assertion(item) for item in assertions],
            dimension=dimension,
            subject_keys=subject_keys,
            valid_date=value,
            perspective=perspective,
            source_cutoff_date=cutoff,
            context=context,
        )
        return {**result, "precision": "DATE"}

    if perspective == "EX_POST_LEGAL_EFFECT":
        result = status_at(
            assertions,
            dimension=dimension,
            subject_keys=subject_keys,
            precision="INSTANT",
            at_value=value,
            context=context,
        )
        return {**result, "perspective": perspective}

    if perspective != "OFFICIAL_SOURCE_STATE_AS_OF":
        raise TemporalPrecisionError(f"unsupported temporal perspective: {perspective}")
    if source_cutoff_time is None:
        return {
            "state": "SOURCE_CUTOFF_REQUIRED",
            "active": None,
            "precision": "INSTANT",
            "perspective": perspective,
        }
    if source_cutoff_time["precision"] != "INSTANT":
        return {
            "state": "SOURCE_PRECISION_UNRESOLVED",
            "active": None,
            "precision": "INSTANT",
            "perspective": perspective,
        }

    availability = context.get("source_available_from", {})
    cutoff = _parse_instant(source_cutoff_time["instant"])
    filtered = []
    unresolved = []
    later = []
    for assertion in assertions:
        if not _relevant(
            assertion,
            dimension=dimension,
            subject_keys=subject_keys,
        ):
            filtered.append(assertion)
            continue
        source_times = []
        missing = []
        for source_ref in assertion.get("source_refs", []):
            raw = availability.get(source_ref["identifier"])
            if raw is None:
                missing.append(source_ref["identifier"])
                continue
            try:
                source_times.append(_parse_instant(raw))
            except (ValueError, TemporalPrecisionError):
                return {
                    "state": "SOURCE_PRECISION_UNRESOLVED",
                    "active": None,
                    "precision": "INSTANT",
                    "perspective": perspective,
                }
        if missing:
            unresolved.append({
                "assertion_id": assertion["assertion_id"],
                "missing_source_availability": sorted(set(missing)),
            })
            continue
        available_from = max(source_times) if source_times else None
        if available_from is None:
            unresolved.append({
                "assertion_id": assertion["assertion_id"],
                "missing_source_availability": ["<no dated official source>"],
            })
        elif available_from <= cutoff:
            filtered.append(assertion)
        else:
            later.append({
                "assertion_id": assertion["assertion_id"],
                "official_source_available_from": available_from.isoformat(),
            })

    if unresolved:
        return {
            "state": "SOURCE_AVAILABILITY_UNRESOLVED",
            "active": None,
            "precision": "INSTANT",
            "perspective": perspective,
            "unresolved": unresolved,
            "later_assertions": later,
        }

    result = status_at(
        filtered,
        dimension=dimension,
        subject_keys=subject_keys,
        precision="INSTANT",
        at_value=value,
        context=context,
    )
    if result["state"] == "NOT_ASSERTED" and later:
        return {
            "state": "NOT_ASSERTED_AS_OF_SOURCE_DATE",
            "active": None,
            "precision": "INSTANT",
            "perspective": perspective,
            "later_assertions": later,
        }
    return {
        **result,
        "perspective": perspective,
        "later_assertions": later,
    }
