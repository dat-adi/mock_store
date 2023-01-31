default: ## Run the app
	. ./venv/bin/activate && python ./main.py

env: ## Install all the dependencies
	@-virtualenv venv
	. ./venv/bin/activate && pip install -r requirements.txt

freeze: ## Freeze python dependencies
	@. ./venv/bin/activate && pip freeze > requirements.txt

help: ## Print a help section for all the make commands
	@cat $(MAKEFILE_LIST) | grep -E '^[a-zA-Z_-]+:.*?## .*$$' | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

lint: ## Run the linter
	/usr/bin/python3 -m black ./*.py
	/usr/bin/python3 -m black ./**.py

test: ## Run tests
	@./venv/bin/pytest .

coverage: ## Make a coverage report
	@./venv/bin/pytest --cov .
