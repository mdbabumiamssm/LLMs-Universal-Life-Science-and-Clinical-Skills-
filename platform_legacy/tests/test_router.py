# Copyright (c) 2026 MD Babu Mia, PhD <md.babu.mia@mssm.edu>
# Icahn School of Medicine at Mount Sinai. All Rights Reserved.

"""
Tests for the BioKernel semantic skill router.

Validates that the TF-IDF-based router correctly matches biomedical
queries to the most relevant skills.
"""

import pytest
from platform.biokernel.router import SkillRouter
from platform.schema.io_types import SkillMetadata, SkillType


@pytest.fixture
def router():
    """Create a router with representative biomedical skills."""
    r = SkillRouter(similarity_threshold=0.1)

    skills = [
        SkillMetadata(
            skill_id="bioinformatics-singlecell",
            name="Single Cell Bioinformatics",
            description="Analyze scRNA-seq data with scanpy including QC, clustering, UMAP, and differential expression",
            skill_type=SkillType.SKILL_MD,
            file_path="/skills/singlecell/SKILL.md",
            tags=["single-cell", "scRNA-seq", "scanpy", "UMAP", "clustering"],
            capabilities=["QC filtering", "Normalization", "Clustering", "Differential expression"],
        ),
        SkillMetadata(
            skill_id="clinical-trial-matcher",
            name="Clinical Trial Matcher",
            description="Match patients to eligible clinical trials based on diagnosis, biomarkers, and inclusion criteria",
            skill_type=SkillType.SKILL_MD,
            file_path="/skills/clinical/SKILL.md",
            tags=["clinical", "trial", "matching", "eligibility"],
            capabilities=["Patient matching", "Eligibility screening", "NCT lookup"],
        ),
        SkillMetadata(
            skill_id="molecule-designer",
            name="Molecule Designer",
            description="Design and optimize small molecule drug candidates using generative chemistry and SMILES notation",
            skill_type=SkillType.SKILL_MD,
            file_path="/skills/drug/SKILL.md",
            tags=["drug-discovery", "chemistry", "SMILES", "molecule"],
            capabilities=["Molecule generation", "Property optimization", "ADMET prediction"],
        ),
        SkillMetadata(
            skill_id="mpn-research-assistant",
            name="MPN Research Assistant",
            description="Expert on myeloproliferative neoplasms including JAK2, CALR, MPL mutations and therapeutic strategies",
            skill_type=SkillType.SKILL_MD,
            file_path="/skills/mpn/SKILL.md",
            tags=["MPN", "JAK2", "CALR", "hematology", "myeloproliferative"],
            capabilities=["Mutation analysis", "Treatment guidance", "Prognosis scoring"],
        ),
        SkillMetadata(
            skill_id="variant-interpretation",
            name="Variant Interpretation",
            description="ACMG-based clinical variant classification for genetic testing reports",
            skill_type=SkillType.SKILL_MD,
            file_path="/skills/genetics/SKILL.md",
            tags=["ACMG", "variant", "pathogenic", "genetics", "VUS"],
            capabilities=["ACMG classification", "Pathogenicity assessment"],
        ),
    ]

    for s in skills:
        r.register_skill(s)

    return r


class TestSkillRouter:
    """Test suite for semantic routing."""

    def test_exact_match_override(self, router: SkillRouter):
        """When skill_id is provided, it should short-circuit to that skill."""
        matches = router.route("anything", skill_id="mpn-research-assistant")
        assert len(matches) == 1
        assert matches[0][0] == "mpn-research-assistant"
        assert matches[0][1] == 1.0

    def test_single_cell_query(self, router: SkillRouter):
        """Single-cell analysis queries should match the scRNA-seq skill."""
        best = router.get_best_match("analyze scRNA-seq data with UMAP clustering")
        assert best == "bioinformatics-singlecell"

    def test_clinical_trial_query(self, router: SkillRouter):
        """Clinical trial queries should match the trial matcher."""
        best = router.get_best_match("find clinical trials for my patient with lung cancer")
        assert best == "clinical-trial-matcher"

    def test_drug_discovery_query(self, router: SkillRouter):
        """Drug design queries should match the molecule designer."""
        best = router.get_best_match("design a small molecule inhibitor with SMILES optimization")
        assert best == "molecule-designer"

    def test_mpn_query(self, router: SkillRouter):
        """MPN-specific queries should match the MPN skill."""
        best = router.get_best_match("JAK2 V617F mutation in myeloproliferative neoplasms")
        assert best == "mpn-research-assistant"

    def test_variant_query(self, router: SkillRouter):
        """Variant interpretation queries should match the genetics skill."""
        best = router.get_best_match("classify BRCA1 variant using ACMG guidelines")
        assert best == "variant-interpretation"

    def test_top_k_returns_multiple(self, router: SkillRouter):
        """Top-k should return multiple ranked matches."""
        matches = router.route("analyze genomic data", top_k=3)
        assert len(matches) >= 1
        # Scores should be descending
        scores = [s for _, s in matches]
        assert scores == sorted(scores, reverse=True)

    def test_empty_router(self):
        """Empty router should return no matches."""
        r = SkillRouter()
        assert r.get_best_match("anything") is None

    def test_register_and_remove(self, router: SkillRouter):
        """Skills can be added and removed dynamically."""
        new_skill = SkillMetadata(
            skill_id="test-skill",
            name="Test Skill",
            description="A test skill for unit testing",
            skill_type=SkillType.SKILL_MD,
            file_path="/test/SKILL.md",
        )
        router.register_skill(new_skill)
        assert "test-skill" in router.skills

        router.remove_skill("test-skill")
        assert "test-skill" not in router.skills

    def test_threshold_filtering(self):
        """Queries below the similarity threshold should not match."""
        r = SkillRouter(similarity_threshold=0.99)
        r.register_skill(SkillMetadata(
            skill_id="specific-skill",
            name="Very Specific",
            description="only matches extremely specific queries about quantum entanglement",
            skill_type=SkillType.SKILL_MD,
            file_path="/test.md",
        ))
        matches = r.route("general biomedical question about proteins")
        assert len(matches) == 0


class TestRouterTokenizer:
    """Test the tokenization and TF-IDF internals."""

    def test_tokenize_removes_stop_words(self):
        tokens = SkillRouter._tokenize("the quick brown fox jumps over the lazy dog")
        assert "the" not in tokens
        assert "over" not in tokens
        assert "quick" in tokens

    def test_tokenize_handles_special_chars(self):
        tokens = SkillRouter._tokenize("JAK2-V617F mutation (p.Val617Phe)")
        assert "jak2" in tokens
        assert "v617f" in tokens
        assert "mutation" in tokens

    def test_cosine_similarity_identical(self):
        vec = {"a": 1.0, "b": 2.0}
        sim = SkillRouter._cosine_similarity(vec, vec)
        assert abs(sim - 1.0) < 1e-6

    def test_cosine_similarity_orthogonal(self):
        a = {"x": 1.0}
        b = {"y": 1.0}
        sim = SkillRouter._cosine_similarity(a, b)
        assert sim == 0.0

    def test_cosine_similarity_empty(self):
        assert SkillRouter._cosine_similarity({}, {"a": 1.0}) == 0.0
