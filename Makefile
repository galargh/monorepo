.PHONY: help install test lint format type-check clean dev

help: ## Show this help message
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install all dependencies
	uv sync

test: ## Run all tests
	uv run pytest

test-cov: ## Run tests with coverage
	uv run pytest --cov=packages --cov=services --cov-report=xml --cov-report=html --cov-report=term --junitxml=junit.xml

lint: ## Run linter
	uv run ruff check .

lint-fix: ## Run linter with auto-fix
	uv run ruff check --fix .

format: ## Format code
	uv run ruff format .

format-check: ## Check code formatting
	uv run ruff format --check .

type-check: ## Run type checker
	uv run mypy packages/ services/

clean: ## Clean build artifacts and cache
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	rm -rf htmlcov .coverage

dev: install ## Setup development environment
	@echo "Development environment ready!"

check: lint format-check type-check test ## Run all checks

api-service: ## Run API service
	uv run uvicorn api_service.main:app --reload
