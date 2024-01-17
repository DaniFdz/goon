# Run the server
run:
	poetry run python3 -m core.manage runserver

# Setup poetry
setup:
	poetry config virtualenvs.create true --local
	poetry config virtualenvs.in-project true --local

# Install dependencies
install: setup
	poetry install --no-root
	poetry run pre-commit install
	poetry run pip install django-admin-honeypot-updated-2021


# Update configuration files
update:
	poetry update

# Apply migrations to the database
migrations:
	poetry run python3 -m core.manage makemigrations
	poetry run python3 -m core.manage migrate

# Apply flake8 linter to python3 files
lint:
	poetry run pre-commit run --all-files

# Run server tests
test:
	poetry run pytest -v -rs -n 3 --show-capture=no

# Check the coverage of the tests
coverage:
	poetry run pytest -v -rs -n 3 --show-capture=no --cov --cov-report=term --cov-fail-under=100

# Check the coverage of the tests and export to html
coverage_html:
	poetry run pytest -v -rs -n 3 --show-capture=no --cov --cov-report=html:htmlcov --cov-report=term --cov-fail-under=100

# Run database development server
db_up:
	docker compose -f docker-compose.dev.yml up -d

# Stop database development server
db_down:
	docker compose -f docker-compose.dev.yml down
