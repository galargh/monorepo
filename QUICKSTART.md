# Quick Start Guide

Get up and running with the Python monorepo in minutes!

## 1. Enter Development Environment

### Option A: Using Nix (Recommended)

```bash
nix develop
```

This will give you all the tools you need: Python 3.11, UV, pytest, ruff, mypy, etc.

### Option B: Using direnv (Automatic)

If you have direnv installed:

```bash
direnv allow
```

The environment will automatically load whenever you enter the directory.

## 2. Install Dependencies

```bash
uv sync
uv pip install -e packages/python/shared-utils -e services/python/api-service
```

This installs all dev dependencies and workspace packages in editable mode.

## 3. Verify Installation

Run the tests to make sure everything works:

```bash
uv run pytest
```

You should see all tests passing! ✅

## 4. Try the Example Service

Start the API service:

```bash
uv run uvicorn api_service.main:app --reload
```

Or using the Makefile:

```bash
make api-service
```

Open your browser to:
- http://localhost:8000/docs - Interactive API documentation
- http://localhost:8000/text/capitalize?text=hello%20world - Try an endpoint

## 5. Make Some Changes

### Edit the shared library

1. Open `packages/python/shared-utils/shared_utils/text.py`
2. Add a new function
3. Add tests in `packages/python/shared-utils/tests/test_text.py`
4. Run tests: `uv run pytest packages/python/shared-utils/tests`

### Use it in the service

1. Import your new function in `services/python/api-service/api_service/main.py`
2. Create a new endpoint
3. Test it with `uv run pytest services/python/api-service/tests`

## 6. Code Quality Checks

Before committing, run:

```bash
# Check everything
make check

# Or individually:
make lint          # Check code style
make format        # Format code
make type-check    # Check types
make test          # Run tests
```

## Common Commands

```bash
# Using UV directly
uv sync                        # Install/update dependencies
uv run pytest                  # Run tests
uv run pytest --cov            # Run tests with coverage
uv run ruff check .            # Lint
uv run ruff format .           # Format
uv run mypy packages/ services/ # Type check

# Using Make
make help          # Show all available commands
make install       # Install dependencies
make test          # Run tests
make test-cov      # Run tests with coverage
make lint          # Lint code
make format        # Format code
make type-check    # Type check
make check         # Run all checks
make clean         # Clean cache files
```

## Next Steps

1. Read the [README.md](README.md) for detailed documentation
2. Explore the example package: [packages/python/shared-utils](packages/python/shared-utils/README.md)
3. Explore the example service: [services/python/api-service](services/python/api-service/README.md)
4. Create your own packages and services!

## Troubleshooting

**Problem**: `uv: command not found`
**Solution**: Make sure you're in the Nix shell: `nix develop`

**Problem**: Import errors when running tests
**Solution**: Run `uv sync` and install workspace packages:
```bash
uv sync
uv pip install -e packages/python/shared-utils -e services/python/api-service
```

**Problem**: Tests not discovered
**Solution**: Test files must start with `test_` or end with `_test.py`

**Problem**: Type checking fails
**Solution**: Add type hints to your functions and variables

Need more help? Check the [README.md](README.md) or open an issue!
