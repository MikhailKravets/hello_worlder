# Hello Worlder

This is the naive project to demonstrate the power of programming to students.

## Installation

Install libraries from `requirements.txt`

```shell
pip install -r requirements.txt
```

Run `docker-compose-dev.yml` file with docker-compose.

```shell
docker-compose -f docker-compose-dev.yml up
```

Run `main.py` script

```shell
python main.py
```

## Run tests

We use pytest (with coverage plugin) to run tests. Use this command to run tests

```shell
pytest tests --cov=. --cov-branch
```

as an output you should see

```shell
Name                     Stmts   Miss Branch BrPart  Cover   Missing
--------------------------------------------------------------------
tests/conftest.py            8      0      0      0   100%
tests/test_storages.py      22      0      0      0   100%
tests/test_worlder.py       11      0      0      0   100%
worlder/__init__.py          5      0      2      0   100%
worlder/storages.py         16      0      4      0   100%
worlder/utils.py             2      0      0      0   100%
--------------------------------------------------------------------
TOTAL                       64      0      6      0   100%
```