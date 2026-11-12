# Copilot instructions for this repository

## Project context

This repository is a learning project for the Ohtu course. The active application in this workspace is the Flask login app under `viikko3/login`.

The app is intentionally small and layered:
- `src/app.py` defines Flask routes and request handling.
- `src/services/user_service.py` contains the business logic: input validation, credential checks, and user creation.
- `src/repositories/user_repository.py` stores users in memory (`_users`) and exposes the singleton `user_repository`.
- `src/entities/user.py` is the plain data object for a `User`.
- `src/AppLibrary.py` is a test helper for Robot Framework Browser tests.
- `src/tests/*.robot` exercises the app through browser automation against the local server.

The app uses an in-memory repository, not a database. There is a reset endpoint at `/tests/reset` used by the test suite to clear state between scenarios.

## Setup and commands

Run everything from the project directory:

```bash
cd viikko3/login
```

Install project dependencies (uses `uv` metadata from `pyproject.toml`):

```bash
uv sync --group dev
```

Start the Flask app:

```bash
uv run python src/index.py
```

The app listens on `http://localhost:5001`.

The app must be running when performing the tests.

Run the full browser test suite:

```bash
uv run robot src/tests
```

Run a single Robot test module:

```bash
uv run robot src/tests/login.robot
```

Run one specific test case:

```bash
uv run robot --test "Login With Correct Credentials" src/tests/login.robot
```

There is no dedicated lint command in this project; the repository relies on the Python/Robot test setup rather than a separate static-analysis tool.

## Architecture notes that matter

- The app is a Flask server with route methods named in pairs such as `render_login` / `handle_login` and `render_register` / `handle_register`.
- User validation and authentication rules live in `UserService`, not in the route layer; routes only fetch form values and turn exceptions into flashed errors.
- The repository layer is operation-specific: `find_by_username`, `create`, `delete`, and `delete_all` are the main methods used by the app.
- The tests are not unit tests; they are end-to-end browser tests using Robot Framework Browser. They rely on the Flask server being running and on the app reset endpoint clearing shared state.
- The `Test Setup` blocks in the Robot suites call `Reset Application` and then create the default `kalle` user before each scenario. This pattern is important when working on or debugging the app because the state is intentionally in-memory and shared across requests.

## Key conventions in this codebase

- Keep the app state in memory only; no persistence layer is expected.
- Use the existing error types and messages rather than introducing new validation flows in the route layer. `UserInputError` and `AuthenticationError` are the contract used by the UI.
- When adding new routes or business logic, follow the existing split:
  - route logic in `src/app.py`
  - validation/business behavior in `src/services/user_service.py`
  - data access in `src/repositories/user_repository.py`
- Robot tests use `resource.robot` to centralize browser setup and shared keywords. When adding scenarios, follow the same `Suite Setup` / `Suite Teardown` / `Test Setup` layout and reuse helper keywords instead of duplicating browser flow logic.
- The project uses `requests` in `src/AppLibrary.py` to hit the app’s HTTP endpoints, so new test helpers should stay consistent with that pattern.
- `src/index.py` is the dev entry point and intentionally runs the server on port `5001` with debug mode enabled; do not change the port unless the tests and helpers are updated together.

## Working with this repo

When making changes, keep the app's existing flow in mind:
1. Validate input (username & password) in `UserService`.
2. Persist or fetch via `user_repository`.
3. Return a flashed error or redirect in the route.
4. If you change validation logic, update the corresponding Robot tests in `src/tests`.

When debugging a failing flow, check the server route and the corresponding Robot scenario together; the browser tests are the living specification for user-facing behavior.
