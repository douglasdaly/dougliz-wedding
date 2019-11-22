#! /usr/bin/env sh

# Exit in case of error
set -e

DOMAIN=backend \
docker-compose \
    -f docker/docker-compose.shared.base-images.yml \
    -f docker/docker-compose.shared.env.yml \
    -f docker/docker-compose.shared.depends.yml \
    -f docker/docker-compose.deploy.build.yml \
    -f docker/docker-compose.test.yml \
    config > docker-stack.yml

docker-compose -f docker-stack.yml build
docker-compose -f docker-stack.yml down -v --remove-orphans # Remove possibly previous broken stacks left hanging after an error
docker-compose -f docker-stack.yml up -d
docker-compose -f docker-stack.yml exec -T backend-tests /app/scripts/tests-start.sh
docker-compose -f docker-stack.yml down -v --remove-orphans
