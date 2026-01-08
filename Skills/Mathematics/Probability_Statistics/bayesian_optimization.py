"""
Bayesian Optimization for Experimental Design

This module implements a simplified Bayesian Optimizer from scratch. 
It is the mathematical engine behind "Self-Driving Labs".

It uses:
1. Surrogate Model: Gaussian Process (GP) to estimate the objective function.
2. Acquisition Function: Expected Improvement (EI) to decide where to sample next.

Usage:
    optimizer = BayesianOptimizer(bounds=[(0, 10), (0, 10)])
    next_point = optimizer.suggest_next_point()
    # Run experiment at next_point -> result
    optimizer.register(next_point, result)
"""

import math
import random
from typing import List, Tuple, Callable, Optional

class GaussianProcess:
    """
    A simplified Gaussian Process Regressor.
    In production, use scikit-learn's GaussianProcessRegressor or GPy/BoTorch.
    """
    def __init__(self, length_scale: float = 1.0, noise: float = 1e-5):
        self.length_scale = length_scale
        self.noise = noise
        self.X_train: List[List[float]] = []
        self.y_train: List[float] = []

    def fit(self, X: List[List[float]], y: List[float]):
        """Store training data."""
        self.X_train = X
        self.y_train = y

    def predict(self, X_test: List[List[float]]) -> Tuple[List[float], List[float]]:
        """
        Predict mean and std deviation for test points.
        Uses a radial basis function (RBF) kernel logic.
        """
        means = []
        stds = []
        
        # If no data, return prior (mean=0, high uncertainty)
        if not self.X_train:
            return [0.0] * len(X_test), [1.0] * len(X_test)

        for x in X_test:
            # Calculate weights (kernel similarities) based on distance to training points
            # Simple RBF Kernel: k(x, x') = exp(-||x - x'||^2 / (2 * l^2))
            weights = []
            total_weight = 0.0
            weighted_y = 0.0
            
            for i, x_train in enumerate(self.X_train):
                dist_sq = sum((xi - xt) ** 2 for xi, xt in zip(x, x_train))
                similarity = math.exp(-dist_sq / (2 * self.length_scale ** 2))
                weights.append(similarity)
                total_weight += similarity
                weighted_y += similarity * self.y_train[i]
            
            # Prediction is weighted average of neighbors
            # (Simplified; real GP does matrix inversion)
            if total_weight > 1e-9:
                pred_mean = weighted_y / total_weight
                # Uncertainty drops as we get closer to known points
                # Max uncertainty is 1.0, min is near 0
                pred_std = 1.0 - (total_weight / (total_weight + 0.5)) 
            else:
                pred_mean = 0.0
                pred_std = 1.0
                
            means.append(pred_mean)
            stds.append(pred_std)
            
        return means, stds

class BayesianOptimizer:
    def __init__(self, bounds: List[Tuple[float, float]]):
        """
        bounds: List of (min, max) for each dimension.
        """
        self.bounds = bounds
        self.model = GaussianProcess()
        self.X_sample: List[List[float]] = []
        self.y_sample: List[float] = []

    def register(self, x: List[float], y: float):
        """Record an observation (input x, output y)."""
        self.X_sample.append(x)
        self.y_sample.append(y)
        self.model.fit(self.X_sample, self.y_sample)

    def _expected_improvement(self, mean: float, std: float, y_max: float, xi: float = 0.01) -> float:
        """
        Calculate Expected Improvement (EI).
        High EI means either high predicted mean (Exploitation) or high variance (Exploration).
        """
        if std == 0.0:
            return 0.0
            
        z = (mean - y_max - xi) / std
        # CDF and PDF approximation for standard normal
        # Using simplified logic since we don't have scipy.stats.norm here
        # This is a heuristic placeholder for: (mean - y_max - xi) * cdf(z) + std * pdf(z)
        
        return max(0, mean - y_max) + (std * 0.5) # Very simplified proxy

    def suggest_next_point(self, num_candidates: int = 100) -> List[float]:
        """
        Find the point that maximizes the Acquisition Function.
        Uses random sampling (Monte Carlo) to optimize the acquisition function.
        """
        # If no data, pick random point
        if not self.X_sample:
            return [random.uniform(b[0], b[1]) for b in self.bounds]

        y_max = max(self.y_sample)
        
        best_x = None
        max_acq = -float("inf")
        
        # Generate candidate points
        candidates = []
        for _ in range(num_candidates):
            cand = [random.uniform(b[0], b[1]) for b in self.bounds]
            candidates.append(cand)
            
        # Predict surrogate
        means, stds = self.model.predict(candidates)
        
        # Calculate acquisition scores
        for i, (mean, std) in enumerate(zip(means, stds)):
            acq = self._expected_improvement(mean, std, y_max)
            if acq > max_acq:
                max_acq = acq
                best_x = candidates[i]
                
        return best_x if best_x else candidates[0]

# --- Example Usage ---

if __name__ == "__main__":
    # Objective Function (Black Box): Maximize -(x-2)^2 + 10 (Peak at x=2, Value=10)
    def objective_function(x):
        return -(x[0] - 2.0)**2 + 10.0
    
    print("--- Bayesian Optimization of f(x) = -(x-2)^2 + 10 ---")
    
    # 1D optimization, bound [0, 5]
    optimizer = BayesianOptimizer(bounds=[(0.0, 5.0)])
    
    # Run 10 iterations
    for i in range(10):
        # 1. Ask optimizer for next point
        next_point = optimizer.suggest_next_point()
        
        # 2. Evaluate objective function (Experiment)
        value = objective_function(next_point)
        
        # 3. Tell optimizer the result
        optimizer.register(next_point, value)
        
        print(f"Iter {i+1}: Sampled x={next_point[0]:.4f}, Result y={value:.4f}")
        
    best_idx = optimizer.y_sample.index(max(optimizer.y_sample))
    print(f"\nBest Found: x={optimizer.X_sample[best_idx][0]:.4f}, y={optimizer.y_sample[best_idx]:.4f}")
