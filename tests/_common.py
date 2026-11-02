"""Shared helpers for the Project Falcon checks. Standard library only."""
import hashlib
import json
import os
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
TARGETS = ROOT / "targets"
DEFAULT_TARGET = "falcon"
MANIFEST_NAME = "data_manifest.json"
EM_DASH = "—"


def run_dir():
    """Folder holding a diligence run (memory/ and output/). Set with run_all.py --run."""
    return (ROOT / os.environ.get("FALCON_RUN_DIR", ".")).resolve()


def run_target(run=None):
    """Name of the target a run used: memory/target.txt, or falcon for runs saved before targets/ existed."""
    path = (run or run_dir()) / "memory" / "target.txt"
    name = read(path).strip() if path.exists() else ""
    return name or DEFAULT_TARGET


def targets():
    """Every target folder that has a data manifest, so its data checks can run."""
    return sorted(p for p in TARGETS.iterdir() if (p / MANIFEST_NAME).exists()) if TARGETS.exists() else []


def target_checks(target):
    """Optional per-target expectations from targets/<target>/checks.json ({} if there is none)."""
    path = target / "checks.json"
    return json.loads(read(path)) if path.exists() else {}


def is_real(target):
    """A real public company's target (written by tools/fetch_edgar.py), not a fictional one."""
    return target_checks(target).get("real") is True


def read(path):
    return pathlib.Path(path).read_text(encoding="utf-8")


def frontmatter(path):
    """Return the YAML frontmatter of a Markdown file as a dict of simple key: value pairs."""
    match = re.match(r"^---\n(.*?)\n---\n", read(path), re.S)
    if not match:
        return None
    fields = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"')
    return fields


def table_rows(text):
    """Return the body rows of every Markdown table as lists of cells (separator rows removed)."""
    rows = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("|") and line.endswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if all(set(c) <= set("-: ") for c in cells):
                continue
            rows.append(cells)
    return rows


def protected_files(target):
    """A target's source data and answer key: files that must never change during a run."""
    files = sorted(p for p in (target / "data").rglob("*") if p.is_file())
    files.append(target / "evaluation" / "answer-key.md")
    return files


def checksums(target):
    """Checksums keyed by path inside the target folder (data/..., evaluation/answer-key.md)."""
    return {p.relative_to(target).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in protected_files(target) if p.exists()}


def write_manifest(target):
    path = target / MANIFEST_NAME
    path.write_text(json.dumps(checksums(target), indent=2) + "\n", encoding="utf-8")
    return path
