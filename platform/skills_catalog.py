# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

#!/usr/bin/env python3
"""Skill catalog + reliability report generator."""

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Tuple

import yaml

SKILLS_ROOT = Path("Skills")
OUTPUT_FILE = Path("skills_catalog.json")
RELIABILITY_OUTPUT = Path("skills_reliability_report.json")
REQUIRED_FIELDS = ["name", "description", "measurable_outcome", "allowed-tools"]


def _strip_leading_comments(text: str) -> str:
    """Remove HTML comment banners so frontmatter can be parsed."""
    stripped = text.lstrip()
    while stripped.startswith("<!--"):
        end_idx = stripped.find("-->")
        if end_idx == -1:
            break
        stripped = stripped[end_idx + 3 :].lstrip()
    return stripped


def parse_frontmatter(content: str) -> Tuple[Dict[str, Any], str]:
    """Parse YAML frontmatter from a SKILL.md file."""
    normalized = _strip_leading_comments(content)
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', normalized, re.DOTALL)
    if not match:
        return {}, content

    yaml_text, body = match.group(1), match.group(2)
    try:
        metadata = yaml.safe_load(yaml_text) or {}
    except yaml.YAMLError as exc:  # pragma: no cover - surfaced to users
        raise ValueError(f"Invalid YAML frontmatter: {exc}") from exc

    if not isinstance(metadata, dict):
        raise ValueError("Frontmatter must parse into a mapping.")

    return metadata, body


def scan_skills(root_dir: Path):
    """Recursively discover SKILL.md files and capture metadata + reliability."""
    catalog: List[Dict[str, Any]] = []
    errors: List[str] = []
    warnings: List[str] = []
    reliability_records: List[Dict[str, Any]] = []

    print(f"Scanning {root_dir} for skills...")

    for path in Path(root_dir).rglob("SKILL.md"):
        try:
            content = path.read_text(encoding="utf-8")
            metadata, _ = parse_frontmatter(content)

            if not metadata:
                warnings.append(f"Missing frontmatter in {path}")
                continue

            missing = [field for field in REQUIRED_FIELDS if field not in metadata]
            if missing:
                errors.append(f"Missing fields {missing} in {path}")
                metadata.setdefault("_validation_error", f"Missing: {missing}")

            metadata["file_path"] = str(path)
            metadata["last_modified"] = datetime.fromtimestamp(path.stat().st_mtime).isoformat()
            catalog.append(metadata)

            reliability_block = metadata.get("reliability") or metadata.get("source_reliability")
            if reliability_block:
                if not isinstance(reliability_block, list):
                    errors.append(f"Reliability block in {path} must be a list.")
                else:
                    for idx, entry in enumerate(reliability_block):
                        if not isinstance(entry, dict):
                            errors.append(f"Reliability entry {idx} in {path} must be a mapping.")
                            continue
                        source = entry.get("source")
                        score_raw = entry.get("score")
                        rationale = entry.get("rationale", "")
                        if not source:
                            errors.append(f"Reliability entry {idx} in {path} missing 'source'.")
                            continue
                        try:
                            score_val = float(score_raw)
                        except (TypeError, ValueError):
                            errors.append(f"Reliability entry {idx} in {path} missing/invalid 'score'.")
                            continue
                        reliability_records.append(
                            {
                                "skill": metadata.get("name", path.stem),
                                "file_path": str(path),
                                "source": source,
                                "score": score_val,
                                "rationale": rationale,
                            }
                        )

        except Exception as exc:  # pylint: disable=broad-except
            errors.append(f"Error processing {path}: {exc}")

    return catalog, errors, warnings, reliability_records


def write_json(path: Path, payload: Dict[str, Any]):
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Wrote {path} ({path.resolve()})")


def main():
    if not SKILLS_ROOT.exists():
        print(f"Error: Skills directory '{SKILLS_ROOT}' not found.")
        return

    catalog, errors, warnings, reliability_records = scan_skills(SKILLS_ROOT)

    write_json(
        OUTPUT_FILE,
        {
            "generated_at": datetime.now().isoformat(),
            "skills": catalog,
        },
    )

    if reliability_records:
        write_json(
            RELIABILITY_OUTPUT,
            {
                "generated_at": datetime.now().isoformat(),
                "sources": reliability_records,
            },
        )
    else:
        print("No reliability metadata detected; report not generated.")

    print(f"Total Skills Found: {len(catalog)}")

    if warnings:
        print("\nWarnings:")
        for warn in warnings:
            print(f"- {warn}")

    if errors:
        print("\nErrors:")
        for err in errors:
            print(f"- {err}")
    else:
        print("\nNo errors found. All skills valid.")


if __name__ == "__main__":
    main()

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
