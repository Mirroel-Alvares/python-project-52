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



devg:
	uv run gunicorn -w 5 -b 127.0.0.1:5000 page_analyzer:app

start:
	uv run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

upgrade:
	uv sync --upgrade

lint:
	uv run ruff check

lintfix:
	uv run ruff check --fix


test:
	python3 manage.py test

test-coverage:
	uv run pytest --cov=task_manager --cov-report xml

	coverage run --source='.' -m pytest tests/
	coverage xml

tests:
	uv run pytest -vv
