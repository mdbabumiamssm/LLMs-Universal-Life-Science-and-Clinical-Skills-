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
name: bio-metabolomics-peak-detection
description: Peak picking, feature detection, alignment and grouping using XCMS, MZmine
  3, or MS-DIAL.
tool_type: mixed
primary_tool: metabolomics
measurable_outcome: Execute skill workflow successfully with valid output within 15
  minutes.
allowed-tools:
- read_file
- run_shell_command
---

# ⛰️ Metabolomics Peak Detection

Peak picking, feature detection, chromatographic alignment and grouping. Supports XCMS, MZmine 3, and MS-DIAL outputs.

## CLI Reference

```bash
python omicsclaw.py run peak-detect --demo
python omicsclaw.py run peak-detect --input <data.csv> --output <dir>
```

## Citations

- [XCMS](https://doi.org/10.1021/ac051437y)
- [MZmine 3](https://doi.org/10.1038/s41587-023-01690-2)
- [MS-DIAL](https://doi.org/10.1038/nmeth.3393)

<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->