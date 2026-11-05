# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

import numpy as np
from dataclasses import dataclass
from typing import List

@dataclass
class TrialArm:
    name: str
    patients: int = 0
    successes: int = 0
    active: bool = True

class BayesianAdaptiveTrial:
    """
    Simulates a Multi-Arm Multi-Stage (MAMS) adaptive clinical trial.
    Uses Bayesian Inference to calculate the probability that a treatment arm 
    is better than control.
    """

    def __init__(self, arm_names: List[str], prior_alpha=1, prior_beta=1):
        self.arms = {name: TrialArm(name) for name in arm_names}
        self.control_name = arm_names[0] # Assume first is control
        self.alpha = prior_alpha
        self.beta = prior_beta

    def update_data(self, arm_name: str, new_patients: int, new_successes: int):
        """Adds new patient data to an arm."""
        if arm_name not in self.arms:
            raise ValueError(f"Arm {arm_name} not found.")
        
        self.arms[arm_name].patients += new_patients
        self.arms[arm_name].successes += new_successes

    def calculate_posterior(self, arm_name: str):
        """
        Calculates Beta posterior parameters (alpha, beta).
        Mean = alpha / (alpha + beta)
        """
        arm = self.arms[arm_name]
        post_alpha = self.alpha + arm.successes
        post_beta = self.beta + (arm.patients - arm.successes)
        return post_alpha, post_beta

    def probability_better_than_control(self, arm_name: str, n_samples=10000) -> float:
        """
        Monte Carlo simulation to find P(Treatment > Control).
        """
        if arm_name == self.control_name:
            return 0.0
        
        # Sample from Treatment Posterior
        t_alpha, t_beta = self.calculate_posterior(arm_name)
        t_samples = np.random.beta(t_alpha, t_beta, n_samples)
        
        # Sample from Control Posterior
        c_alpha, c_beta = self.calculate_posterior(self.control_name)
        c_samples = np.random.beta(c_alpha, c_beta, n_samples)
        
        # Calculate fraction where Treatment > Control
        return np.mean(t_samples > c_samples)

    def run_interim_analysis(self, futility_threshold=0.1, efficacy_threshold=0.95):
        """
        Checks all active arms. 
        Drops arms with P(Treat > Control) < futility_threshold.
        Declares success if P(Treat > Control) > efficacy_threshold.
        """
        print("\n--- Interim Analysis ---")
        for name, arm in self.arms.items():
            if not arm.active or name == self.control_name:
                continue
                
            prob_better = self.probability_better_than_control(name)
            print(f"Arm {name}: Patients={arm.patients}, Rate={arm.successes/arm.patients:.2f}, P(>Control)={prob_better:.3f}")
            
            if prob_better < futility_threshold:
                print(f"  -> DROPPING Arm {name} for futility.")
                arm.active = False
            elif prob_better > efficacy_threshold:
                print(f"  -> SUCCESS: Arm {name} is significantly better!")
                # In MAMS, might continue to gather more data or stop early.

# --- Simulation Demo ---
if __name__ == "__main__":
    # Setup Trial: Control vs 3 Drugs
    trial = BayesianAdaptiveTrial(["Control", "DrugA", "DrugB", "DrugC"])
    
    # Phase 1: 20 patients per arm
    # True Rates: Control=0.3, DrugA=0.3 (Useless), DrugB=0.4 (Marginal), DrugC=0.6 (Effective)
    np.random.seed(42)
    
    print("Simulating Batch 1 (20 patients/arm)...")
    trial.update_data("Control", 20, np.random.binomial(20, 0.3))
    trial.update_data("DrugA", 20, np.random.binomial(20, 0.3))
    trial.update_data("DrugB", 20, np.random.binomial(20, 0.4))
    trial.update_data("DrugC", 20, np.random.binomial(20, 0.6))
    
    trial.run_interim_analysis()
    
    # Phase 2: Recruit 20 more for remaining active arms
    print("\nSimulating Batch 2 (20 more patients for active arms)...")
    for name in ["Control", "DrugA", "DrugB", "DrugC"]:
        if trial.arms[name].active:
            # Keep same true rates
            rate = {"Control":0.3, "DrugA":0.3, "DrugB":0.4, "DrugC":0.6}[name]
            trial.update_data(name, 20, np.random.binomial(20, rate))
            
    trial.run_interim_analysis()

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
