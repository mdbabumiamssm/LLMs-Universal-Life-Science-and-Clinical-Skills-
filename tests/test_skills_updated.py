# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA


import sys
import os
import unittest
from datetime import datetime

# Adjust path to include project root AND platform folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../platform")))

# Import Skills
from Skills.Anthropic_Health_Stack.regulatory_drafter import RegulatoryDrafter
from Skills.Clinical.Prior_Authorization.anthropic_coworker import PriorAuthCoworker
from Skills.Consumer_Health.wearable_copilot_openai import OpenAIHealthCareCopilot
from Skills.Clinical.Regulatory_Affairs.compliance_checker import RegulatoryComplianceChecker

class TestUpdatedSkills(unittest.TestCase):

    def test_regulatory_drafter(self):
        print("\nTesting RegulatoryDrafter...")
        drafter = RegulatoryDrafter()
        result = drafter.draft_submission(
            clinical_data="Study 101: No pediatric patients.", 
            fda_guidance="Waiver allowed if disease non-existent in children."
        )
        
        self.assertIsInstance(result, dict)
        self.assertIn("trace", result)
        self.assertIn("draft", result)
        self.assertIn("prompt_used", result)
        print("RegulatoryDrafter passed.")

    def test_prior_auth_coworker(self):
        print("\nTesting PriorAuthCoworker...")
        coworker = PriorAuthCoworker()
        case = {
            "case_id": "TEST-001",
            "procedure_code": "MRI-L-SPINE",
            "clinical_note": "Persistent back pain for 10 weeks. Failed therapy. Red flags present."
        }
        payload = coworker.review(case)
        
        self.assertIsInstance(payload, dict)
        self.assertEqual(payload["decision"], "APPROVED")
        self.assertIn("trace", payload)
        self.assertTrue(payload["trace"].startswith("<thinking>"))
        print("PriorAuthCoworker passed.")

    def test_wearable_copilot(self):
        print("\nTesting OpenAIHealthCareCopilot...")
        copilot = OpenAIHealthCareCopilot()
        # Mock stream
        stream = [
            {"timestamp": datetime(2026, 1, i + 1).isoformat(), "resting_heart_rate": 60 + i, "sleep_score": 85 - i, "hrr_variability": 50}
            for i in range(10)
        ]
        copilot.ingest_wearable_stream(stream)
        profile = {"user_id": "test_user"}
        
        # 1. Test Plan Generation
        plan = copilot.generate_care_plan(profile)
        self.assertIsNotNone(plan)
        
        # 2. Test Insight Generation (Meta-Prompter Integration)
        insight = copilot.generate_synthetic_insight(plan)
        self.assertIn("[System Prompt Sent to OpenAI]", insight)
        print("OpenAIHealthCareCopilot passed.")

    def test_compliance_checker(self):
        print("\nTesting RegulatoryComplianceChecker...")
        checker = RegulatoryComplianceChecker()
        doc = "All admins share the password '12345'."
        report = checker.check_document(doc)
        
        self.assertIsInstance(report, dict)
        self.assertIn("audit_prompt_used", report)
        self.assertIn("findings", report)
        
        # Check if it caught the violation (based on our mock logic)
        violations = [f for f in report["findings"] if f["status"] == "VIOLATION"]
        self.assertTrue(len(violations) > 0)
        print("RegulatoryComplianceChecker passed.")

if __name__ == "__main__":
    unittest.main()

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
