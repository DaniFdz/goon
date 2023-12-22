run:
	poetry run python3 manage.py runserver

migrations:
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate

test:
	poetry run python3 manage.py test

coverage:
	poetry run coverage run manage.py test
	poetry run coverage html
	poetry run coverage report
	

