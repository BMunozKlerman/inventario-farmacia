"""Inyección de skills en el prompt.

Cada agente descubre sus skills en un directorio propio (`.agents/`, `.claude/`, …).
Para no depender de ese mecanismo, el pipeline lee las skills del repositorio y las
incluye literalmente en el prompt.
"""

import re
from pathlib import Path

FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)
HEADER = (
    "Aplica las skills 7Cs incluidas literalmente a continuación. Son la definición "
    "autoritativa de la tarea: no busques archivos de skill en el entorno ni asumas que "
    "están registradas como herramientas.\n"
)


class SkillNotFound(FileNotFoundError):
    pass


def load_skill(skills_root, name):
    directory = Path(skills_root) / name
    skill = directory / "SKILL.md"
    if not skill.is_file():
        raise SkillNotFound("Skill ausente: {}".format(skill))

    parts = [FRONTMATTER.sub("", skill.read_text(encoding="utf-8")).strip()]
    for reference in sorted((directory / "references").glob("*.md")):
        parts.append("----- referencia: {} -----\n{}".format(
            reference.name, reference.read_text(encoding="utf-8").strip()
        ))
    return "\n\n".join(parts)


def inline_skills(skills_root, names):
    blocks = [
        "===== SKILL: {} =====\n{}".format(name, load_skill(skills_root, name))
        for name in names
    ]
    return HEADER + "\n\n" + "\n\n".join(blocks) + "\n\n===== FIN DE LAS SKILLS =====\n"
