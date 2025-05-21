dev:
	python3 manage.py runserver

install:
	uv sync

migrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

shell:
	python3 manage.py shell

render-start:
	gunicorn task_manager.wsgi:application

start:
	uv run gunicorn -w 5 -b 127.0.0.1:8000 task_manager.wsgi:application

build:
	./build.sh

upgrade:
	uv sync --upgrade

lint:
	uv run ruff check

lintfix:
	uv run ruff check --fix

test:
	python3 manage.py test

test-coverage:
	uv run coverage run manage.py test task_manager
	uv run coverage xml
	uv run coverage report
