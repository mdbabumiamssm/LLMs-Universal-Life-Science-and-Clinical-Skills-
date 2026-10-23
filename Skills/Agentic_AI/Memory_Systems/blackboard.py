# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

from typing import Dict, Any, List
import time

# Shared Context Blackboard
# A centralized memory store where agents publish tasks and data.
# Enables decoupled collaboration between autonomous agents.

class Blackboard:
    def __init__(self):
        self._memory: Dict[str, Any] = {}
        self._logs: List[str] = []

    def write(self, key: str, value: Any, author: str):
        """Publish data to the shared context."""
        self._memory[key] = {
            "value": value,
            "author": author,
            "timestamp": time.time()
        }
        self._log(f"📌 {author} published to [{key}]: {str(value)[:50]}...")

    def read(self, key: str) -> Any:
        """Retrieve data from the shared context."""
        data = self._memory.get(key)
        if data:
            self._log(f"👀 Access read on [{key}]")
            return data["value"]
        return None

    def get_full_context(self) -> Dict[str, Any]:
        """Retrieve the complete system state."""
        return {k: v["value"] for k, v in self._memory.items()}

    def _log(self, message: str):
        self._logs.append(message)
        print(f"[Blackboard] {message}")

# Global Instance
shared_context = Blackboard()

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
