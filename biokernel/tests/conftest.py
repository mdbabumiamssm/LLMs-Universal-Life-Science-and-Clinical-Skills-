# Copyright (c) 2026 MD Babu Mia, PhD. All Rights Reserved.

"""
Test configuration — resolves the `platform` package import conflict.

The directory name ``platform/`` shadows Python's stdlib ``platform`` module.
This conftest adds the project root to sys.path and uses importlib to ensure
our package is found correctly during test discovery.
"""

import sys
import os

# Ensure the skills root is on the path so `platform.*` resolves to our package
_skills_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _skills_root not in sys.path:
    sys.path.insert(0, _skills_root)
