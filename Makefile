all: one two three
.PHONY: all

dev-install:
	poetry install

dev: dev-install
	poetry run uvicorn waky.main:app --reload

prod-install:
	poetry install --no-dev

prod: prod-install
	poetry run uvicorn waky.main:app --host 0.0.0.0 --port 8000
