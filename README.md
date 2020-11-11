![GitHub Workflow Status](https://img.shields.io/github/workflow/status/landier/waky/CI?style=flat-square)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/landier/waky?style=flat-square)
![LGTM Grade](https://img.shields.io/lgtm/grade/python/github/landier/waky?style=flat-square)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/landier/waky?style=flat-square)
![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/landier/waky?style=flat-square)
![PyPI](https://img.shields.io/pypi/v/waky?style=flat-square)


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
