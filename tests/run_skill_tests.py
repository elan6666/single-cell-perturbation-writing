#!/usr/bin/env python3
"""Lightweight smoke tests for the skill package.

The tests intentionally use only the Python standard library so the repository
can be checked immediately after cloning.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_frontmatter() -> None:
    skill_files = sorted(SKILLS.glob("*/SKILL.md"))
    if len(skill_files) < 16:
        fail(f"expected at least 16 skill files, found {len(skill_files)}")

    for path in skill_files:
        text = read(path)
        if not text.startswith("---\n"):
            fail(f"{path} does not start with YAML front matter")
        match = re.match(r"---\nname: ([^\n]+)\ndescription: ([^\n]+)\n---\n", text)
        if not match:
            fail(f"{path} has invalid front matter shape")


def test_manifest() -> None:
    manifest = read(ROOT / "manifest.yml")
    required = [
        "perturbation-writing-do",
        "perturbation-prediction-writing",
        "trishift-writing-core",
        "perturbation-reviewer",
        "quiet_by_default",
        "patch_plan",
    ]
    for token in required:
        if token not in manifest:
            fail(f"manifest missing {token}")


def test_router_contract() -> None:
    router = read(SKILLS / "perturbation-writing-do" / "SKILL.md")
    required = [
        "Default to quiet routing",
        "trishift-writing-core",
        "State-Aware Defaults",
        "Routing Examples",
    ]
    for token in required:
        if token not in router:
            fail(f"router missing {token}")


def test_legacy_alias() -> None:
    legacy = read(SKILLS / "perturbation-prediction-writing" / "SKILL.md")
    if "Do not maintain a separate routing table here" not in legacy:
        fail("legacy entrypoint still looks like an independent router")
    if "Routing Table" in legacy:
        fail("legacy entrypoint contains a routing table")


def test_reference_files() -> None:
    for rel in [
        "references/metric-cards.md",
        "references/claim-ledger-template.md",
        "references/method-variable-scope.md",
        "references/latest-corpus-writing-guide.md",
        "references/paper-imitation-guide.md",
    ]:
        if not (ROOT / rel).exists():
            fail(f"missing {rel}")


def main() -> None:
    test_frontmatter()
    test_manifest()
    test_router_contract()
    test_legacy_alias()
    test_reference_files()
    print("OK: skill smoke tests passed")


if __name__ == "__main__":
    main()
