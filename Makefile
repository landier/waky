.DEFAULT_GOAL := all
.PHONY : all install lint test build upload clean

all: install run

install:
	pip3 install --user pipenv
	pipenv install --dev

run:
	pipenv run python main.py

build:
	pipenv run python setup.py sdist bdist_wheel

upload: build
	pipenv run python -m twine upload dist/*

clean:
	rm -rf dist/* build/*
