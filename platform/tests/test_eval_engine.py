# Copyright (c) 2026 MD Babu Mia, PhD <md.babu.mia@mssm.edu>
# Icahn School of Medicine at Mount Sinai. All Rights Reserved.

"""
Tests for the evaluation engine assertion checker.

Validates each assertion type with representative biomedical outputs.
"""

import pytest
from platform.evaluator.eval_engine import AssertionChecker, EvaluationEngine
from platform.schema.io_types import EvalAssertion, EvalCase


@pytest.fixture
def checker():
    return AssertionChecker()


class TestAssertionChecker:
    """Test individual assertion types."""

    def test_contains_pass(self, checker: AssertionChecker):
        passed, reason = checker.check({"contains": "BRCA1"}, "The BRCA1 gene is mutated.")
        assert passed

    def test_contains_fail(self, checker: AssertionChecker):
        passed, reason = checker.check({"contains": "TP53"}, "The BRCA1 gene is mutated.")
        assert not passed

    def test_contains_case_insensitive(self, checker: AssertionChecker):
        passed, _ = checker.check({"contains": "brca1"}, "The BRCA1 gene is important.")
        assert passed

    def test_not_contains_pass(self, checker: AssertionChecker):
        passed, _ = checker.check({"not_contains": "ricin"}, "This is a safe compound.")
        assert passed

    def test_not_contains_fail(self, checker: AssertionChecker):
        passed, _ = checker.check({"not_contains": "harmful"}, "This is a harmful substance.")
        assert not passed

    def test_regex_pass(self, checker: AssertionChecker):
        passed, _ = checker.check({"regex": r"NCT\d{8}"}, "Trial NCT12345678 is active.")
        assert passed

    def test_regex_fail(self, checker: AssertionChecker):
        passed, _ = checker.check({"regex": r"NCT\d{8}"}, "No trial information available.")
        assert not passed

    def test_json_valid_pass(self, checker: AssertionChecker):
        passed, _ = checker.check(
            {"json_valid": True},
            '{"gene": "EGFR", "variant": "L858R"}',
        )
        assert passed

    def test_json_valid_fail(self, checker: AssertionChecker):
        passed, _ = checker.check({"json_valid": True}, "Not valid JSON at all")
        assert not passed

    def test_length_min_pass(self, checker: AssertionChecker):
        passed, _ = checker.check({"length_min": 10}, "This is a long enough response.")
        assert passed

    def test_length_min_fail(self, checker: AssertionChecker):
        passed, _ = checker.check({"length_min": 1000}, "Short.")
        assert not passed

    def test_length_max_pass(self, checker: AssertionChecker):
        passed, _ = checker.check({"length_max": 100}, "Short response.")
        assert passed

    def test_length_max_fail(self, checker: AssertionChecker):
        passed, _ = checker.check({"length_max": 5}, "This response is too long.")
        assert not passed

    def test_safety_check_pass(self, checker: AssertionChecker):
        output = "Please consult your physician before making any changes."
        passed, _ = checker.check({"safety_check": True}, output)
        assert passed

    def test_safety_check_fail(self, checker: AssertionChecker):
        passed, _ = checker.check({"safety_check": True}, "Take 500mg daily.")
        assert not passed

    def test_biomedical_entity_gene(self, checker: AssertionChecker):
        passed, reason = checker.check(
            {"entity_type": "gene"},
            "EGFR and TP53 are commonly mutated in NSCLC.",
        )
        assert passed
        assert "EGFR" in reason or "TP53" in reason

    def test_biomedical_entity_drug(self, checker: AssertionChecker):
        passed, _ = checker.check(
            {"entity_type": "drug"},
            "Gefitinib is an EGFR inhibitor. Imatinib targets BCR-ABL.",
        )
        assert passed

    def test_biomedical_entity_nct(self, checker: AssertionChecker):
        passed, _ = checker.check(
            {"entity_type": "nct"},
            "Enrolled in NCT04561234.",
        )
        assert passed

    def test_citation_check_pmid(self, checker: AssertionChecker):
        passed, _ = checker.check(
            {"citation_check": True},
            "As shown by Smith et al. (PMID: 12345678).",
        )
        assert passed

    def test_citation_check_doi(self, checker: AssertionChecker):
        passed, _ = checker.check(
            {"citation_check": True},
            "Published in Nature (doi:10.1038/s41586-024-1234).",
        )
        assert passed

    def test_citation_check_year(self, checker: AssertionChecker):
        passed, _ = checker.check(
            {"citation_check": True},
            "Smith et al. (2024) reported significant findings.",
        )
        assert passed

    def test_citation_check_fail(self, checker: AssertionChecker):
        passed, _ = checker.check(
            {"citation_check": True},
            "Gene expression was significantly upregulated.",
        )
        assert not passed

    def test_unknown_assertion_type(self, checker: AssertionChecker):
        passed, reason = checker.check({"unknown_type": "value"}, "any output")
        assert passed  # Unknown types are skipped
        assert "skipped" in reason.lower()


class TestEvaluationEngine:
    """Test the full evaluation pipeline."""

    def test_run_single_eval_mock(self):
        """Mock executor should produce results."""
        engine = EvaluationEngine()
        case = EvalCase(
            name="test_basic",
            input="What is BRCA1?",
            assertions=[
                EvalAssertion(assertion_type="length_min", value="5"),
            ],
        )
        result = engine.run_single_eval(case)
        assert result.case_name == "test_basic"
        assert result.output  # Should have mock output

    def test_custom_executor(self):
        """Custom executor should be used when provided."""
        engine = EvaluationEngine()
        case = EvalCase(
            name="test_custom",
            input="test input",
            assertions=[
                EvalAssertion(assertion_type="contains", value="custom"),
            ],
        )

        def my_executor(input_text):
            return f"custom response for: {input_text}"

        result = engine.run_single_eval(case, my_executor)
        assert result.passed
        assert "custom" in result.output

    def test_all_assertions_fail(self):
        """When all assertions fail, score should be 0."""
        engine = EvaluationEngine()
        case = EvalCase(
            name="test_fail",
            input="test",
            assertions=[
                EvalAssertion(assertion_type="contains", value="nonexistent_string_xyz"),
                EvalAssertion(assertion_type="contains", value="another_missing_string"),
            ],
        )

        def executor(inp):
            return "simple response"

        result = engine.run_single_eval(case, executor)
        assert result.score == 0.0
        assert not result.passed
