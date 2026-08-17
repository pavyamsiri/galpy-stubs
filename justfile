set shell := ["bash", "-cu"]

stubs := "galpy-stubs"
typing_tests := "tests/typing"
sources := stubs + " " + typing_tests
python := ".venv/bin/python"

default: check

check: format-check lint basedpyright basedmypy ty pyrefly

ready:
    just format
    just check

format:
    .venv/bin/ruff format {{sources}}

format-check:
    .venv/bin/ruff format --check {{sources}}

lint:
    .venv/bin/ruff check scripts tests

# Recreate the generated baseline with the installed runtime version.
skeleton:
    {{python}} scripts/generate_skeleton.py

basedpyright:
    .venv/bin/basedpyright {{stubs}} {{typing_tests}}

basedmypy:
    .venv/bin/mypy --no-incremental --no-strict --strict --disable-error-code=explicit-any --disable-error-code=misc --disable-error-code=explicit-override --disable-error-code=override --disable-error-code=type-arg --disable-error-code=import-untyped --disable-error-code=subclass-any --disable-error-code=no-any-unimported --disable-error-code=attr-defined --python-executable {{python}} --python-version 3.13 {{stubs}} {{typing_tests}}

ty:
    .venv/bin/ty check --python .venv --extra-search-path . {{stubs}}

pyrefly:
    .venv/bin/pyrefly check --python-interpreter-path {{python}} --search-path . --summary=none --progress-bar no {{stubs}}

sync:
    uv sync --dev

build:
    uv build
