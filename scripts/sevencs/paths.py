"""Resolución de rutas del repositorio, independiente del separador del sistema operativo."""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


class PathOutsideRepo(ValueError):
    pass


def repo_path(root, path):
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    return Path(root) / candidate


def resolve_pdf(root, pdf_path):
    root = Path(root).resolve()
    resources = root / "resources"
    pdf = repo_path(root, pdf_path).resolve()
    if resources not in pdf.parents:
        raise PathOutsideRepo("El PDF debe estar dentro de resources/: {}".format(pdf))
    if not pdf.is_file():
        raise FileNotFoundError("PDF no encontrado: {}".format(pdf))
    return pdf


def sole_pdf(root):
    pdfs = sorted((Path(root) / "resources").glob("*.pdf"))
    if not pdfs:
        raise FileNotFoundError("No hay ningún PDF en resources/.")
    if len(pdfs) > 1:
        raise ValueError(
            "Hay más de un PDF en resources/. Indica uno con: "
            "--pdf-path resources/archivo.pdf"
        )
    return pdfs[0]
