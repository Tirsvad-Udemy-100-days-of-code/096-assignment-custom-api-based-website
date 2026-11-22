#!/bin/bash
# Take the lecture-step screenshots inside Docker containers, so the host
# desktop is never used. Needs Docker with Linux containers.
# Usage: bash tests/e2e/capture.sh
set -euo pipefail
cd "$(dirname "$0")/../.."
NET=hp-shots
PLAYWRIGHT_IMAGE=${PLAYWRIGHT_IMAGE:-mcr.microsoft.com/playwright/python:v1.55.0-noble}
PY_IMAGE=python:3.14-slim
cleanup() {
  docker rm -f hp-online hp-offline >/dev/null 2>&1 || true
  docker network rm "$NET" >/dev/null 2>&1 || true
}
trap cleanup EXIT
cleanup
docker network create "$NET" >/dev/null
for pair in "hp-online:hp_site.presentation.app:create_app" \
            "hp-offline:offline_app:create_offline_app"; do
  name=${pair%%:*}; factory=${pair#*:}; module=${factory%%:*}
  docker run -d --name "$name" --network "$NET" -v "$PWD:/app:ro" -w /app \
    -e PYTHONPATH=/app/src:/app/tests/e2e "$PY_IMAGE" sh -c \
    "pip install -q flask && flask --app '${module}:${factory##*:}' run --host 0.0.0.0 --port 5000" >/dev/null
done
for name in hp-online hp-offline; do
  for _ in $(seq 1 60); do
    docker logs "$name" 2>&1 | grep -q "Running on" && break
    sleep 2
  done
  docker logs "$name" 2>&1 | grep -q "Running on" || { docker logs "$name"; exit 1; }
done
docker run --rm --network "$NET" -v "$PWD/tests/e2e:/e2e:ro" -v "$PWD/docs/images:/out" \
  "$PLAYWRIGHT_IMAGE" python /e2e/capture.py /out
