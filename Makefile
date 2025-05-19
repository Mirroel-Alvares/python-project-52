dev:
	python3 manage.py runserver

install:
	uv sync

migrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

collectstatic:
	python manage.py collectstatic --noinput

shell:
	python3 manage.py shell

render-start:
	gunicorn task_manager.wsgi

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
	uv run coverage html
	uv run coverage report
