# Copilot instructions for the tdd-ostoskori project

## Project context

This project is a small TDD shopping-cart exercise in `viikko4/tdd-ostoskori`.

- `src/tuote.py`: product data and its name/price accessors
- `src/ostos.py`: one product plus quantity, including quantity changes and line totals
- `src/ostoskori.py`: shopping-cart API under implementation
- `src/tests/`: pytest/unittest-style tests

## Setup and test commands

Run everything for `viikko4/tdd-ostoskori` from that exercise directory:

```bash
cd viikko4/tdd-ostoskori
```

Run Python and tests only through `uv` or the exercise virtual environment. Do not use an uncontrolled global Python or pytest installation.

Using `uv`:

```bash
uv sync --group dev
uv run pytest
```

Tests must be executed with `uv run pytest`.

Run one test module:

```bash
uv run pytest src/tests/ostoskori_test.py
```

Run one test case:

```bash
uv run pytest src/tests/ostoskori_test.py::TestOstoskori::test_ostoskorin_hinta_ja_tavaroiden_maara_alussa
```

Using an existing virtual environment:

```bash
# Linux/macOS/WSL
source .venv/bin/activate
# Windows
.venv\Scripts\activate

python -m pytest
python -m pytest src/tests/ostoskori_test.py
python -m pytest src/tests/ostoskori_test.py::TestOstoskori::test_ostoskorin_hinta_ja_tavaroiden_maara_alussa
```

The project defines pytest in `pyproject.toml` as a development dependency. There is no dedicated lint command.

## Shopping-cart architecture

- `Ostos` wraps a `Tuote` and owns quantity behavior. It supplies the product name and calculates quantity times unit price.
- `Ostoskori` is the collection-level API and currently contains TDD starter stubs.
- Source modules use direct sibling imports such as `from tuote import Tuote`, so pytest must be run with the exercise's `src` import layout available; keep imports consistent with the existing module style.
- Tests create a fresh `Ostoskori` in `setUp` and assert both aggregate totals and cart contents.

## Key conventions

- The user writes tests for each functionality; do not edit tests unless explicitly asked.
- Implement one functionality at a time to make the current test pass, following TDD principles.
- Before implementation, run the relevant test to confirm it fails; after implementation, run it with `uv run pytest` and verify it passes before moving to the next test.
- Do not change the code in `src/ostos.py` or `src/tuote.py`.
- Implement absolutely minimal code that makes the tests pass.
- Implement methods in `Ostoskori` through the existing API; do not rename or replace it while completing kata tests.
- Keep quantity behavior consistent with `Ostos.muuta_lukumaaraa`: quantities cannot be negative.
- Preserve the Finnish domain names and methods used throughout the exercise (`tavaroita_korissa`, `hinta`, `lisaa_tuote`, `poista_tuote`, `tyhjenna`, `ostokset`).
