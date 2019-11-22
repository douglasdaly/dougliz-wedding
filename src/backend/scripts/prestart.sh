#! /usr/bin/env sh

# Let the DB start
python -m app check db

# Run migrations
alembic upgrade head

# Create initial data in DB
python -m app init
