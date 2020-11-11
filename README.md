![GitHub Workflow Status](https://img.shields.io/github/workflow/status/landier/waky/CI?style=for-the-badge)

# waky
_Waky is a web application to manage Wake-On-Lan supporting devices._

## Requirements
* make
* [poetry](https://python-poetry.org/)
* [pre-commit](https://pre-commit.com/)
* Python 3.8

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
