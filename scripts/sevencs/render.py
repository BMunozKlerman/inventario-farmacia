"""Renderizado local del PDF a PNG mediante Poppler (pdftoppm) del sistema."""

import hashlib
import json
import platform
import shutil
import subprocess
from pathlib import Path

INSTALL_HINTS = {
    "Darwin": "brew install poppler",
    "Linux": "sudo apt install poppler-utils   (o el equivalente de tu distribución)",
    "Windows": "choco install poppler   (o scoop install poppler)",
}


class RendererNotAvailable(RuntimeError):
    pass


def find_renderer():
    renderer = shutil.which("pdftoppm")
    if not renderer:
        hint = INSTALL_HINTS.get(platform.system(), "instala poppler-utils")
        raise RendererNotAvailable(
            "Poppler no está disponible: falta pdftoppm en el PATH. Instálalo con: {}".format(hint)
        )
    return renderer


def render_pages(pdf, evidence_directory, delivery_id, dpi=180, root=None):
    renderer = find_renderer()
    evidence = Path(evidence_directory)
    evidence.mkdir(parents=True, exist_ok=True)
    prefix = evidence / "{}-page".format(delivery_id)

    completed = subprocess.run(
        [renderer, "-png", "-r", str(dpi), str(pdf), str(prefix)]
    )
    if completed.returncode != 0:
        raise RuntimeError("pdftoppm falló: {}".format(completed.returncode))

    rendered = sorted(evidence.glob("{}-page-*.png".format(delivery_id)))
    if not rendered:
        raise RuntimeError("No se generaron imágenes desde el PDF")

    pages = []
    for number, source in enumerate(rendered, start=1):
        target = evidence / "{}-p{:02d}.png".format(delivery_id, number)
        source.replace(target)
        pages.append({"page": number, "evidence": _relative(target, root), "status": "pending"})
    return pages


def _relative(path, root):
    if root is None:
        return path.name
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.name


def write_page_index(pdf, evidence_directory, delivery_id, pages):
    index = {
        "delivery_id": delivery_id,
        "source": "resources/{}".format(Path(pdf).name),
        "source_sha256": sha256(pdf),
        "pages": pages,
    }
    path = Path(evidence_directory) / "{}-page-index.json".format(delivery_id)
    path.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()
