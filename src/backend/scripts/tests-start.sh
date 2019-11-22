#! /usr/bin/env sh
set -e

python -m app check db
python -m app check api

pytest $* /app/app/tests/
