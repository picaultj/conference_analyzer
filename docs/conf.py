"""Sphinx configuration for the ConfLens documentation.

The docs are plain Markdown (rendered through MyST), so this build never
imports ConfLens itself — no LLM/NiceGUI dependencies are needed on Read the
Docs. The version is read straight from ``pyproject.toml`` to keep it in sync
with the release that `release.yml` bumps.
"""

import tomllib
from pathlib import Path

_pyproject = tomllib.loads(
    (Path(__file__).parent.parent / "pyproject.toml").read_text(encoding="utf-8")
)

project = "ConfLens"
author = _pyproject["project"]["authors"][0]["name"]
copyright = f"2025, {author}"  # noqa: A001 - Sphinx expects this name
release = _pyproject["project"]["version"]
version = ".".join(release.split(".")[:2])

extensions = ["myst_parser", "sphinxcontrib.mermaid"]

exclude_patterns = ["_build", "requirements.txt", "Thumbs.db", ".DS_Store"]

# -- MyST ---------------------------------------------------------------------
# `colon_fence` lets directives be written as ::: blocks; heading anchors make
# the README's in-page "Contents" links (#quick-start, ...) resolve.
myst_enable_extensions = ["colon_fence", "deflist", "linkify", "substitution"]
myst_heading_anchors = 3

# Render GitHub-style ```mermaid fences (used throughout ARCHITECTURE.md and the
# README) through sphinxcontrib-mermaid instead of trying to syntax-highlight them.
myst_fence_as_directive = ["mermaid"]

# -- HTML ---------------------------------------------------------------------
html_theme = "furo"
html_title = f"{project} {release}"
html_static_path = ["_static"]
