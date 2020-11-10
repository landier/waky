all: one two three
.PHONY: all

dev-install:
	poetry install

dev: dev-install
	poetry run uvicorn waky.main:app --reload

prod-install:
	poetry install --no-dev

prod: prod-install
	poetry run gunicorn -w 2 -k uvicorn.workers.UvicornWorker --log-level warning waky.main:app --bind 0.0.0.0:8000
