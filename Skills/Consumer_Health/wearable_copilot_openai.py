# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

"""
OpenAI Health Stack – Care Copilot (Universal Edition)
------------------------------------------------------
Transforms wearable and patient-reported data into a schema-enforced
coaching plan for health coaching. 

Updates (Jan 2026):
- Integration with Agentic AI Self-Correction.
- Enhanced Schema Validation.
- Statistical Anomaly Detection (Z-Score).
"""

from __future__ import annotations

import json
import sys
import os
from dataclasses import dataclass, asdict
from datetime import datetime
from statistics import mean, stdev
from typing import Any, Dict, List

# Adjust path to find platform module if running standalone
if __name__ == "__main__":
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../platform")))

class SchemaValidationError(Exception):
    """Raised when a generated payload violates the declared schema."""

@dataclass
class CarePlan:
    user_id: str
    generated_at: str
    vitals_summary: Dict[str, Any]
    risk_flags: List[Dict[str, Any]]
    recommendations: List[Dict[str, Any]]

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2)


class OpenAIHealthCareCopilot:
    """
    Harmonises wearable telemetry and emits OpenAI-style JSON payloads.
    The schema mirrors public ChatGPT Health demos (summary + actions).
    """

    REQUIRED_VITAL_KEYS = {"resting_heart_rate", "sleep_score", "hrr_variability"}

    def __init__(self) -> None:
        self.stream_buffer: List[Dict[str, Any]] = []

    def ingest_wearable_stream(self, samples: List[Dict[str, Any]]) -> None:
        """Accepts streamed wearable points and keeps the last 30 entries."""
        self.stream_buffer.extend(samples)
        self.stream_buffer = sorted(self.stream_buffer, key=lambda s: s["timestamp"])[-30:]

    def generate_care_plan(self, patient_profile: Dict[str, Any]) -> CarePlan:
        """
        Generates a schema-compliant care plan.
        `patient_profile` contains demographics + optional clinician goals.
        """
        vitals = self._summarise_vitals()
        flags = self._detect_risks(vitals, patient_profile)
        recommendations = self._build_recommendations(flags, patient_profile)

        plan = CarePlan(
            user_id=patient_profile.get("user_id", "anonymous"),
            generated_at=datetime.utcnow().isoformat(),
            vitals_summary=vitals,
            risk_flags=flags,
            recommendations=recommendations,
        )
        self._validate_schema(asdict(plan))
        return plan

    def generate_synthetic_insight(self, plan: CarePlan) -> str:
        """
        Uses the Meta-Prompter to construct a prompt for OpenAI.
        If 'SelfCorrectionAgent' is available, it uses it to refine the output.
        """
        # Try to import SelfCorrectionAgent robustly
        try:
            # Add repo root to path if not present
            repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
            if repo_root not in sys.path:
                sys.path.append(repo_root)
            
            from Skills.Agentic_AI.Agent_Architectures.Self_Correction.self_correction_agent import SelfCorrectionAgent
            
            agent = SelfCorrectionAgent()
            task = f"Analyze this care plan and provide a patient-facing summary: {plan.to_json()}"
            criteria = ["Be empathetic", "Highlight top risk", "Propose one immediate action", "Keep it under 50 words"]
            
            print(">> Delegating to SelfCorrectionAgent for insight generation...")
            result = agent.run_cycle(task, criteria, max_iterations=1)
            return result["final_output"]

        except ImportError as e:
            print(f"Warning: Could not import SelfCorrectionAgent ({e}). Falling back to MetaPrompter or basic.")

        try:
            from optimizer.meta_prompter import PromptOptimizer, ModelTarget
            optimizer = PromptOptimizer()
            raw_prompt = f"""
            Data: {plan.to_json()}
            Task: Summarize this care plan for the patient in a friendly, encouraging tone.
            """
            optimized = optimizer.optimize(raw_prompt, ModelTarget.OPENAI)
            return f"[Simulated AI Response via MetaPrompter]:\nBased on your data, please rest today. Your HR is elevated."
        except ImportError:
             return "Optimizer not found. Insight generation unavailable."


    # ------------------
    # Internal helpers
    # ------------------

    def _summarise_vitals(self) -> Dict[str, Any]:
        if not self.stream_buffer:
            return {}

        field_history: Dict[str, List[float]] = {}
        for entry in self.stream_buffer:
            for key, value in entry.items():
                if key == "timestamp":
                    continue
                # Ensure value is float
                try:
                    val = float(value)
                    field_history.setdefault(key, []).append(val)
                except ValueError:
                    continue

        summary = {}
        for key, values in field_history.items():
            if not values: continue
            
            # Calculate basic stats
            s_mean = mean(values)
            s_std = stdev(values) if len(values) > 1 else 0.0
            
            summary[key] = {
                "latest": values[-1],
                "avg_7d": mean(values[-7:]) if len(values) >= 7 else s_mean,
                "std_dev": s_std,
                "trend": values[-1] - values[0],
                "history_len": len(values)
            }
        return summary

    def _detect_risks(
        self, vitals: Dict[str, Any], patient_profile: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """
        Uses Z-score anomaly detection if enough history (n>5), else falls back to static thresholds.
        """
        risk_flags: List[Dict[str, Any]] = []
        
        # Default static thresholds
        thresholds = patient_profile.get(
            "thresholds",
            {"resting_heart_rate": 5, "sleep_score": -10, "hrr_variability": -15},
        )
        
        Z_SCORE_THRESHOLD = 2.0  # Deviations > 2 sigma are flagged

        for metric, stats in vitals.items():
            latest = stats["latest"]
            avg = stats.get("avg_7d", stats["latest"]) # Approximate baseline
            std_dev = stats.get("std_dev", 0)
            history_len = stats.get("history_len", 0)
            
            is_anomaly = False
            msg = ""
            severity = "low"

            # Method A: Statistical (Preferred)
            if history_len > 5 and std_dev > 0.1:
                z_score = (latest - avg) / std_dev
                
                # Logic varies by metric directionality
                if metric == "resting_heart_rate" and z_score > Z_SCORE_THRESHOLD:
                    is_anomaly = True
                    severity = "high" if z_score > 3 else "medium"
                    msg = f"Resting HR is {z_score:.1f} sigma above baseline."
                
                elif metric in ["sleep_score", "hrr_variability"] and z_score < -Z_SCORE_THRESHOLD:
                    is_anomaly = True
                    severity = "high" if z_score < -3 else "medium"
                    msg = f"{metric} is {-z_score:.1f} sigma below baseline."

            # Method B: Threshold Fallback
            else:
                change = stats.get("trend", 0)
                if metric == "resting_heart_rate" and change > thresholds.get("resting_heart_rate", 5):
                    is_anomaly = True
                    severity = "medium"
                    msg = f"Resting HR increased by {change:.1f} bpm (static check)."
                elif metric in thresholds and change < thresholds[metric]:
                    is_anomaly = True
                    severity = "medium"
                    msg = f"{metric} dropped by {change:.1f} points (static check)."

            if is_anomaly:
                risk_flags.append({
                    "metric": metric,
                    "severity": severity,
                    "message": msg
                })

        return risk_flags

    def _build_recommendations(
        self, flags: List[Dict[str, Any]], patient_profile: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        if not flags:
            return [
                {
                    "goal": "maintain",
                    "action": "Continue current routines; no anomalies detected.",
                    "category": "general",
                }
            ]

        recs: List[Dict[str, Any]] = []
        for flag in flags:
            if flag["metric"] == "resting_heart_rate":
                recs.append(
                    {
                        "goal": "reduce stress load",
                        "action": "Schedule low-intensity recovery day, ensure hydration, and revisit stimulant intake.",
                        "category": "cardio",
                    }
                )
            elif flag["metric"] == "sleep_score":
                recs.append(
                    {
                        "goal": "improve sleep hygiene",
                        "action": "Enforce a fixed bedtime, limit evening screen time, and track caffeine cut-off.",
                        "category": "sleep",
                    }
                )
            else:
                recs.append(
                    {
                        "goal": "boost recovery",
                        "action": "Introduce guided breathing or HRV biofeedback session before bed.",
                        "category": "recovery",
                    }
                )
        return recs

    def _validate_schema(self, payload: Dict[str, Any]) -> None:
        missing = [k for k in CarePlan.__annotations__.keys() if k not in payload]
        if missing:
            raise SchemaValidationError(f"CarePlan payload missing keys: {missing}")
        if not isinstance(payload["risk_flags"], list):
            raise SchemaValidationError("`risk_flags` must be a list.")
        if not isinstance(payload["recommendations"], list):
            raise SchemaValidationError("`recommendations` must be a list.")


def _demo() -> None:
    # Generate data with a spike at the end
    stream = [
        {"timestamp": datetime(2026, 1, i + 1).isoformat(), "resting_heart_rate": 60 + (i%2), "sleep_score": 85}
        for i in range(10)
    ]
    # Add a spike
    stream.append({"timestamp": datetime(2026, 1, 11).isoformat(), "resting_heart_rate": 75, "sleep_score": 50})
    
    copilot = OpenAIHealthCareCopilot()
    copilot.ingest_wearable_stream(stream)
    profile = {"user_id": "patient_001", "thresholds": {"resting_heart_rate": 4, "sleep_score": -8, "hrr_variability": -10}}
    plan = copilot.generate_care_plan(profile)
    
    print("\n--- JSON Plan ---")
    print(plan.to_json())
    
    print("\n--- Synthetic Insight ---")
    print(copilot.generate_synthetic_insight(plan))


if __name__ == "__main__":
    _demo()
__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
