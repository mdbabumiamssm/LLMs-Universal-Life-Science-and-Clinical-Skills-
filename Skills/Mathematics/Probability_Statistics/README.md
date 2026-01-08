# Probability & Statistics for AI

This directory contains statistical methods and probabilistic models underpinning modern AI agents, particularly for experimental design and decision making under uncertainty.

## Contents

### `bayesian_optimization.py`
A from-scratch implementation of Bayesian Optimization, the engine behind **Self-Driving Labs**.

- **Gaussian Process (GP):** Acts as a surrogate model to estimate the outcome of experiments without actually running them.
- **Expected Improvement (EI):** Acquisition function that balances Exploration (trying high-uncertainty areas) vs Exploitation (trying high-value areas).
- **Usage:** Used to optimize chemical reactions, hyperparameters, or biological protocols with minimal trials.

## Usage
```python
from bayesian_optimization import BayesianOptimizer

# Optimize a function bounded between 0 and 10
opt = BayesianOptimizer(bounds=[(0, 10)])
next_exp = opt.suggest_next_point()
```