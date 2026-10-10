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
OpenAI Health Stack – Clinical Ops Automator
-------------------------------------------
Produces structured documentation artifacts (coding hints, SOAP note, 
prior authorization packet) aligned with OpenAI's JSON-schema-first APIs.
"""

from __future__ import annotations

import json
from datetime import datetime
from typing import Any, Dict, List


class ClinicalSchemaViolation(Exception):
    pass


class ClinicalOpsAutomator:
    def __init__(self) -> None:
        self.allowed_sections = {"subjective", "objective", "assessment", "plan"}

    def draft_encounter_package(self, note: str, vitals: Dict[str, Any]) -> Dict[str, Any]:
        """Main entry point consumed by BioKernel / CLI."""
        package = {
            "generated_at": datetime.utcnow().isoformat(),
            "coding": {
                "icd10": self._suggest_icd_codes(note),
                "cpt": self._suggest_cpt_codes(note),
            },
            "soap_note": self._build_soap(note, vitals),
            "prior_authorization": self._build_prior_auth_hint(note, vitals),
        }
        self._validate(package)
        return package

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _suggest_icd_codes(self, note: str) -> List[Dict[str, str]]:
        icd_map = {
            "back pain": ("M54.50", "Low back pain, unspecified"),
            "hypertension": ("I10", "Essential (primary) hypertension"),
            "diabetes": ("E11.9", "Type 2 diabetes mellitus without complications"),
        }
        matches = []
        lower = note.lower()
        for keyword, (code, desc) in icd_map.items():
            if keyword in lower:
                matches.append({"code": code, "description": desc, "confidence": 0.82})
        return matches

    def _suggest_cpt_codes(self, note: str) -> List[Dict[str, str]]:
        cpt_codes = []
        if "mri" in note.lower():
            cpt_codes.append({"code": "72148", "description": "MRI lumbar spine w/o contrast"})
        if "follow up" in note.lower():
            cpt_codes.append({"code": "99214", "description": "Established patient visit"})
        return cpt_codes

    def _build_soap(self, note: str, vitals: Dict[str, Any]) -> Dict[str, Any]:
        soap = {section: "" for section in self.allowed_sections}
        soap["subjective"] = self._extract_section(note, ["chief complaint", "history"])
        soap["objective"] = f"Vitals: {json.dumps(vitals)}"
        soap["assessment"] = self._extract_section(note, ["assessment", "impression"])
        soap["plan"] = self._extract_section(note, ["plan", "recommendation"])
        return soap

    def _build_prior_auth_hint(self, note: str, vitals: Dict[str, Any]) -> Dict[str, Any]:
        required = {
            "clinical_rationale": self._extract_section(note, ["because", "due to", "secondary to"]),
            "supporting_vitals": vitals,
            "documents": [
                {"type": "clinical_note", "uri": "inline"},
            ],
        }
        return required

    def _extract_section(self, note: str, keywords: List[str]) -> str:
        lower = note.lower()
        for keyword in keywords:
            if keyword in lower:
                start = lower.index(keyword)
                return note[start : start + 400]
        return note[:200]

    def _validate(self, payload: Dict[str, Any]) -> None:
        if "coding" not in payload or "soap_note" not in payload:
            raise ClinicalSchemaViolation("Payload missing sections.")
        if not isinstance(payload["coding"]["icd10"], list):
            raise ClinicalSchemaViolation("ICD-10 suggestions must be a list.")
        for section in self.allowed_sections:
            if section not in payload["soap_note"]:
                raise ClinicalSchemaViolation(f"SOAP note missing {section}.")


def _demo() -> None:
    note = """Chief Complaint: Chronic low back pain. History: Failed PT and NSAIDs.
    Assessment: Lumbar radiculopathy. Plan: MRI lumbar spine and continue conservative care."""
    vitals = {"bp": "132/82", "hr": 78}
    automator = ClinicalOpsAutomator()
    package = automator.draft_encounter_package(note, vitals)
    print(json.dumps(package, indent=2))


if __name__ == "__main__":
    _demo()

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
