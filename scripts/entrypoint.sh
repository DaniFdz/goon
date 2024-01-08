#!/usr/bin/env bash

set -e

RUN_MANAGE_PY="poetry run python -m core.manage"

echo "Collecting static files..."
$RUN_MANAGE_PY collectstatic --no-input

find /opt/project/media -type d -exec chmod 755 {} \;
find /opt/project/media -type f -exec chmod 644 {} \;
find /opt/project/static -type d -exec chmod 755 {} \;
find /opt/project/static -type f -exec chmod 644 {} \;

echo "Running migrations..."
$RUN_MANAGE_PY migrate --no-input

exec poetry run daphne core.project.asgi:application -p 8000 -b 0.0.0.0
