# Contributing to Python Monorepo

## Development Workflow

1. **Fork and clone** the repository
2. **Set up the development environment** using Nix:
   ```bash
   nix develop
   # or with direnv
   direnv allow
   ```
3. **Install dependencies**:
   ```bash
   make install
   ```
4. **Make your changes** with appropriate tests
5. **Run all checks** before committing:
   ```bash
   make check
   ```
6. **Commit and push** your changes
7. **Open a pull request**

## CI/CD

All pull requests and commits to the main branch run through our CI pipeline:

### Checks Run in CI

1. **Linting** - Ensures code follows style guidelines (Ruff)
2. **Format Check** - Verifies code is properly formatted (Ruff)
3. **Type Check** - Static type analysis (mypy)
4. **Tests** - Full test suite across Python 3.11, 3.12, and 3.13

### Running Checks Locally

You can run the same checks locally using Make commands:

```bash
# Run all checks (same as CI)
make check

# Run individual checks
make lint
make format-check
make type-check
make test
make test-cov  # with coverage report
```

## Code Quality Standards

- All code must pass linting and formatting checks
- Type hints are required for all functions
- All new features must include tests
- Maintain test coverage above 80%

## Pull Request Process

1. Ensure all CI checks pass
2. Update documentation if needed
3. Add tests for new features
4. Keep changes focused and atomic
5. Write clear commit messages

## Questions?

If you have questions about the contribution process, feel free to open an issue.

