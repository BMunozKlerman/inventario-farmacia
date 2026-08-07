#!/usr/bin/env python3
"""Punto de entrada: detecta el PDF en resources/ y ejecuta el pipeline completo."""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import run_pipeline
from sevencs.agent import AgentNotAvailable
from sevencs.audit import AuditFailed, ClarificationGateClosed
from sevencs.paths import REPO_ROOT, PathOutsideRepo, sole_pdf


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf-path")
    parser.add_argument("--delivery-id", default="E1")
    parser.add_argument("--com-only", action="store_true")
    arguments = parser.parse_args(argv)

    pdf_path = arguments.pdf_path or sole_pdf(REPO_ROOT)
    pipeline_argv = ["--pdf-path", str(pdf_path), "--delivery-id", arguments.delivery_id]
    if arguments.com_only:
        pipeline_argv.append("--com-only")
    return run_pipeline.main(pipeline_argv)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (AgentNotAvailable, AuditFailed, ClarificationGateClosed, PathOutsideRepo,
            FileNotFoundError, RuntimeError, ValueError) as error:
        print("Error: {}".format(error), file=sys.stderr)
        sys.exit(1)
