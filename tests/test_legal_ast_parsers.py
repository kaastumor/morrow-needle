import io
import json
import zipfile
from pathlib import Path

from jsonschema import Draft202012Validator

from needle.ast.formex import FormexASTParser
from needle.ast.historical_html import HistoricalHTMLASTParser


SCHEMA = json.loads(Path("schemas/legal-ast-v0.1.schema.json").read_text(encoding="utf-8"))


def _source(representation_class: str, adapter: str):
    return {
        "source_observation_ids": ["test:obs"],
        "celex": "TEST",
        "eli": None,
        "work_uri": None,
        "expression_uri": None,
        "manifestation_uri": None,
        "language": "ENG",
        "representation_class": representation_class,
        "adapter": adapter,
        "adapter_version": "0.1",
        "canonicalization_profile": "whitespace-collapse-v0.1",
    }


def _validate(ast):
    Draft202012Validator(SCHEMA).validate(ast)


def test_formex_article_and_mutation_annotation():
    xml = b'''<?xml version="1.0" encoding="UTF-8"?>
<ACT>
  <?CLG.MDFO ID="O1" IDREF="C1" ACTION="REPLACED" LEVEL="STRUCTURE"
      COMMAND="EXPLICIT" ACTIVE.DOC="32008R0271" ACTIVE.LOC="AR:1;PT:1" MOD.LEVEL="1"?>
  <ARTICLE IDENTIFIER="003">
    <TI.ART>Article 3</TI.ART>
    <PARAG ID="p1">Member States shall notify the Commission.</PARAG>
  </ARTICLE>
  <?CLG.MDFC ID="C1" IDREF="O1"?>
</ACT>'''
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        zf.writestr("main.xml", xml)

    parser = FormexASTParser(
        state_id="test-formex",
        source=_source("STRUCTURED_LEGAL_XML", "test-formex"),
        source_observation_id="test:obs",
    )
    ast = parser.parse_zip(buf.getvalue())
    _validate(ast)

    assert any(n["kind"] == "ARTICLE" and n["display_label"] == "Article 3" for n in ast["nodes"])
    assert any(n["kind"] == "PARAGRAPH" for n in ast["nodes"])
    assert any("Member States shall notify" in s["text_source"] for s in ast["segments"])
    annotations = [a for a in ast["annotations"] if a["kind"] == "CONSOLIDATION_MODIFICATION"]
    assert len(annotations) == 1
    assert annotations[0]["data"]["active_doc"] == "32008R0271"


def test_formex_raster_assets_force_known_gap():
    xml = b"<ACT><ARTICLE><TI.ART>Article 1</TI.ART><PARAG>Text.</PARAG></ARTICLE></ACT>"
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        zf.writestr("main.xml", xml)
        zf.writestr("annex.tif", b"TIFF")

    parser = FormexASTParser(
        state_id="test-raster",
        source=_source("STRUCTURED_LEGAL_XML", "test-formex"),
        source_observation_id="test:obs",
    )
    ast = parser.parse_zip(buf.getvalue())
    _validate(ast)
    assert any("raster assets" in gap for gap in ast["completeness"]["known_gaps"])


def test_historical_html_recovers_articles_and_blocks():
    body = b"""
<html><body>
<p>REGULATION No 1</p>
<p>Article 1</p>
<p>The languages of the institutions shall be Dutch, French, German and Italian.</p>
<p>Article 2</p>
<p>Documents which a Member State sends to the institutions may be drafted in any one of the official languages.</p>
</body></html>
"""
    parser = HistoricalHTMLASTParser(
        state_id="test-html",
        source=_source("STRUCTURED_HTML", "test-html"),
        source_observation_id="test:obs",
    )
    ast = parser.parse(body, native_path="test.html")
    _validate(ast)

    articles = [n for n in ast["nodes"] if n["kind"] == "ARTICLE"]
    assert [n["display_label"] for n in articles] == ["Article 1", "Article 2"]
    assert ast["parse_report"]["fidelity"] == "PARTIAL_STRUCTURAL"
    assert any("The languages of the institutions" in s["text_source"] for s in ast["segments"])


def test_formex_mixed_content_keeps_parent_flow_around_structures():
    xml = b'''<?xml version="1.0" encoding="UTF-8"?>
<ACT>
  <ARTICLE IDENTIFIER="001">
    <TI.ART>Article 1</TI.ART>
    <P>Before <NOTE>footnote text</NOTE> after note.</P>
    <CONTENTS>
      <NP>
        <NO.P>6.</NO.P>
        <TXT>Question before table</TXT>
        <TABLE>
          <ROW><CELL>Cell value</CELL></ROW>
        </TABLE>
        <P>Question after table</P>
      </NP>
    </CONTENTS>
  </ARTICLE>
</ACT>'''
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        zf.writestr("main.xml", xml)

    parser = FormexASTParser(
        state_id="test-mixed-flow",
        source=_source("STRUCTURED_LEGAL_XML", "test-formex"),
        source_observation_id="test:obs",
    )
    ast = parser.parse_zip(buf.getvalue())
    _validate(ast)

    text = " | ".join(segment["text_source"] for segment in ast["segments"])
    assert "Before" in text
    assert "after note." in text
    assert "6." in text
    assert "Question before table" in text
    assert "Question after table" in text
    assert "Cell value" in text

    assert any(node["kind"] == "FOOTNOTE" for node in ast["nodes"])
    assert any(node["kind"] == "TABLE" for node in ast["nodes"])
    assert any(node["kind"] == "TABLE_CELL" for node in ast["nodes"])

    accounting = ast["parse_report"]["source_text_accounting"]
    assert accounting["unexplained_chars"] == 0
    assert accounting["unexplained_shapes"] == []
    assert accounting["duplicate_claim_count"] == 0
    assert ast["parse_report"]["fidelity"] == "FULL_STRUCTURAL"


def test_formex_semantic_title_sequence_and_nested_list_labels():
    xml = b'''<?xml version="1.0" encoding="UTF-8"?>
<ACT>
  <FMX>ENREGTEST</FMX>
  <ENACTING.TERMS>
    <TITLE>
      <TI>CHAPTER I</TI>
      <STI>Subject matter</STI>
    </TITLE>
    <ARTICLE IDENTIFIER="001">
      <TI.ART>Article 1</TI.ART>
      <GR.SEQ>
        <NO.GR.SEQ>1.</NO.GR.SEQ>
        <P>Grouped question text.</P>
      </GR.SEQ>
      <LIST TYPE="alpha">
        <ITEM>
          <NP>
            <NO.P>(a)</NO.P>
            <TXT>first item;</TXT>
          </NP>
        </ITEM>
      </LIST>
    </ARTICLE>
  </ENACTING.TERMS>
</ACT>'''
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        zf.writestr("main.xml", xml)

    parser = FormexASTParser(
        state_id="test-semantic-structure",
        source=_source("STRUCTURED_LEGAL_XML", "test-formex"),
        source_observation_id="test:obs",
    )
    ast = parser.parse_zip(buf.getvalue())
    _validate(ast)

    chapters = [n for n in ast["nodes"] if n["kind"] == "CHAPTER"]
    assert len(chapters) == 1
    assert chapters[0]["display_label"] == "CHAPTER I"
    chapter_segments = [
        s for s in ast["segments"] if s["node_id"] == chapters[0]["node_id"]
    ]
    assert any(s["role"] == "HEADING" and s["text_source"] == "Subject matter" for s in chapter_segments)

    blocks = [n for n in ast["nodes"] if n["kind"] == "BLOCK" and n["native_kind"] == "GR.SEQ"]
    assert len(blocks) == 1
    assert blocks[0]["display_label"] == "1."

    items = [n for n in ast["nodes"] if n["kind"] == "LIST_ITEM"]
    assert len(items) == 1
    assert items[0]["display_label"] == "(a)"
    item_text = " ".join(
        s["text_source"] for s in ast["segments"] if s["node_id"] == items[0]["node_id"]
    )
    assert "first item;" in item_text

    accounting = ast["parse_report"]["source_text_accounting"]
    assert accounting["unexplained_chars"] == 0
    assert accounting["duplicate_claim_count"] == 0
    assert "FMX" not in ast["parse_report"]["unknown_native_kinds"]
    assert "TI" not in ast["parse_report"]["unknown_native_kinds"]
    assert "STI" not in ast["parse_report"]["unknown_native_kinds"]


def test_formex_document_family_wrappers_are_metadata_not_legal_body():
    xml = b'''<?xml version="1.0" encoding="UTF-8"?>
<DOC>
  <FMX>ENREGTEST</FMX>
  <FAM.COMP>32004R0794 32008R0271 32025R0905</FAM.COMP>
  <ACT>
    <ARTICLE IDENTIFIER="001">
      <TI.ART>Article 1</TI.ART>
      <PARAG>Operative text survives.</PARAG>
    </ARTICLE>
  </ACT>
</DOC>'''
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        zf.writestr("main.xml", xml)

    parser = FormexASTParser(
        state_id="test-source-metadata",
        source=_source("STRUCTURED_LEGAL_XML", "test-formex"),
        source_observation_id="test:obs",
    )
    ast = parser.parse_zip(buf.getvalue())
    _validate(ast)

    legal_text = " ".join(segment["text_source"] for segment in ast["segments"])
    assert "Operative text survives." in legal_text
    assert "ENREGTEST" not in legal_text
    assert "32008R0271" not in legal_text

    accounting = ast["parse_report"]["source_text_accounting"]
    metadata = next(
        category for category in accounting["categories"]
        if category["category"] == "SOURCE_METADATA"
    )
    assert metadata["chars"] > 0
    assert accounting["unexplained_chars"] == 0
    assert accounting["duplicate_claim_count"] == 0
    assert "DOC" not in ast["parse_report"]["unknown_native_kinds"]
    assert "FAM.COMP" not in ast["parse_report"]["unknown_native_kinds"]
