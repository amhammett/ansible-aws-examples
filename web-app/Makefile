.PHONY: help venv install test

profile := dev
region := us-west-2

ifeq ($(OS),Windows_NT)
    python_path := $(shell where python)
    venv_flake8_path := venv\Scripts\flake8
    venv_isort_path := venv\Scripts\isort
    venv_pip_path := venv\Scripts\pip
    venv_python_path := venv\Scripts\python
    virtualenv_path := python -m virtualenv
else
    python_path := $(shell which python2.7)
    venv_flake8_path := ./venv/bin/flake8
    venv_isort_path := ./venv/bin/isort
    venv_pip_path := ./venv/bin/pip
    venv_python_path := ./venv/bin/python
    virtualenv_path := virtualenv
endif

help: ## this help task
	@echo 'Available targets'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# environment
venv: ## virtual environment
	$(virtualenv_path) venv --python=$(python_path)

install: ## install all the things
	$(venv_pip_path) install -I pip
	$(venv_pip_path) install -r requirements.txt

# app
run: ## run the app
	$(venv_python_path) src/web.py

# test
test: | isort flake8 ## test all the things

flake8:
	$(venv_flake8_path) src/

isort:
	$(venv_isort_path) --quiet --check-only --recursive src
