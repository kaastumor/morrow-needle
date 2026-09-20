from needle.ast.completeness import audit_text_witness


def _ast(text):
    return {"segments": [{"text_compare": text}]}


def test_text_witness_detects_additional_block():
    primary = _ast(
        "Article 1 Member States shall notify the Commission by electronic means "
        "before granting the aid and shall identify confidential material."
    )
    witness = b"""
<html><body>
<p>Article 1 Member States shall notify the Commission by electronic means before granting the aid and shall identify confidential material.</p>
<p>Annex I Additional reporting fields include the undertaking identifier, amount, region, sector, date, legal basis, aid instrument, objective, eligible costs, intensity and supporting documentation.</p>
</body></html>
"""
    result = audit_text_witness(primary, witness, shingle_size=5, min_block_tokens=8)
    assert result["coverage"]["primary_shingles_found_in_witness"] == 1.0
    assert result["coverage"]["witness_shingles_found_in_primary"] < 1.0
    assert result["witness_excess_block_count"] >= 1


def test_text_witness_equal_text_has_symmetric_coverage():
    text = "Article 1 This regulation shall enter into force on the twentieth day following publication."
    result = audit_text_witness(
        _ast(text),
        f"<html><body><p>{text}</p></body></html>".encode(),
        shingle_size=4,
        min_block_tokens=4,
    )
    assert result["coverage"]["primary_shingles_found_in_witness"] == 1.0
    assert result["coverage"]["witness_shingles_found_in_primary"] == 1.0
