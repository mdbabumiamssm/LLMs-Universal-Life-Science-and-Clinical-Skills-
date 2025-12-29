# AgentD: Drug Discovery Agent

## Description
AgentD is an AI-driven agent designed to accelerate the early stages of drug discovery. It integrates literature mining, molecular property prediction, and generative chemistry to propose novel drug candidates.

## Capabilities
- **Literature Mining**: Extracts protein-ligand interaction data and structure-activity relationships (SAR) from scientific papers.
- **Molecule Generation**: Generates novel molecular structures using generative models (e.g., REINVENT, SMILES-based generation) optimized for specific properties.
- **Property Prediction**: Predicts ADMET (Absorption, Distribution, Metabolism, Excretion, Toxicity) properties and bioactivity.
- **Docking Simulation Setup**: Prepares input files for molecular docking simulations.

## Usage (Conceptual)

### Prerequisite
Integration with cheminformatics libraries (RDKit) and external APIs (e.g., ChEMBL, PubChem).

### Example Prompt
```text
Find small molecules that are known inhibitors of EGFR.
Based on the scaffold of Gefitinib, generate 5 new analogues with potentially better solubility (LogP < 4).
Predict their drug-likeness (QED score).
```

## References
- Based on **AgentD** ([hoon-ock/AgentD](https://github.com/hoon-ock/AgentD)).
- Related tools: ChemCrow, DrugAgent.
