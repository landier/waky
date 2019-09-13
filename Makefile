.DEFAULT_GOAL := all
.PHONY : all install lint test

all: install run

install:
	pip3 install --user pipenv
	pipenv install

run:
	pipenv run python main.py
