# Run the server
run:
	poetry run python3 -m core.manage runserver

# Apply migrations to the database
migrations:
	poetry run python3 -m core.manage makemigrations
	poetry run python3 -m core.manage migrate

# Apply flake8 linter to python3 files
lint:
	poetry run flake8

# Run server tests
test:
	poetry run python3 -m core.manage test

# Check the coverage of the tests
coverage:
	poetry run coverage run -m core.manage test
	poetry run coverage html
	poetry run coverage report

