# Chemical Property Lookup

**ID:** `biomedical.drug_discovery.chemical_properties`
**Version:** 1.0.0
**Status:** Production
**Category:** Drug Discovery / Cheminformatics

---

## Overview

The **Chemical Property Lookup Skill** provides Python tools for calculating molecular properties using the **RDKit** cheminformatics library. It enables LLM agents to answer chemistry questions, validate compound structures, and assess drug-likeness without requiring deep cheminformatics expertise.

This skill serves as a foundational tool for drug discovery workflows, providing the molecular calculations that inform lead optimization decisions.

---

## Key Capabilities

### Implemented Functions

| Function | Input | Output | Use Case |
|----------|-------|--------|----------|
| `calculate_molecular_weight(smiles)` | SMILES string | Exact MW (Daltons) | Lipinski Rule of 5 check |
| `get_mol_block(smiles)` | SMILES string | MolBlock (2D coords) | Structure visualization, file export |

### Planned Extensions

| Function | Description | Status |
|----------|-------------|--------|
| `calculate_logp()` | Partition coefficient | Planned |
| `calculate_tpsa()` | Topological polar surface area | Planned |
| `count_hbd_hba()` | H-bond donors/acceptors | Planned |
| `calculate_qed()` | Drug-likeness score | Planned |
| `check_lipinski()` | Rule of 5 compliance | Planned |

---

## Usage

### As Agent Tools (LangChain)

```python
from langchain.tools import tool
from molecular_tools import calculate_molecular_weight, get_mol_block

@tool
def get_molecular_weight(smiles: str) -> str:
    """
    Calculate the molecular weight of a compound from its SMILES string.

    Args:
        smiles: SMILES representation of the molecule

    Returns:
        Molecular weight in Daltons, or error message if invalid SMILES
    """
    return calculate_molecular_weight(smiles)

@tool
def get_structure(smiles: str) -> str:
    """
    Convert SMILES to MolBlock format for visualization or file export.

    Args:
        smiles: SMILES representation of the molecule

    Returns:
        MolBlock string with 2D coordinates
    """
    return get_mol_block(smiles)

# Add to agent's tool list
tools = [get_molecular_weight, get_structure]
```

### Direct Python Usage

```python
from molecular_tools import calculate_molecular_weight, get_mol_block

# Calculate molecular weight of Aspirin
aspirin_smiles = "CC(=O)OC1=CC=CC=C1C(=O)O"
mw = calculate_molecular_weight(aspirin_smiles)
print(f"Aspirin MW: {mw}")  # Output: "Molecular weight: 180.16 Da"

# Get MolBlock for file export
molblock = get_mol_block(aspirin_smiles)
with open("aspirin.mol", "w") as f:
    f.write(molblock)
```

### Example Agent Interaction

**User:** What's the molecular weight of Ibuprofen (CC(C)Cc1ccc(cc1)C(C)C(=O)O)?

**Agent:** (Calls `get_molecular_weight` tool)

**Response:** The molecular weight of Ibuprofen is 206.28 Da.

---

## Technical Details

### SMILES Validation

The skill validates SMILES input before calculation:

```python
from rdkit import Chem

def validate_smiles(smiles: str) -> bool:
    """Check if SMILES string represents a valid molecule."""
    mol = Chem.MolFromSmiles(smiles)
    return mol is not None
```

### Error Handling

- Invalid SMILES returns descriptive error message
- Empty strings are rejected
- Disconnected fragments (salts) are handled appropriately

---

## Dependencies

```
rdkit>=2023.03
```

### Installation

```bash
# Recommended: conda installation (includes dependencies)
conda install -c conda-forge rdkit

# Alternative: pip installation
pip install rdkit
```

---

## Common SMILES Examples

| Compound | SMILES | MW |
|----------|--------|-----|
| Aspirin | `CC(=O)OC1=CC=CC=C1C(=O)O` | 180.16 |
| Ibuprofen | `CC(C)Cc1ccc(cc1)C(C)C(=O)O` | 206.28 |
| Caffeine | `CN1C=NC2=C1C(=O)N(C(=O)N2C)C` | 194.19 |
| Metformin | `CN(C)C(=N)NC(=N)N` | 129.16 |
| Atorvastatin | Complex SMILES | 558.64 |

---

## Integration with Other Skills

This skill provides foundational calculations for:

- **AgentD Drug Discovery:** Property prediction in molecule generation
- **Literature Mining:** Validating compound structures from papers
- **ADMET Prediction:** Input validation before property prediction

---

## API Reference

### `calculate_molecular_weight(smiles: str) -> str`

Calculates the exact molecular weight of a compound.

**Parameters:**
- `smiles` (str): SMILES representation of the molecule

**Returns:**
- str: Formatted string with molecular weight in Daltons, or error message

**Example:**
```python
>>> calculate_molecular_weight("CCO")
"Molecular weight: 46.07 Da"
>>> calculate_molecular_weight("invalid")
"Error: Invalid SMILES string"
```

### `get_mol_block(smiles: str) -> str`

Converts SMILES to MolBlock format with 2D coordinates.

**Parameters:**
- `smiles` (str): SMILES representation of the molecule

**Returns:**
- str: MolBlock string (V2000 format), or error message

**Example:**
```python
>>> molblock = get_mol_block("CCO")
>>> print(molblock[:50])
"
     RDKit          2D

  3  2  0  0  0..."
```

---

## Author

**MD BABU MIA**
*Artificial Intelligence Group*
*Icahn School of Medicine at Mount Sinai*
md.babu.mia@mssm.edu
