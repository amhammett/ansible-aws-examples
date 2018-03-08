.PHONY: help test flake8 isort venv install

profile := dev
region := us-west-2

ifeq ($(OS),Windows_NT)
    python_path := $(shell where python)
    venv_pip_path := venv\Scripts\pip
else
    python_path := $(shell which python2.7)
    venv_ansible_path := AWS_PROFILE=$(profile) AWS_DEFAULT_REGION=$(region) ../venv/bin/ansible-playbook
    venv_pip_path := ../venv/bin/pip
endif

help: ## this help task
	@echo 'Available targets'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# ansible
playbook_vars := -e env=$(env)

# cache app
cache-app-deploy:
	$(venv_ansible_path) cache-app-deploy.yml $(playbook_vars)

cache-app-terminate:
	$(venv_ansible_path) cache-app-terminate.yml $(playbook_vars)

# db app
db-app-deploy:
	$(venv_ansible_path) db-app-deploy.yml $(playbook_vars)

db-app-terminate:
	$(venv_ansible_path) db-app-terminate.yml $(playbook_vars)

# web app - high availability
web-app-ha-deploy:
	$(venv_ansible_path) web-app-ha-deploy.yml $(playbook_vars)

web-app-ha-terminate:
	$(venv_ansible_path) web-app-ha-terminate.yml $(playbook_vars)

# web app - simple
web-app-simple-deploy:
	$(venv_ansible_path) web-app-simple-deploy.yml $(playbook_vars)

web-app-simple-terminate:
	$(venv_ansible_path) web-app-simple-terminate.yml $(playbook_vars)

# test
test: ## test all the things
	$(venv_ansible_path) --version

# inventory
list:
	AWS_PROFILE=$(profile) ./inventory/ec2.py --list
clear:
	AWS_PROFILE=$(profile) ./inventory/ec2.py --refresh-cache
