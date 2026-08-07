#!/usr/bin/env python3
"""Valida que cada skill exista y declare el frontmatter esperado."""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from sevencs.paths import REPO_ROOT

SKILLS = (
    "7cs-canvas-ingest",
    "7cs-business-context",
    "7cs-architectural-context",
    "7cs-system-context",
    "7cs-structural",
    "7cs-functional-A",
    "7cs-functional-B",
    "7cs-deployment",
    "7cs-com-transform",
    "7cs-spec-compose",
    "7cs-spec-audit",
    "7cs-backend-slice",
)


def validate(root=REPO_ROOT):
    for skill in SKILLS:
        path = Path(root) / ".agents" / "skills" / skill / "SKILL.md"
        if not path.is_file():
            raise RuntimeError("Skill ausente: {}".format(skill))
        with open(path, encoding="utf-8", newline=None) as handle:
            text = handle.read()
        pattern = r"\A---\nname:\s+{}\ndescription:\s+.+?\n---".format(re.escape(skill))
        if not re.search(pattern, text, re.DOTALL):
            raise RuntimeError("Frontmatter inválido: {}".format(skill))
    return len(SKILLS)


def main():
    try:
        count = validate()
    except RuntimeError as error:
        print(error, file=sys.stderr)
        return 1
    print("Skills valid: {}".format(count))
    return 0


if __name__ == "__main__":
    sys.exit(main())
