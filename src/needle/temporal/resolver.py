from __future__ import annotations

from calendar import monthrange
from datetime import date, timedelta
from typing import Any


def _date(value: str) -> date:
    return date.fromisoformat(value)


def _add_months(value: date, months: int) -> date:
    month_index = value.month - 1 + months
    year = value.year + month_index // 12
    month = month_index % 12 + 1
    day = min(value.day, monthrange(year, month)[1])
    return date(year, month, day)


def _apply_offset(value: date, offset: dict[str, Any]) -> date:
    amount = int(offset["value"])
    unit = offset["unit"]
    if unit == "DAYS":
        return value + timedelta(days=amount)
    if unit == "MONTHS":
        return _add_months(value, amount)
    if unit == "YEARS":
        try:
            return value.replace(year=value.year + amount)
        except ValueError:
            return value.replace(month=2, day=28, year=value.year + amount)
    raise ValueError(f"unsupported temporal offset unit: {unit}")


def _guard_allows(value: date, guard: dict[str, Any] | None) -> bool:
    if not guard:
        return True
    other = _date(guard["date"])
    op = guard["operator"]
    if op == "BEFORE":
        return value < other
    if op == "ON_OR_BEFORE":
        return value <= other
    if op == "AFTER":
        return value > other
    if op == "ON_OR_AFTER":
        return value >= other
    raise ValueError(f"unsupported temporal guard: {op}")


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
    raise ValueError(f"unsupported entity condition: {condition['operator']}")


def _trigger_date(assertion: dict[str, Any], context: dict[str, Any]) -> tuple[date | None, str | None]:
    if assertion.get("normalized_date"):
        return _date(assertion["normalized_date"]), None

    trigger = assertion["trigger"]
    if trigger["kind"] == "ABSOLUTE_DATE":
        return _date(trigger["date"]), None

    event_key = trigger["event_key"]
    events = context.get("events", {})
    raw = events.get(event_key)
    if raw is None:
        return None, event_key
    value = _apply_offset(_date(raw), trigger["offset"])
    if not _guard_allows(value, trigger.get("guard")):
        return None, None
    return value, None


def resolve_boundary(
    assertions: list[dict[str, Any]],
    *,
    dimension: str,
    boundary: str,
    subject_keys: set[str],
    context: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one temporal boundary without inventing missing context.

    Overrides are explicit evidence relationships: the resolver never infers
    specificity merely from labels such as "Article 24(2)".
    """
    context = context or {}
    applicable: dict[str, tuple[dict[str, Any], date]] = {}
    pending: list[dict[str, str]] = []

    for assertion in assertions:
        if assertion["dimension"] != dimension or assertion["boundary"] != boundary:
            continue
        if not subject_keys.intersection(assertion["scope"]["applies_to"]):
            continue

        condition = _entity_condition(assertion, context)
        if condition is False:
            continue
        if condition is None:
            pending.append({"assertion_id": assertion["assertion_id"], "missing":"entity_condition"})
            continue

        value, missing_event = _trigger_date(assertion, context)
        if missing_event:
            pending.append({"assertion_id": assertion["assertion_id"], "missing":missing_event})
            continue
        if value is None:
            # A conditional trigger whose guard is false simply does not
            # override its fallback/default.
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

    # A missing conditional override matters: a default date can be shown as
    # fallback, but Needle must not pretend it is the resolved entity date.
    pending_override = [
        item for item in pending
        if next(
            a for a in assertions if a["assertion_id"] == item["assertion_id"]
        )["scope"]["mode"] == "CONDITIONAL_OVERRIDE"
    ]
    if pending_override:
        defaults = [
            {"assertion_id":a["assertion_id"], "date":v.isoformat()}
            for a, v in survivors
            if a["scope"]["mode"] == "DEFAULT"
        ]
        return {
            "state":"CONTEXT_REQUIRED",
            "date":None,
            "fallbacks":defaults,
            "missing":pending_override,
        }

    dates = {value for _, value in survivors}
    if not survivors:
        return {"state":"NOT_ASSERTED","date":None,"assertion_ids":[]}
    if len(dates) > 1:
        return {
            "state":"CONFLICTING",
            "date":None,
            "assertion_ids":[a["assertion_id"] for a, _ in survivors],
            "dates":sorted(v.isoformat() for v in dates),
        }

    value = next(iter(dates))
    return {
        "state":"RESOLVED",
        "date":value.isoformat(),
        "assertion_ids":[a["assertion_id"] for a, _ in survivors],
    }


def status_on(
    assertions: list[dict[str, Any]],
    *,
    dimension: str,
    subject_keys: set[str],
    on_date: str,
    context: dict[str, Any] | None = None,
) -> dict[str, Any]:
    start = resolve_boundary(
        assertions,
        dimension=dimension,
        boundary="START",
        subject_keys=subject_keys,
        context=context,
    )
    end = resolve_boundary(
        assertions,
        dimension=dimension,
        boundary="END",
        subject_keys=subject_keys,
        context=context,
    )

    if start["state"] == "CONTEXT_REQUIRED" or end["state"] == "CONTEXT_REQUIRED":
        return {"state":"CONTEXT_REQUIRED","active":None,"start":start,"end":end}
    if start["state"] in {"CONFLICTING"} or end["state"] in {"CONFLICTING"}:
        return {"state":"CONFLICTING","active":None,"start":start,"end":end}
    if start["state"] == "NOT_ASSERTED":
        return {"state":"NOT_ASSERTED","active":None,"start":start,"end":end}

    query = _date(on_date)
    active = query >= _date(start["date"])
    if end["state"] == "RESOLVED":
        active = active and query <= _date(end["date"])

    return {"state":"RESOLVED","active":active,"start":start,"end":end}


def gap_between(
    previous_end: str,
    next_start: str,
    *,
    previous_end_inclusive: bool = True,
    next_start_inclusive: bool = True,
) -> dict[str, Any]:
    """Return the uncovered calendar-date interval between two regimes."""
    end = _date(previous_end)
    start = _date(next_start)
    gap_start = end + (timedelta(days=1) if previous_end_inclusive else timedelta())
    gap_end = start - (timedelta(days=1) if next_start_inclusive else timedelta())
    if gap_start > gap_end:
        return {"state":"NO_GAP","start":None,"end":None}
    return {"state":"GAP","start":gap_start.isoformat(),"end":gap_end.isoformat()}
