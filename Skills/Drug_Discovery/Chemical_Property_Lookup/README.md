# Chemical Property Lookup Skill

This skill provides python tools for calculating chemical properties using the **RDKit** library. It is designed to be used by agents (like ChemCrow or custom LangChain agents) to answer chemistry questions.

## Capabilities
- **Molecular Weight Calculation:** Calculates exact molecular weight from SMILES.
- **Structure Conversion:** Converts SMILES to MolBlock (for visualization/files).

## Usage

### As Agent Tools

You can wrap these functions as tools for your LLM agent.

**Example (LangChain):**

```python
from langchain.tools import tool
from molecular_tools import calculate_molecular_weight

@tool
def get_weight(smiles: str) -> str:
    """Useful for finding the molecular weight of a chemical compound given its SMILES string."""
    return calculate_molecular_weight(smiles)

# Add 'get_weight' to your agent's tool list
```

## Requirements
- `rdkit` (Recommended installation: `pip install rdkit`)
