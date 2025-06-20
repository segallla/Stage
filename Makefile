.PHONY: etl test lint

etl:
python -m etl.fetch_sce_ica

lint:
ruff backend
black --check backend
mypy --strict backend

test:
pytest -q
