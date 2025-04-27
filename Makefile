PORT ?= 8000

dev:
	python3 manage.py runserver

install:
	uv sync

devg:
	uv run gunicorn -w 5 -b 127.0.0.1:5000 page_analyzer:app

start:
	uv run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

upgrade:
	uv sync --upgrade

lint:
	uv run ruff check

lintfix:
	uv run ruff check --fix


test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

tests:
	uv run pytest -vv
