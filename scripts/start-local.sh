#! /usr/bin/env sh

# Exit in case of error
set -e

docker-compose \
    -f docker/docker-compose.shared.admin.yml \
    -f docker/docker-compose.shared.base-images.yml \
    -f docker/docker-compose.shared.depends.yml \
    -f docker/docker-compose.shared.env.yml \
    -f docker/docker-compose.dev.build.yml \
    -f docker/docker-compose.dev.env.yml \
    -f docker/docker-compose.dev.labels.yml \
    -f docker/docker-compose.dev.networks.yml \
    -f docker/docker-compose.dev.ports.yml \
    -f docker/docker-compose.dev.volumes.yml \
    -f docker/docker-compose.dev.command.yml \
    config > docker-stack.yml

docker-compose -f docker-stack.yml build
docker-compose -f docker-stack.yml down -v --remove-orphans  # Remove possibly previous broken stacks left hanging after an error
docker-compose -f docker-stack.yml up -d
