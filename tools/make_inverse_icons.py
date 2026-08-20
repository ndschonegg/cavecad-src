#!/usr/bin/env python3
"""Generate missing dark-theme icon variants.

RGuiAction::getIconPath loads "Name-inverse.svg" instead of "Name.svg"
when the GUI background is dark. Upstream QCAD ships inverse variants for
only part of the icon set; this script creates the missing ones by turning
black line work white, following the upstream convention (accent colors
and grays are left alone).

Usage: python3 tools/make_inverse_icons.py [--dry-run]
Run from the repository root. Safe to re-run; existing -inverse.svg files
are never overwritten.
"""

import re
import sys
from pathlib import Path

SKIP_NAMES = {"cavecad_icon.svg"}


def invert(svg: str) -> str:
    # black -> white; negative lookahead keeps longer hex colors
    # (e.g. #000080) intact
    svg = re.sub(r"#000000(?![0-9a-fA-F])", "#ffffff", svg)
    svg = re.sub(r"#000(?![0-9a-fA-F])", "#fff", svg)
    svg = re.sub(r"(?<![-\w])black(?![-\w])", "white", svg)
    # SVG's default fill is black, so shapes without any fill would still
    # render black on a dark background; a fill on the root element only
    # reaches elements that don't specify their own.
    if re.search(r"<svg\b[^>]*\bfill=", svg) is None:
        svg = re.sub(r"<svg\b", '<svg fill="#ffffff"', svg, count=1)
    return svg


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    root = Path("scripts")
    if not root.is_dir():
        print("run from the repository root (scripts/ not found)", file=sys.stderr)
        return 1

    created = 0
    for src in sorted(root.rglob("*.svg")):
        if src.name.endswith("-inverse.svg") or src.name in SKIP_NAMES:
            continue
        dst = src.with_name(src.stem + "-inverse.svg")
        if dst.exists():
            continue
        if dry_run:
            print(f"would create {dst}")
        else:
            dst.write_text(invert(src.read_text(encoding="utf-8")), encoding="utf-8")
        created += 1

    print(f"{'would create' if dry_run else 'created'} {created} inverse icons")
    return 0


if __name__ == "__main__":
    sys.exit(main())
