# AgentD: Drug Discovery Agent

**ID:** `biomedical.drug_discovery.agentd`
**Version:** 1.0.0
**Status:** Production
**Category:** Drug Discovery / Cheminformatics

---

## Overview

**AgentD** is an AI-driven agent that accelerates early-stage drug discovery by integrating literature mining, molecular property prediction, and generative chemistry. It enables researchers to move from target hypothesis to novel compound candidates in a fraction of the traditional timeline.

Drug discovery is resource-intensive: it takes $2.6B and 10-15 years to bring a drug to market. AgentD addresses early-stage bottlenecks by automating literature synthesis, scaffold optimization, and ADMET prediction.

---

## Key Capabilities

### 1. Literature Mining

Extracts actionable data from scientific publications:

| Data Type | Sources | Output |
|-----------|---------|--------|
| **Protein-Ligand Interactions** | PubMed, ChEMBL literature | Binding affinity data, IC50 values |
| **Structure-Activity Relationships (SAR)** | Medicinal chemistry papers | Functional group contributions |
| **Known Inhibitors/Activators** | DrugBank, ChEMBL | Reference compound sets |
| **Clinical Outcomes** | Trial publications | Efficacy/safety signals |

### 2. Molecule Generation

Creates novel molecular structures optimized for specific properties:

- **REINVENT-based generation:** Reinforcement learning for property optimization
- **SMILES-based design:** Direct string manipulation with validity checks
- **Scaffold hopping:** Bioisosteric replacements while maintaining activity
- **Fragment-based design:** Growing fragments into lead compounds

### 3. Property Prediction

Predicts critical drug-likeness parameters:

| Property | Description | Target Range |
|----------|-------------|--------------|
| **LogP** | Lipophilicity | 1-3 (oral drugs) |
| **TPSA** | Topological Polar Surface Area | <140 (oral absorption) |
| **MW** | Molecular Weight | <500 (Lipinski) |
| **HBD/HBA** | H-bond donors/acceptors | ≤5 / ≤10 |
| **QED** | Quantitative Estimate of Drug-likeness | >0.5 |
| **ADMET** | Absorption, Distribution, Metabolism, Excretion, Toxicity | Acceptable profiles |

### 4. Docking Simulation Setup

- Prepares ligand and protein structures for docking
- Generates input files for AutoDock Vina, Glide, GOLD
- Post-processes docking results for ranking

---

## Usage

### Example Prompt

```text
Find small molecules that are known inhibitors of EGFR (Epidermal Growth Factor Receptor).
Based on the scaffold of Gefitinib, generate 5 new analogues with:
- Improved solubility (LogP < 4)
- Maintained kinase binding (preserve quinazoline core)
- Drug-like properties (QED > 0.5)

Predict their ADMET properties and rank by overall drug-likeness.
```

### Expected Output

```
## EGFR Inhibitor Design Results

### Reference Compound
- **Gefitinib** (SMILES: COc1cc2ncnc(Nc3ccc(F)c(Cl)c3)c2cc1OCCCN1CCOCC1)
- LogP: 3.2, MW: 446.9, QED: 0.67

### Generated Analogues

| ID | SMILES | LogP | MW | QED | TPSA | Rank |
|----|--------|------|-----|-----|------|------|
| GEF-01 | [SMILES] | 2.8 | 432 | 0.71 | 78 | 1 |
| GEF-02 | [SMILES] | 3.1 | 458 | 0.68 | 85 | 2 |
| GEF-03 | [SMILES] | 2.5 | 418 | 0.73 | 72 | 3 |
| GEF-04 | [SMILES] | 3.4 | 471 | 0.62 | 91 | 4 |
| GEF-05 | [SMILES] | 2.9 | 445 | 0.69 | 80 | 5 |

### ADMET Predictions (Top Candidate: GEF-01)
- **Absorption:** High intestinal absorption predicted
- **Distribution:** CNS penetration unlikely (desired for peripheral target)
- **Metabolism:** CYP3A4 substrate (moderate)
- **Excretion:** Hepatic clearance predicted
- **Toxicity:** No hERG liability predicted
```

### LLM Agent Integration

```python
@tool
def design_drug_candidates(
    target_protein: str,
    reference_compound: str = None,
    num_candidates: int = 5,
    optimization_goals: list[str] = ["drug-likeness"]
) -> str:
    """
    Designs novel drug candidates for a target protein.

    Args:
        target_protein: Gene symbol or UniProt ID of target
        reference_compound: SMILES of reference compound (optional)
        num_candidates: Number of candidates to generate
        optimization_goals: Properties to optimize (solubility, potency, selectivity)

    Returns:
        Ranked list of candidates with predicted properties
    """
    pass
```

---

## Prerequisites

### Required APIs/Databases

| Resource | Purpose | Access |
|----------|---------|--------|
| **ChEMBL** | Bioactivity data | Public API |
| **PubChem** | Chemical structures | Public API |
| **UniProt** | Target sequences | Public API |
| **RDKit** | Molecular calculations | Python library |

### Dependencies

```
rdkit>=2023.03
requests>=2.28
pandas>=1.5
numpy>=1.24
torch>=2.0  # For generative models
```

---

## Methodology

### Molecule Generation Pipeline

1. **Seed selection:** Start from reference compound or de novo
2. **Property optimization:** Reinforcement learning with multi-objective reward
3. **Validity filtering:** Ensure chemical feasibility (valence, ring systems)
4. **Diversity selection:** Cluster candidates to maximize chemical space coverage
5. **ADMET prediction:** Filter for acceptable drug-like profiles

### Scoring Functions

```python
def calculate_qed(smiles: str) -> float:
    """Quantitative Estimate of Drug-likeness (Bickerton et al. 2012)"""
    from rdkit import Chem
    from rdkit.Chem.QED import qed
    mol = Chem.MolFromSmiles(smiles)
    return qed(mol) if mol else 0.0

def calculate_druglikeness_score(smiles: str, target_logp: float = 3.0) -> float:
    """Multi-parameter optimization score"""
    from rdkit import Chem
    from rdkit.Chem import Descriptors, Crippen

    mol = Chem.MolFromSmiles(smiles)
    if not mol:
        return 0.0

    logp = Crippen.MolLogP(mol)
    mw = Descriptors.MolWt(mol)
    hbd = Descriptors.NumHDonors(mol)
    hba = Descriptors.NumHAcceptors(mol)

    # Lipinski penalties
    score = 1.0
    if mw > 500: score -= 0.2
    if logp > 5: score -= 0.2
    if hbd > 5: score -= 0.1
    if hba > 10: score -= 0.1

    # Target LogP bonus
    if abs(logp - target_logp) < 0.5:
        score += 0.1

    return max(0, score)
```

---

## Related Skills

- **Chemical Property Lookup:** RDKit-based property calculations
- **CRISPR Design Agent:** Target validation through gene knockout
- **Literature Mining:** Automated hypothesis generation from publications

---

## References

- Based on **AgentD** by Hoon-Ock et al. ([hoon-ock/AgentD](https://github.com/hoon-ock/AgentD))
- Related frameworks: ChemCrow, DrugAgent, REINVENT
- Bickerton et al. "Quantifying the chemical beauty of drugs." *Nature Chemistry* (2012)

---

## Author

**MD BABU MIA**
*Artificial Intelligence Group*
*Icahn School of Medicine at Mount Sinai*
md.babu.mia@mssm.edu
