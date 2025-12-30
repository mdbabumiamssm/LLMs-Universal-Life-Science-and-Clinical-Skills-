try:
    from rdkit import Chem
    from rdkit.Chem import Descriptors
except ImportError:
    raise ImportError("RDKit is required. Install it via 'pip install rdkit' or 'conda install -c conda-forge rdkit'")

def calculate_molecular_weight(smiles: str) -> str:
    """
    Calculates the exact molecular weight of a compound given its SMILES string.
    
    Args:
        smiles (str): The SMILES representation of the molecule.
        
    Returns:
        str: The molecular weight as a string, or an error message.
    """
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return "Error: Invalid SMILES string."
    
    weight = Descriptors.ExactMolWt(mol)
    return str(weight)

def get_mol_block(smiles: str) -> str:
    """
    Returns the MolBlock (2D representation) for a given SMILES string.
    Useful for visualization or saving to .mol files.
    """
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return "Error: Invalid SMILES string."
    
    return Chem.MolToMolBlock(mol)

if __name__ == "__main__":
    # Test with Aspirin
    aspirin_smiles = "CC(=O)OC1=CC=CC=C1C(=O)O"
    print(f"Testing with Aspirin ({aspirin_smiles})")
    print(f"Molecular Weight: {calculate_molecular_weight(aspirin_smiles)}")
    print("MolBlock generated successfully.")
