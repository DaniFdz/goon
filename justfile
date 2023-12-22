# Run the server
run:
	poetry run python3 manage.py runserver

# Apply migrations to the database
migrations:
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate

# Apply flake8 linter to python3 files
lint:
	poetry run flake8

# Run server tests
test:
	poetry run python3 manage.py test

# Check the coverage of the tests
coverage:
	poetry run coverage run manage.py test
	poetry run coverage html
	poetry run coverage report

