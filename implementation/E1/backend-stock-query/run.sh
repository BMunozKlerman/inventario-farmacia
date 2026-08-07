#!/usr/bin/env bash
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
docker build -t e1-backend-stock-query "$here"
[ "${1:-}" = "--build-only" ] && exit 0
docker run --rm -p 8080:8080 -e POS_API_KEY=local-demo-key e1-backend-stock-query
