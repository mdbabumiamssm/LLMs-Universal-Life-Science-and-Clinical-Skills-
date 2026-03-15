<!--
# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

-->

---
name: semantic-code-indexing
description: Indexes code into a knowledge graph, enabling natural language search, impact analysis, and architectural understanding for AI agents.
keywords:
  - code
  - indexing
  - graph
  - semantic
  - mcp
measurable_outcome: Successfully indexes a target repository and answers structural queries with 95% accuracy.
license: MIT
metadata:
  author: Software Engineering Tools
  version: "1.0.0"
compatibility:
  - system: Multi-platform
allowed-tools:
  - run_shell_command
  - read_file
---

# Semantic Code Indexing

This skill provides AI agents with the ability to index codebases into knowledge graphs, allowing for deep, semantic understanding of code architecture and dependencies.

## When to Use This Skill

*   When a deep structural understanding of a legacy or complex codebase is needed.
*   For root cause analysis across multiple files.
*   To plan large-scale refactoring.

## Core Capabilities

1.  **Graph Construction**: Parses source code to build dependency and call graphs.
2.  **Semantic Search**: Allows querying the codebase using natural language.
3.  **Impact Analysis**: Identifies side effects of proposed code changes.

## Example Usage

**User**: "Index the current project and show me dependencies of the main entry point."

**Agent Action**:
```bash
python3 src/indexer/run.py --target . --query "dependencies of main"
```

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->