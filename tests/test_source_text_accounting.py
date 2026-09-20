import xml.etree.ElementTree as ET

from needle.ast.accounting import XMLTextLedger, aggregate_accounting_reports


def test_xml_text_ledger_distinguishes_mapped_metadata_and_unexplained():
    root = ET.fromstring(
        "<ACT>"
        "<BIB.DOC><NO.CELEX>32004R0794</NO.CELEX></BIB.DOC>"
        "<ARTICLE><PARAG>Member States shall notify.</PARAG></ARTICLE>"
        "<MYSTERY>Unclassified visible source text.</MYSTERY>"
        "</ACT>"
    )
    bib = root.find("BIB.DOC")
    paragraph = root.find("./ARTICLE/PARAG")
    assert bib is not None
    assert paragraph is not None

    ledger = XMLTextLedger(root, source_entry="fixture.xml")
    ledger.claim_subtree(
        bib,
        category="SOURCE_METADATA",
        reason="bibliographic source block",
    )
    ledger.claim_subtree(
        paragraph,
        category="LEGAL_MAPPED",
        reason="canonical paragraph",
    )
    ledger.classify_unclaimed(
        lambda atom: ("UNEXPLAINED", "no parser disposition")
    )
    report = ledger.report()

    by_category = {item["category"]: item for item in report["categories"]}
    assert by_category["LEGAL_MAPPED"]["chars"] > 0
    assert by_category["SOURCE_METADATA"]["chars"] > 0
    assert by_category["UNEXPLAINED"]["chars"] > 0
    assert report["unexplained_ratio"] > 0
    assert report["duplicate_claim_count"] == 0


def test_xml_text_ledger_records_duplicate_claims():
    root = ET.fromstring("<ACT><ARTICLE>Text</ARTICLE></ACT>")
    article = root.find("ARTICLE")
    assert article is not None

    ledger = XMLTextLedger(root, source_entry="fixture.xml")
    ledger.claim_subtree(article, category="LEGAL_MAPPED", reason="first")
    ledger.claim_subtree(article, category="LEGAL_MAPPED", reason="second")
    ledger.classify_unclaimed(
        lambda atom: ("UNEXPLAINED", "no parser disposition")
    )
    report = ledger.report()

    assert report["duplicate_claim_count"] == 1
    assert report["unexplained_chars"] == 0


def test_aggregate_accounting_preserves_totals():
    first_root = ET.fromstring("<A>One</A>")
    second_root = ET.fromstring("<B>Two</B>")
    first = XMLTextLedger(first_root, source_entry="a.xml")
    second = XMLTextLedger(second_root, source_entry="b.xml")
    first.claim_subtree(first_root, category="LEGAL_MAPPED", reason="mapped")
    second.classify_unclaimed(
        lambda atom: ("SOURCE_METADATA", "metadata")
    )

    report = aggregate_accounting_reports([first.report(), second.report()])
    assert report["entry_count"] == 2
    assert report["source_chars"] == len("One") + len("Two")
    assert report["accounted_chars"] == report["source_chars"]
    assert report["unexplained_chars"] == 0
