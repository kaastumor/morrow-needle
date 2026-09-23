import json
from pathlib import Path


AUDIT=json.loads(
    Path("fixtures/audit/reg794-article3-system-continuity-2025-v0.1.json").read_text(
        encoding="utf-8"
    )
)
THREAD=json.loads(
    Path("fixtures/thread/reg794-article3-thread-v0.1.json").read_text(
        encoding="utf-8"
    )
)


def evidence():
    return {item["evidence_id"]:item for item in AUDIT["evidence"]}


def test_pre2025_legal_text_names_sani_and_pki_separately():
    old=evidence()["legal-pre2025"]
    assert old["notification_system"] == "State Aid Notification Interactive (SANI)"
    assert old["correspondence_system"] == "Public Key Infrastructure (PKI)"
    assert "LEGAL_TEXT_IDENTITY:SANI" in old["supports"]
    assert "LEGAL_TEXT_IDENTITY:PKI" in old["supports"]


def test_2025_legal_rewrite_deliberately_uses_generic_designations():
    new=evidence()["legal-2025-rewrite"]
    assert "practice has evolved" in new["recital_fact"]
    assert new["notification_system"] == "electronic application designated by the Commission"
    assert new["correspondence_system"] == "secured electronic system designated by the Commission"


def test_current_operational_docs_support_sani2_but_not_technical_continuity():
    current=evidence()["current-commission-notification-docs"]
    assert current["notification_system"] == "SANI / SANI2"
    assert "CURRENT_OPERATIONAL_IDENTIFICATION:NOTIFICATION:SANI2" in current["supports"]
    assert "TECHNICAL_CONTINUITY:SANI_2008_TO_SANI2" in current["does_not_support"]


def test_post2025_correspondence_identity_remains_unresolved():
    findings=AUDIT["findings"]
    assert findings["correspondence_current_operational_identification"] == "UNRESOLVED"
    assert findings["correspondence_technical_continuity"] == "UNRESOLVED"
    assert findings["notification_technical_continuity"] == "UNRESOLVED"


def test_existing_thread_unknown_remains_correct():
    unknown=next(
        item for item in THREAD["unknowns"]
        if item["unknown_id"] == "technical-channel-identity"
    )
    assert unknown["state"] == "UNRESOLVED"
    assert "does not assert" in unknown["description"]
    assert AUDIT["findings"]["thread_unknown_disposition"] == (
        "SURVIVES_WITH_FINER_EXPLANATION"
    )
    assert AUDIT["findings"]["current_claim_defect_observed"] is False


def test_electronic_rule_continuity_does_not_imply_technical_identity():
    forbidden=" ".join(AUDIT["forbidden_inferences"])
    assert "technically identical" in forbidden
    assert "solely because the previous legal text named PKI" in forbidden
    assert "Proposition-level continuity" in forbidden
