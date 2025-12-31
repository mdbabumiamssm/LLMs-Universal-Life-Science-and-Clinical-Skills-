# Generative Quantum Chemistry Agent

## Overview
This agent utilizes **Quantum Circuit Born Machines (QCBM)** and hybrid quantum-GANs (QGANs) to generate novel small molecule structures. By exploiting the probabilistic nature of quantum mechanics, it explores chemical space more efficiently than classical generative models.

## Methodology
1.  **Quantum Distribution Loading**: Encodes chemical properties into quantum states.
2.  **QCBM Ansatz**: Uses parameterized quantum circuits to learn the distribution of valid SMILES tokens.
3.  **Hybrid Training**: Optimizes circuit parameters using classical gradient descent (PyTorch/TensorFlow).

## Integration
- **Insilico Medicine Pipeline**: Modeled after the hybrid quantum-classical workflows for drug discovery.
- **Qiskit Machine Learning**: Utilizes quantum kernels for property prediction.
