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

    boundaries = {
        (value, bool(assertion.get("inclusive", True)))
        for assertion, value in survivors
    }
    if not survivors:
        return {"state":"NOT_ASSERTED","date":None,"assertion_ids":[]}
    if len(boundaries) > 1:
        return {
            "state":"CONFLICTING",
            "date":None,
            "assertion_ids":[a["assertion_id"] for a, _ in survivors],
            "dates":sorted({v.isoformat() for v, _ in boundaries}),
            "inclusive_values":sorted({inclusive for _, inclusive in boundaries}),
        }

    value, inclusive = next(iter(boundaries))
    return {
        "state":"RESOLVED",
        "date":value.isoformat(),
        "inclusive":inclusive,
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
    start_date = _date(start["date"])
    active = (
        query >= start_date
        if start.get("inclusive", True)
        else query > start_date
    )
    if end["state"] == "RESOLVED":
        end_date = _date(end["date"])
        active = active and (
            query <= end_date
            if end.get("inclusive", True)
            else query < end_date
        )

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



def _publication_availability_index(
    assertions: list[dict[str, Any]],
    context: dict[str, Any] | None = None,
) -> dict[str, date]:
    """Earliest official-source availability known to this fixture/query.

    Historical-source perspective is based on official publication/availability,
    not on when Needle happened to ingest the source and not on assumptions
    about what a particular person knew.
    """
    context = context or {}
    index: dict[str, date] = {
        key: _date(value)
        for key, value in context.get("source_available_from", {}).items()
    }

    for assertion in assertions:
        if assertion["dimension"] != "PUBLICATION" or assertion["boundary"] != "POINT":
            continue
        value, missing = _trigger_date(assertion, context)
        if value is None or missing:
            continue
        identifier = assertion["subject_ref"]["identifier"]
        previous = index.get(identifier)
        if previous is None or value < previous:
            index[identifier] = value
    return index


def _is_relevant(
    assertion: dict[str, Any],
    *,
    dimension: str,
    subject_keys: set[str],
) -> bool:
    return (
        assertion["dimension"] == dimension
        and bool(subject_keys.intersection(assertion["scope"]["applies_to"]))
    )


def _filter_assertions_by_official_source_cutoff(
    assertions: list[dict[str, Any]],
    *,
    cutoff_date: str,
    dimension: str,
    subject_keys: set[str],
    context: dict[str, Any] | None = None,
) -> dict[str, Any]:
    context = context or {}
    cutoff = _date(cutoff_date)
    availability = _publication_availability_index(assertions, context)

    included: list[dict[str, Any]] = []
    later: list[dict[str, Any]] = []
    unresolved: list[dict[str, Any]] = []

    for assertion in assertions:
        source_dates: list[date] = []
        missing_sources: list[str] = []

        # Publication assertions are self-dating official-source facts.
        if assertion["dimension"] == "PUBLICATION":
            value, missing = _trigger_date(assertion, context)
            if value is not None and not missing:
                source_dates.append(value)
        else:
            for source_ref in assertion.get("source_refs", []):
                identifier = source_ref["identifier"]
                value = availability.get(identifier)
                if value is None:
                    missing_sources.append(identifier)
                else:
                    source_dates.append(value)

        if missing_sources:
            if _is_relevant(assertion, dimension=dimension, subject_keys=subject_keys):
                unresolved.append({
                    "assertion_id": assertion["assertion_id"],
                    "missing_source_availability": sorted(set(missing_sources)),
                })
            continue

        available_from = max(source_dates) if source_dates else None
        if available_from is None:
            if _is_relevant(assertion, dimension=dimension, subject_keys=subject_keys):
                unresolved.append({
                    "assertion_id": assertion["assertion_id"],
                    "missing_source_availability": ["<no dated official source>"],
                })
            continue

        if available_from <= cutoff:
            included.append(assertion)
        elif _is_relevant(assertion, dimension=dimension, subject_keys=subject_keys):
            later.append({
                "assertion_id": assertion["assertion_id"],
                "official_source_available_from": available_from.isoformat(),
            })

    return {
        "assertions": included,
        "later_relevant": later,
        "unresolved_relevant": unresolved,
        "cutoff_date": cutoff.isoformat(),
    }


def status_on_perspective(
    assertions: list[dict[str, Any]],
    *,
    dimension: str,
    subject_keys: set[str],
    valid_date: str,
    perspective: str = "EX_POST_LEGAL_EFFECT",
    source_cutoff_date: str | None = None,
    context: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve legal time under an explicit historical-source perspective.

    EX_POST_LEGAL_EFFECT:
        Use the full evidence set, including later acts with retroactive effect.

    OFFICIAL_SOURCE_STATE_AS_OF:
        Only use assertions supported by official sources available by the
        source cutoff date. This reconstructs the official-source state as of
        that date; it does not claim what any particular person actually knew.
    """
    context = context or {}

    if perspective == "EX_POST_LEGAL_EFFECT":
        result = status_on(
            assertions,
            dimension=dimension,
            subject_keys=subject_keys,
            on_date=valid_date,
            context=context,
        )
        return {
            **result,
            "perspective":"EX_POST_LEGAL_EFFECT",
            "valid_date":valid_date,
            "source_cutoff_date":None,
        }

    if perspective != "OFFICIAL_SOURCE_STATE_AS_OF":
        raise ValueError(f"unsupported temporal perspective: {perspective}")
    if not source_cutoff_date:
        return {
            "state":"SOURCE_CUTOFF_REQUIRED",
            "active":None,
            "perspective":perspective,
            "valid_date":valid_date,
            "source_cutoff_date":None,
        }

    filtered = _filter_assertions_by_official_source_cutoff(
        assertions,
        cutoff_date=source_cutoff_date,
        dimension=dimension,
        subject_keys=subject_keys,
        context=context,
    )
    if filtered["unresolved_relevant"]:
        return {
            "state":"SOURCE_AVAILABILITY_UNRESOLVED",
            "active":None,
            "perspective":perspective,
            "valid_date":valid_date,
            "source_cutoff_date":source_cutoff_date,
            "unresolved":filtered["unresolved_relevant"],
            "later_assertions":filtered["later_relevant"],
        }

    result = status_on(
        filtered["assertions"],
        dimension=dimension,
        subject_keys=subject_keys,
        on_date=valid_date,
        context=context,
    )
    if result["state"] == "NOT_ASSERTED" and filtered["later_relevant"]:
        return {
            "state":"NOT_ASSERTED_AS_OF_SOURCE_DATE",
            "active":None,
            "perspective":perspective,
            "valid_date":valid_date,
            "source_cutoff_date":source_cutoff_date,
            "later_assertions":filtered["later_relevant"],
        }

    return {
        **result,
        "perspective":perspective,
        "valid_date":valid_date,
        "source_cutoff_date":source_cutoff_date,
        "later_assertions":filtered["later_relevant"],
    }
