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
name: multi-cloud-pricing
description: Compares pricing across major cloud providers (AWS, Azure, GCP, OCI) for various instance types, aiding in cost optimization.
keywords:
  - cloud
  - pricing
  - finops
  - mcp
measurable_outcome: Generates a cost comparison report across 3 providers within 2 minutes.
license: MIT
metadata:
  author: Software Engineering Tools
  version: "1.0.0"
compatibility:
  - system: Multi-platform
allowed-tools:
  - run_shell_command
---

# Multi-Cloud Pricing Analysis

This skill provides comparative pricing metrics for infrastructure components across major cloud providers, enabling cost-effective architecture planning.

## When to Use This Skill

*   When planning migration to the cloud.
*   To optimize existing infrastructure costs.
*   To perform "what-if" scenarios for scaling up services.

## Core Capabilities

1.  **Cross-Cloud Querying**: Fetches up-to-date pricing data via provider APIs.
2.  **Resource Normalization**: Matches equivalent instance types (e.g., vCPUs, RAM) across providers.
3.  **Cost Projections**: Estimates monthly/yearly spend based on usage patterns.

## Example Usage

**User**: "Compare the cost of a 16 vCPU, 64GB RAM instance on AWS and GCP."

**Agent Action**:
```bash
python3 src/cloud_tools/pricing_comparator.py --vcpu 16 --ram 64 --providers aws,gcp
```

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->