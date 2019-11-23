#!/usr/bin/env make -f

#
#	Configuration
#

-include .env

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

ifndef PYTHON
	PYTHON = python
endif

ifndef PKG_MGR
	PKG_MGR = pipenv
endif

ifndef NODE_MGR
	NODE_MGR = yarn
endif

ifndef PYTEST_CORES
	PYTEST_CORES = auto
endif

SUBDIR_ROOTS := docs src/backend
DIRS := . $(shell find $(SUBDIR_ROOTS) -type d)
GARBAGE_PATTERNS := *.pyc *~ *-checkpoint.ipynb *.egg-info __pycache__/
GARBAGE := $(foreach DIR,$(DIRS),$(addprefix $(DIR)/,$(GARBAGE_PATTERNS)))

ALEMBIC = alembic
FLAKE8 = flake8
PYTEST = pytest
UVICORN = uvicorn

ifeq ($(PKG_MGR), pipenv)
	RUN_PRE = pipenv run
	VENV_ACTIVATE := . $(shell pipenv --venv)/bin/activate
else
	RUN_PRE =
	VENV_ACTIVATE = source env/bin/activate
endif
VENV_DEACTIVATE = deactivate

ifeq ($(NODE_MGR), npm)
	RUN_NODE := $(NODE_MGR) run
else
	RUN_NODE := $(NODE_MGR)
endif

RUN_ALEMBIC := $(RUN_PRE) $(ALEMBIC)
RUN_FLAKE8 := $(RUN_PRE) $(FLAKE8)
RUN_PYTEST := $(RUN_PRE) $(PYTEST)
RUN_PYTHON := $(RUN_PRE) $(PYTHON)
RUN_UVICORN := $(RUN_PRE) $(UVICORN)


#
#	Recipes
#

.PHONY: help setup teardown \
		clean-python \
		test \
		coverage lint lint-backend lint-frontend \
		debug-backend debug-frontend

.DEFAULT-GOAL := help

help:
	@printf 'Usage: make \033[36m[target]\033[0m\n'
	@echo ''
	@echo 'Available targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'
	@echo ''

# - Environment

setup: .env ## Sets up the development environment.
	@echo '[INFO] Setting up environment...'

teardown: ## Tears down the development environment.
	@echo '[INFO] Tearing down environment...'

.env:
	cp sample.env .env

# - Cleaning

clean-python:
	@rm -rf $(GARBAGE)

# - Unit testing

test: ## Runs the unit tests over the codebase.
	$(RUN_PYTEST) -n $(PYTEST_CORES)

# - Code coverage/linting

coverage: ## Runs code coverage checks.
	$(RUN_PYTEST) --cov=src/ -n $(PYTEST_CORES)

lint: lint-backend lint-frontend ## Runs all code linting.

lint-backend:
	@echo '[INFO] Linting backend code...'
	$(RUN_FLAKE8)

lint-frontend:
	@echo '[INFO] Linting frontend code...'
	cd ./src/frontend && $(RUN_PRE) $(RUN_NODE) lint

cloc: ## Code line counts
	@cloc ./docker ./scripts ./src --exclude-dir=__pycache__,.nuxt,dist,node_modules

# - Debug server

debug-backend:
	@( \
		$(VENV_ACTIVATE); \
		export PYTHONPATH=./src/backend; \
		cd ./src/backend; \
		$(UVICORN) app.main:app --debug --reload --port=$(SERVER_PORT); \
		$(VENV_DEACTIVATE); \
	)

debug-frontend:
	cd ./src/frontend && $(RUN_PRE) $(RUN_NODE) dev

# - Alembic

alembic-upgrade:
	cd ./src/backend && $(RUN_ALEMBIC) upgrade head

alembic-revise:
	cd ./src/backend && $(RUN_ALEMBIC) revision

# - Docker

docker-build: ## Build docker containers (deployment)
	./scripts/build.sh

docker-local: ## Start docker containers on local machine (develop)
	./scripts/start-local.sh

docker-stop: ## Stop docker containers (from docker-stack.yml)
	docker-compose -f docker-stack.yml down -v --remove-orphans
