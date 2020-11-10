# waky

## Requisites
* make
* [poetry](https://python-poetry.org/)
* [pre-commit](https://pre-commit.com/)

## Quickstart
```bash
poetry install
poetry run uvicorn waky.main:app --reload
```

or

```bash
make local
```

## Links
* http://localhost:8000/
* http://localhost:8000/docs

## Dev
```bash
cd waky
pre-commit install
poetry install
```
