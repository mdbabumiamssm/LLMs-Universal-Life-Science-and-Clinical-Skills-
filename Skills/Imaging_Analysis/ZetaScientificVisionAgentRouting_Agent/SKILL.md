<!--
# COPYRIGHT NOTICE
# This file is part of the "Universal AI Agentic Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA
-->



<!-- AUTHOR_SIGNATURE: 9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE -->

---
name: 'zeta-scientific-vision-agent-routing'
description: 'Implement and evaluate scientific image-analysis routing separately from visual execution using explicit intent policies, tool contracts, traceable artifacts, and separate error metrics.'
measurable_outcome: 'Execute skill workflow successfully with valid output within 15 minutes.'
allowed-tools:
  - read_file
  - run_shell_command
  - web_fetch
---

# ZETA Scientific Vision Agent Routing

## Overview

Separate scientific intent selection from image-tool execution so that a wrong operation can be distinguished from an incorrect visual result. This skill applies ZETA's architectural principle through auditable routing records, explicit executor contracts, and independent evaluation of both stages.

### Evidence and implementation boundary

The [versioned paper](https://arxiv.org/html/2611.06760v1), checked on 2026-11-05, describes routing from query text and non-pixel context before specialized visual execution. Its evaluated categories are count, describe, detect, segment, and text-only; Section 4 identifies Zenesis for segmentation and optional deterministic measurement from compatible geometry. The study evaluates 51 intent queries, not 51 unique images, and measures routing rather than downstream visual accuracy or clinical performance; improvements vary by model.

An official ZETA implementation, installable package, and executable API were not verified in the paper or accompanying search. The contracts and workflow below are proposed integration conventions, not released ZETA interfaces. Before using any claimed release, verify its provenance, revision, task inventory, dependencies, and callable schemas against its documentation. Do not invent installation commands or infer biomedical validation from routing results.

## When to Use This Skill

- Build a scientific imaging assistant that must choose among localization, counting, outlining, and description.
- Diagnose whether a plausible-looking result came from an inappropriate operation or failed perception.
- Compare explicit routing guidance against an unchanged legal tool interface.
- Add reproducible measurements and provenance to an existing image-analysis pipeline.
- Audit ambiguous requests at boundaries such as object detection versus segmentation.

## Core Capabilities

1. **Define the legal interface separately from policy.** Inventory available adapters, their versions, and their actual supported inputs and outputs. Freeze the route enumeration and schemas before comparing policies. Mark unavailable capabilities explicitly; never silently substitute description for segmentation or detection for counting.

2. **Specify intent-to-route rules.** Use the requested deliverable, not isolated keywords, to select a route. The following table is a proposed policy for local adaptation; verify each adapter before enabling it.

   | Route | Requested deliverable | Required evidence or output |
   | --- | --- | --- |
   | `describe` | Qualitative image appearance | Image-grounded text; no invented counts or measurements |
   | `detect` | Object locations | Boxes or points with coordinate convention and image reference |
   | `count` | Number of target instances | Integer and documented counting method, with instance evidence when available |
   | `segment` | Pixel membership or boundaries | Mask or polygons with dimensions, labels, and spatial mapping |
   | `text_only` | Explanation answerable without image inspection | Text response with no image executor call |

   An image-specific question remains a visual task even if the image is missing. Record the intended route and block execution pending the image. Treat area, length, or other measurements as explicit postprocessing requests with geometry prerequisites; a bounding box is not an object boundary. For multiple requested outputs, create linked atomic routing records and dependencies. If materially different interpretations remain, record `needs_clarification` and the missing distinction before dispatch.

3. **Persist routing decisions before execution.** Route using query text, permitted metadata, and the fixed interface. Keep pixels and downstream results out of the router's decision input. Record a concise decision justification, not hidden reasoning, and preserve the original record if a later revision is necessary.

   Minimum routing record:

   ```yaml
   request_id: sample-001
   query: "Outline the particles in this image."
   context: {image_id: image-001, target: particles}
   interface_version: local-v1
   policy_version: explicit-v1
   router_model_revision: deployment-specific
   inference_settings: {temperature: 0}
   route: segment
   requested_measurement: null
   status: ready
   decision_basis: "The requested output is object boundaries."
   dependencies: []
   ```

   Validate enumeration membership, required fields, argument types, and measurement compatibility before dispatch. A legal route can still be semantically wrong. Keep adjudicated reference labels in the evaluation harness, outside router inputs.

4. **Enforce tool contracts and retain artifacts.** For each adapter, specify accepted image formats, dimensions and channels, target specification, coordinate origin, pixel versus physical units, permitted parameters, timeout, and output schema. Require an execution record linked to the routing record containing tool/model revision, input checksum, parameters, start/end times, status, artifact references, validation results, and errors. Validate mask dimensions and label conventions, finite in-bounds coordinates, and nonnegative integer counts. Treat contract validity and scientific correctness as distinct checks. Use `not_run`, `timeout`, `tool_error`, and `invalid_artifact` explicitly; missing results are not zero counts. Bound retries and retain every attempt without silently changing the route.

5. **Compute measurements from explicit geometry.** Accept validated masks, polygons, or task-appropriate geometric objects, and record the formula, calibration, units, and source artifact. For a binary 2D mask with pixel spacings `sx` and `sy`, compute area as foreground-pixel count times `sx * sy`. Without calibration, report pixel area only. Record thresholding, connectivity, overlap handling, and border exclusions when they affect counts or geometry. Deterministic arithmetic does not establish that the source segmentation is correct.

6. **Evaluate routing and execution independently.** Prepare adjudicated intent labels, task-specific reference artifacts where available, and a frozen scoring protocol. Compare an interface-only condition with an explicit-policy condition while holding the queries, model revision, legal routes, schemas, measurement options, and inference configuration fixed. Keep labels hidden and report repeated-run variation if decoding is stochastic.

   Report these proposed evaluation measures with numerator, denominator, exclusions, and sample counts:

   - Routing accuracy: correct routes divided by all labeled requests; invalid outputs and abstentions count as unsuccessful in this primary measure. Also report coverage and accuracy among answered requests.
   - Per-route recall and a confusion matrix, retaining invalid outputs and abstentions as separate prediction categories. Distinguish schema-invalid decisions from legal-but-wrong routes.
   - Execution contract pass rate: valid artifacts divided by attempted executions, with failures and retries itemized.
   - Conditional execution success: successful intended executions divided by correctly routed, execution-required requests. Include blocked or failed executions in the denominator and state the reason.
   - End-to-end success: requests with both correct routing and successful intended execution divided by all execution-required requests. Score text-only answers separately.
   - Task quality when reference data exist: detection precision/recall under a fixed matching rule, count absolute error, segmentation Dice/IoU, measurement error, or description rubric scores. Define thresholds and empty-reference handling before scoring. Without reference data, mark scientific correctness as unassessed.

   To compare executor quality without routing selection bias, additionally force each intended route on the same eligible cases and label this as an oracle-route evaluation. Report misrouting and downstream artifact defects independently; both can occur in the same request. Do not present contract compliance or routing accuracy as segmentation accuracy, biomedical efficacy, or clinical readiness.

### Bounded workflow

For a 15-minute smoke run with existing adapters, spend approximately three minutes confirming capabilities and inputs, four defining the frozen contracts and routing rules, five processing a small labeled fixture set, and three validating traces and calculating metrics. Include a localization-versus-boundary pair, a missing-image request, and an invalid-artifact case when fixtures permit. This is a local smoke test, not reproduction of the paper's benchmark.

Stop dispatch for unresolved intent, incompatible measurement geometry, or an unavailable required adapter, and return the recorded blocker. If implementation or reference data are absent, deliver a clearly labeled design-only result with proposed contracts and evaluation cases; do not claim execution or scientific validation. Completion requires every attempted request to have a routing record, an execution status or explicit non-execution reason, and metrics whose denominators reconcile with those records.

## Inputs / Outputs

**Inputs:** Scientific requests; image identifiers and accessible image data for execution; permitted non-pixel context; target definitions; optional spatial calibration; verified tool inventory and schemas; router and executor revisions; execution budget; and optional adjudicated routing labels and reference annotations.

**Outputs:** A versioned action interface and routing policy; immutable linked routing and execution records; validated artifact references and geometry-derived measurements where supported; a routing confusion matrix and separate execution-quality report; and explicit unresolved, unavailable, or unassessed items. Write artifacts only to destinations within the user's requested scope. A design-only result must identify which adapters, data, or references are still needed for a real run.

## References

- Shubhabrata Mukherjee, Jeffrey Donatelli, and Daniela Ushizima. *Route First, See Later: Enabling Vision Agents to Reason Scientifically by Separating Routing Policy from Action Spaces*. arXiv:2611.06760v1, 2026. [Source finding](http://arxiv.org/abs/2611.06760v1); [full text, architecture and evaluation](https://arxiv.org/html/2611.06760v1).
