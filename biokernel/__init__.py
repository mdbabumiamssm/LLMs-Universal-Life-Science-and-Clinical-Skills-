# BioKernel: Autonomous Biomedical AI Skills Platform
# Copyright (c) 2026 MD Babu Mia, PhD <md.babu.mia@mssm.edu>
# Icahn School of Medicine at Mount Sinai
# All Rights Reserved.

"""
BioKernel — Universal Biomedical Skills Platform
=================================================

An autonomous, agentic AI platform for orchestrating biomedical skills
across multiple LLM providers with:

- Universal Skill Description Language (USDL) for write-once, deploy-anywhere skills
- Semantic routing for intelligent skill matching
- DAG-based workflow engine for multi-agent orchestration
- Cross-platform evaluation with biomedical-domain rubrics
- MCP (Model Context Protocol) server for tool integration

Architecture::

    User Query → BioKernel Router → Skill Selection → Provider Adapter → LLM
                                                    ↓
                                          Workflow Engine (DAG)
                                                    ↓
                                          Evaluation Engine
"""

__version__ = "2026.4.0"
__author__ = "MD Babu Mia, PhD"
__email__ = "md.babu.mia@mssm.edu"
__institution__ = "Icahn School of Medicine at Mount Sinai"
