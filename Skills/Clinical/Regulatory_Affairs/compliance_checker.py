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
Regulatory Compliance Checker
-----------------------------
A new skill for 2026 that scans documents against specific regulatory frameworks (FDA, EMA).
It utilizes the BioKernel's Meta-Prompter to switch between strict "Auditor Mode" (OpenAI)
and explanatory "Consultant Mode" (Claude).
"""

import sys
import os
import json
from typing import Dict, Any

# Adjust path to find platform module
if __name__ == "__main__":
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../platform")))

try:
    from optimizer.meta_prompter import PromptOptimizer, ModelTarget
except ImportError:
    # Attempt to add path if not main
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../platform")))
    try:
         from optimizer.meta_prompter import PromptOptimizer, ModelTarget
    except ImportError:
        # Fallback mock
        class PromptOptimizer:
            def optimize(self, p, t): return p
        class ModelTarget:
            CLAUDE = "claude"
            OPENAI = "openai"

class RegulatoryComplianceChecker:
    def __init__(self):
        self.optimizer = PromptOptimizer()
        self.rules_db = {
            "FDA_21CFR_PART_11": [
                "Audit trails must be secure.",
                "Electronic signatures must be unique to the individual.",
                "Records must be retrievable throughout the retention period."
            ]
        }

    def check_document(self, document_text: str, standard: str = "FDA_21CFR_PART_11") -> Dict[str, Any]:
        """
        Simulates checking a document against a standard.
        """
        rules = self.rules_db.get(standard, [])
        if not rules:
            return {"error": f"Standard {standard} not found."}

        # 1. Optimize Prompt for an "Auditor" persona (OpenAI style - structured, strict)
        raw_prompt = f"""
        Standard: {standard}
        Rules: {json.dumps(rules)}
        Document: {document_text}
        
        Task: Identify violations. Return strictly structured JSON.
        """
        
        audit_prompt = self.optimizer.optimize(raw_prompt, ModelTarget.OPENAI)
        
        # 2. Simulate Findings (Logic-based mock for this demo)
        findings = []
        doc_lower = document_text.lower()
        
        for rule in rules:
            # Simple keyword matching for demo purposes
            if "signature" in rule.lower() and "password" in doc_lower:
                 # Broad catch for demo: any mention of password in context of signature rule is suspicious
                findings.append({
                    "rule": rule,
                    "status": "VIOLATION",
                    "evidence": "Found mention of 'password' which may violate unique signature requirements."
                })
            elif "audit" in rule.lower() and "no log" in doc_lower:
                findings.append({
                    "rule": rule,
                    "status": "VIOLATION",
                    "evidence": "Found 'no log' which violates audit trail requirement."
                })
            else:
                 findings.append({
                    "rule": rule,
                    "status": "COMPLIANT",
                    "evidence": "No obvious violation detected in text."
                })

        return {
            "standard": standard,
            "audit_prompt_used": audit_prompt, # Showing the internal prompt
            "findings": findings,
            "summary": f"Found {len([f for f in findings if f['status'] == 'VIOLATION'])} violations."
        }

if __name__ == "__main__":
    checker = RegulatoryComplianceChecker()
    
    sample_doc = """
    System Administration Manual:
    1. Users can access the system via the web portal.
    2. For convenience, all admins use a shared password 'Admin123'.
    3. Audit logs are deleted every day to save space (no log retention).
    """
    
    report = checker.check_document(sample_doc)
    print(json.dumps(report, indent=2))

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
