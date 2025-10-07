# api-service

Example API service that demonstrates using shared packages from the monorepo.

## Features

- FastAPI-based REST API
- Uses `shared-utils` package for text and math operations
- Fully tested with pytest

## Endpoints

- `GET /` - Welcome message
- `GET /text/capitalize?text=...` - Capitalize words in text
- `GET /text/reverse?text=...` - Reverse text
- `GET /math/add?a=...&b=...` - Add two numbers
- `GET /math/multiply?a=...&b=...` - Multiply two numbers

## Running the service

From the monorepo root:

```bash
uv run uvicorn api_service.main:app --reload
```

The API will be available at `http://localhost:8000`. Visit `http://localhost:8000/docs` for the interactive API documentation.

## Testing

Run tests from the monorepo root:

```bash
uv run pytest services/python/api-service/tests
```
