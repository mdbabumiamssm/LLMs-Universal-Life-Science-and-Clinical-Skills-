#!/usr/bin/env python3
# Copyright (c) 2026 MD Babu Mia, PhD <md.babu.mia@mssm.edu>
# Icahn School of Medicine at Mount Sinai. All Rights Reserved.

"""
Skills Catalog Scanner — discovers, validates, and indexes SKILL.md files.
Also generates a skill reliability report.

Uses proper YAML parsing (PyYAML) instead of homebrew frontmatter parsing.
Generates a JSON catalog for the BioKernel runtime and external tooling.
"""

from __future__ import annotations

import json
import re
import yaml
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple

from platform.observability import get_logger

logger = get_logger("skills_catalog")

SKILLS_ROOT = Path("Skills")
OUTPUT_FILE = Path("skills_catalog.json")
RELIABILITY_OUTPUT = Path("skills_reliability_report.json")
REQUIRED_FIELDS = ["name", "description"]


def _strip_leading_comments(text: str) -> str:
    """Remove HTML comment banners so frontmatter can be parsed."""
    stripped = text.lstrip()
    while stripped.startswith("<!--"):
        end_idx = stripped.find("-->")
        if end_idx == -1:
            break
        stripped = stripped[end_idx + 3 :].lstrip()
    return stripped


def parse_skill_md(content: str) -> Tuple[Dict[str, Any] | None, str]:
    """
    Parse a SKILL.md file's YAML frontmatter and markdown body.

    Uses PyYAML for robust parsing instead of line-by-line heuristics.

    Args:
        content: Full file content.

    Returns:
        (metadata_dict, body_text) or (None, body_text) if no frontmatter.
    """
    normalized = _strip_leading_comments(content)
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", normalized, re.DOTALL)
    if not match:
        return None, content

    yaml_text = match.group(1)
    body = match.group(2)

    try:
        metadata = yaml.safe_load(yaml_text)
        if not isinstance(metadata, dict):
            return None, content
        return metadata, body
    except yaml.YAMLError as exc:
        logger.warning("YAML parse error in frontmatter", error=str(exc))
        return None, content


def scan_skills(root_dir: str) -> Tuple[List[Dict[str, Any]], List[str], List[str], List[Dict[str, Any]]]:
    """
    Recursively find and parse all SKILL.md files and capture metadata + reliability.

    Args:
        root_dir: Root directory to scan.

    Returns:
        (catalog_list, errors_list, warnings_list, reliability_records_list)
    """
    catalog: List[Dict[str, Any]] = []
    errors: List[str] = []
    warnings: List[str] = []
    reliability_records: List[Dict[str, Any]] = []

    root = Path(root_dir)
    if not root.exists():
        errors.append(f"Root directory not found: {root_dir}")
        return catalog, errors, warnings, reliability_records

    logger.info("Scanning for skills", root=root_dir)

    for path in sorted(root.rglob("SKILL.md")):
        try:
            content = path.read_text(encoding="utf-8")
            metadata, body = parse_skill_md(content)

            if metadata is None:
                warnings.append(f"Missing frontmatter: {path}")
                continue

            # Validate required fields
            missing = [f for f in REQUIRED_FIELDS if f not in metadata]
            if missing:
                errors.append(f"Missing fields {missing}: {path}")
                metadata["_validation_errors"] = missing

            # Enrich with file metadata
            metadata["file_path"] = str(path)
            metadata["relative_path"] = str(path.relative_to(root))
            metadata["last_modified"] = datetime.fromtimestamp(
                path.stat().st_mtime, tz=timezone.utc
            ).isoformat()
            metadata["body_length"] = len(body)

            # Extract capabilities from body headings
            metadata["capabilities"] = re.findall(r"^#+\s+(.+)$
", body, re.MULTILINE)

            catalog.append(metadata)

            # Reliability Extraction
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

        except Exception as exc:
            errors.append(f"Error processing {path}: {exc}")

    logger.info("Scan complete", skills_found=len(catalog), errors=len(errors))
    return catalog, errors, warnings, reliability_records


def write_json(path: Path, payload: Dict[str, Any]):
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {path} ({path.resolve()})")


def generate_catalog(
    root_dir: str = str(SKILLS_ROOT),
    output_file: str = str(OUTPUT_FILE),
) -> Dict[str, Any]:
    """
    Scan skills and write a JSON catalog.

    Returns:
        The catalog dict (also written to disk).
    """
    catalog, errors, warnings, reliability_records = scan_skills(root_dir)

    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "generator": "BioKernel Skills Catalog v2026.4.0",
        "total_skills": len(catalog),
        "total_errors": len(errors),
        "skills": catalog,
        "errors": errors,
        "warnings": warnings,
    }

    write_json(Path(output_file), result)

    if reliability_records:
        rel_result = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "sources": reliability_records,
        }
        write_json(RELIABILITY_OUTPUT, rel_result)
    else:
        print("No reliability metadata detected; report not generated.")

    return result


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import sys

    root = sys.argv[1] if len(sys.argv) > 1 else str(SKILLS_ROOT)
    result = generate_catalog(root)

    print(f"\nBioKernel Skills Catalog")
    print(f"  Skills found: {result['total_skills']}")
    print(f"  Errors: {result['total_errors']}")
    print(f"  Warnings: {len(result.get('warnings', []))}")
    print(f"  Output: {OUTPUT_FILE.absolute()}")

    if result["errors"]:
        print("\nErrors:")
        for err in result["errors"][:10]:
            print(f"  - {err}")
    
    if result.get("warnings"):
        print("\nWarnings:")
        for warn in result["warnings"][:10]:
            print(f"  - {warn}")