import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from needle.identity.resolver import IdentityGraphError, TypedIdentifierGraph


SCHEMA = json.loads(
    Path("schemas/identifier-graph-v0.1.schema.json").read_text(encoding="utf-8")
)
FIXTURE = json.loads(
    Path("fixtures/identity/eu-identifier-adversaries-v0.1.json").read_text(encoding="utf-8")
)


def _graph():
    return TypedIdentifierGraph(FIXTURE)


def test_identifier_graph_fixture_validates():
    errors = [error.message for error in Draft202012Validator(SCHEMA).iter_errors(FIXTURE)]
    assert errors == []
    _graph()


def test_base_act_celex_eli_and_cellar_work_are_same_legal_resource():
    graph = _graph()
    ids = {node["node_id"] for node in graph.equivalents("r794-celex")}
    assert ids == {"r794-celex","r794-eli","r794-cellar-work"}


def test_expression_and_manifestation_are_not_same_identity_as_work():
    graph = _graph()
    assert not graph.same_identity("r794-celex","r794-eng-expression")
    assert not graph.same_identity("r794-celex","r794-eng-fmx4")
    assert graph.related("r794-eng-expression","EXPRESSION_OF")[0]["node_id"] == "r794-cellar-work"
    assert graph.related("r794-eng-fmx4","MANIFESTATION_OF")[0]["node_id"] == "r794-eng-expression"


def test_consolidated_state_is_related_to_but_not_equivalent_to_base_act():
    graph = _graph()
    assert graph.same_identity("r794-consolidated-celex","r794-consolidated-eli")
    assert not graph.same_identity("r794-consolidated-celex","r794-celex")
    assert graph.related("r794-consolidated-celex","TEXT_STATE_OF")[0]["node_id"] == "r794-celex"
    assert graph.related("r794-consolidated-nld","EXPRESSION_OF")[0]["node_id"] == "r794-consolidated-eli"


def test_corrigendum_is_own_resource_with_typed_target_relation():
    graph = _graph()
    assert graph.same_identity("r794-corr-celex","r794-corr-eli")
    assert not graph.same_identity("r794-corr-celex","r794-celex")
    assert graph.related("r794-corr-celex","CORRIGENDUM_OF")[0]["node_id"] == "r794-celex"


def test_historical_eli_is_resolved_not_generated():
    graph = _graph()
    eli = graph.find("ELI","http://data.europa.eu/eli/reg/1958/1(1)/oj")
    assert eli is not None
    assert graph.same_identity("r1958-celex","r1958-eli")
    assert graph.find("ELI","http://data.europa.eu/eli/reg/1958/1/oj") is None


def test_proposal_procedure_and_adopted_act_are_distinct_identities():
    graph = _graph()
    assert graph.same_identity("dsa-proposal-celex","dsa-proposal-com")
    assert not graph.same_identity("dsa-proposal-celex","dsa-act")
    assert not graph.same_identity("dsa-procedure","dsa-act")
    assert graph.related("dsa-proposal-celex","DOCUMENT_IN_PROCEDURE")[0]["node_id"] == "dsa-procedure"
    assert graph.related("dsa-act","RESULT_OF_PROCEDURE")[0]["node_id"] == "dsa-procedure"


def test_oj_citation_and_subdivision_are_relations_not_aliases():
    graph = _graph()
    assert not graph.same_identity("dsa-act","dsa-oj")
    assert graph.related("dsa-act","PUBLISHED_AS")[0]["node_id"] == "dsa-oj"
    assert not graph.same_identity("r2019-1241-art2-eli","r2019-1241-eli")
    assert graph.related("r2019-1241-art2-eli","SUBDIVISION_OF")[0]["node_id"] == "r2019-1241-eli"


def test_equivalence_relation_rejects_cross_level_nodes():
    broken = json.loads(json.dumps(FIXTURE))
    broken["relations"].append({
        "relation_id":"bad-same-document",
        "relation_type":"SAME_LEGAL_RESOURCE",
        "from_node_id":"r794-celex",
        "to_node_id":"r794-eng-expression",
        "evidence_state":"DIRECT",
        "source_refs":[{"source_type":"CELLAR","identifier":"bad","locator":None,"role":"EQUIVALENCE"}],
        "notes":None,
    })
    with pytest.raises(IdentityGraphError):
        TypedIdentifierGraph(broken)
