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
	poetry run python3 -m core.manage test

# Check the coverage of the tests
coverage:
	poetry run coverage run -m core.manage test
	poetry run coverage html
	poetry run coverage report

# Run database development server
db_up:
	docker compose -f docker-compose.dev.yml up -d

# Stop database development server
db_down:
	docker compose -f docker-compose.dev.yml down
