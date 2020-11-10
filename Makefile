all: one two three
.PHONY: all

venv:
	poetry install

local: venv
	poetry run uvicorn waky.main:app --reload
