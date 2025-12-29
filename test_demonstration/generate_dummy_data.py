import anndata
import numpy as np
import pandas as pd
from scipy import sparse

def create_dummy_h5ad(filename="test_input.h5ad", n_cells=100, n_genes=200):
    print(f"Generating dummy data with {n_cells} cells and {n_genes} genes...")
    
    # Create random count matrix
    counts = sparse.csr_matrix(np.random.randint(0, 100, size=(n_cells, n_genes)))
    
    # Create obs (cells) dataframe
    obs = pd.DataFrame(index=[f"cell_{i}" for i in range(n_cells)])
    obs['batch'] = np.random.choice(['batch1', 'batch2'], size=n_cells)
    
    # Create var (genes) dataframe
    var = pd.DataFrame(index=[f"gene_{i}" for i in range(n_genes)])
    # Mark some genes as mitochondrial
    var['mt'] = False
    var.iloc[:10, var.columns.get_loc('mt')] = True  # First 10 genes are "mitochondrial"
    # Rename them to start with MT- for realism if the QC script checks names, 
    # though the QC script likely uses a list or regex. 
    # Let's check the qc_core.py later. For now, this is a placeholder.
    # Actually, let's rename the index for the first 10 genes
    new_index = list(var.index)
    for i in range(10):
        new_index[i] = f"MT-{i}"
    var.index = new_index

    # Create AnnData object
    adata = anndata.AnnData(X=counts, obs=obs, var=var)
    
    # Save
    adata.write_h5ad(filename)
    print(f"Saved to {filename}")

if __name__ == "__main__":
    create_dummy_h5ad()
