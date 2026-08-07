#!/usr/bin/env python3
"""Auditoría determinista de cobertura de trazas para un delivery."""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from sevencs.audit import AuditFailed, ClarificationGateClosed, audit
from sevencs.paths import REPO_ROOT, repo_path


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--delivery-id", required=True)
    parser.add_argument("--com-directory", default="com")
    parser.add_argument("--mapping-directory", default="mapping")
    parser.add_argument("--clarification-directory", default="clarifications")
    parser.add_argument("--require-clarification-gate", action="store_true")
    parser.add_argument("--falsifiability-check", action="store_true")
    arguments = parser.parse_args(argv)

    try:
        result = audit(
            delivery_id=arguments.delivery_id,
            com_directory=repo_path(REPO_ROOT, arguments.com_directory),
            mapping_directory=repo_path(REPO_ROOT, arguments.mapping_directory),
            clarification_directory=repo_path(REPO_ROOT, arguments.clarification_directory),
            require_clarification_gate=arguments.require_clarification_gate,
            falsifiability_check=arguments.falsifiability_check,
        )
    except (AuditFailed, ClarificationGateClosed) as error:
        print("Audit {}: ERROR {}".format(arguments.delivery_id, error), file=sys.stderr)
        return 1

    print("Audit {}: {} C={}".format(
        arguments.delivery_id, "PASS" if result.passed else "FAIL", result.coverage
    ))
    if not result.passed and not arguments.falsifiability_check:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
