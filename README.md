# Python Monorepo

A modern Python monorepo setup using UV workspace and Nix for reproducible development environments.

## 🏗️ Structure

```
.
├── packages/python/          # Shared libraries
│   └── shared-utils/         # Example shared utilities package
│       ├── shared_utils/     # Source code
│       ├── tests/            # Package tests
│       └── pyproject.toml    # Package configuration
│
├── services/python/          # Services
│   └── api-service/          # Example API service
│       ├── api_service/      # Source code
│       ├── tests/            # Service tests
│       └── pyproject.toml    # Service configuration
│
├── pyproject.toml            # Workspace configuration
├── flake.nix                 # Nix development environment
└── .envrc                    # direnv configuration
```

## 🚀 Getting Started

### Prerequisites

- [Nix](https://nixos.org/download.html) with flakes enabled
- [direnv](https://direnv.net/) (optional, for automatic environment loading)

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd monorepo
   ```

2. **Enter the Nix development shell:**
   ```bash
   nix develop
   ```

   Or if you have direnv installed:
   ```bash
   direnv allow
   ```

3. **Install dependencies:**
   ```bash
   uv sync
   uv pip install -e packages/python/shared-utils -e services/python/api-service
   ```

## 📦 Workspace Management

This monorepo uses UV's workspace feature to manage multiple packages and services.

### Adding a New Package

1. Create a new directory under `packages/python/`:
   ```bash
   mkdir -p packages/python/my-package/my_package
   mkdir -p packages/python/my-package/tests
   ```

2. Create `pyproject.toml`:
   ```toml
   [project]
   name = "my-package"
   version = "0.1.0"
   requires-python = ">=3.11"
   dependencies = []

   [build-system]
   requires = ["hatchling"]
   build-backend = "hatchling.build"
   ```

3. Install the new package:
   ```bash
   uv pip install -e packages/python/my-package
   ```

### Adding a New Service

1. Create a new directory under `services/python/`:
   ```bash
   mkdir -p services/python/my-service/my_service
   mkdir -p services/python/my-service/tests
   ```

2. Create `pyproject.toml` with dependencies (including workspace packages):
   ```toml
   [project]
   name = "my-service"
   version = "0.1.0"
   requires-python = ">=3.11"
   dependencies = [
       "shared-utils",  # Reference workspace package
   ]

   [tool.uv.sources]
   shared-utils = { workspace = true }

   [build-system]
   requires = ["hatchling"]
   build-backend = "hatchling.build"
   ```

3. Install dependencies and the new service:
   ```bash
   uv sync
   uv pip install -e services/python/my-service
   ```

## 🧪 Testing

Run all tests:
```bash
uv run pytest
```

Run tests for a specific package:
```bash
uv run pytest packages/python/shared-utils/tests
```

Run tests for a specific service:
```bash
uv run pytest services/python/api-service/tests
```

Run tests with coverage:
```bash
uv run pytest --cov=packages --cov=services --cov-report=html
```

## 🔍 Code Quality

### Linting

Check code with Ruff:
```bash
uv run ruff check .
```

Auto-fix issues:
```bash
uv run ruff check --fix .
```

### Formatting

Format code:
```bash
uv run ruff format .
```

Check formatting:
```bash
uv run ruff format --check .
```

### Type Checking

Run mypy:
```bash
uv run mypy packages/ services/
```

## 🏃 Running Services

### API Service

Start the API service:
```bash
uv run uvicorn api_service.main:app --reload
```

The API will be available at:
- Application: http://localhost:8000
- Interactive docs: http://localhost:8000/docs
- OpenAPI schema: http://localhost:8000/openapi.json

## 🛠️ Development Tools

The Nix flake provides the following tools:

- **Python 3.11**: Programming language
- **UV**: Fast Python package manager
- **pytest**: Testing framework
- **ruff**: Linting and formatting
- **mypy**: Static type checking
- **git**: Version control
- **direnv**: Automatic environment loading

## 📚 Example Packages

### shared-utils

A utility library demonstrating:
- Text manipulation functions
- Math operations
- Comprehensive test coverage
- Type hints

See [packages/python/shared-utils/README.md](packages/python/shared-utils/README.md) for details.

### api-service

A FastAPI service demonstrating:
- REST API endpoints
- Using shared workspace packages
- API testing with TestClient
- Modern async Python

See [services/python/api-service/README.md](services/python/api-service/README.md) for details.

## 🔄 Workflow

1. **Make changes** to packages or services
2. **Run tests**: `uv run pytest`
3. **Check linting**: `uv run ruff check .`
4. **Format code**: `uv run ruff format .`
5. **Type check**: `uv run mypy .`
6. **Commit** your changes

## 🤝 Contributing

1. Create a new branch for your feature
2. Make your changes with appropriate tests
3. Ensure all tests pass and code is formatted
4. Submit a pull request

## 📝 Configuration Files

- **`pyproject.toml`**: Root workspace configuration, shared dependencies, and tool settings
- **`flake.nix`**: Nix development environment with all tools
- **`.envrc`**: direnv configuration for automatic environment loading
- **`.gitignore`**: Git ignore patterns for Python and Nix

## 🎯 Best Practices

1. **Keep packages focused**: Each package should have a single, clear purpose
2. **Write tests**: All code should have corresponding tests
3. **Type hints**: Use type hints for better code quality and IDE support
4. **Documentation**: Document public APIs and complex logic
5. **Dependencies**: Only add necessary dependencies, prefer workspace packages over external ones

## 🐛 Troubleshooting

### UV not found
Make sure you're in the Nix shell: `nix develop`

### Import errors
Run `uv sync` and then install workspace packages:
```bash
uv sync
uv pip install -e packages/python/shared-utils -e services/python/api-service
```

### Tests not found
Ensure your test files follow the naming convention: `test_*.py` or `*_test.py`

### Virtual environment issues
Remove and recreate: `rm -rf .venv && uv venv && uv sync`

## 📄 License

[Your License Here]
