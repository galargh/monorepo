# shared-utils

Shared utility library for the monorepo.

## Features

- **Text utilities**: String manipulation functions
- **Math utilities**: Basic mathematical operations

## Installation

This package is part of the monorepo workspace. It's automatically available to other packages and services in the workspace.

## Usage

```python
from shared_utils import capitalize_words, reverse_string, add, multiply

# Text utilities
result = capitalize_words("hello world")  # "Hello World"
reversed_text = reverse_string("hello")   # "olleh"

# Math utilities
sum_result = add(2, 3)        # 5
product = multiply(4, 5)       # 20
```

## Testing

Run tests from the monorepo root:

```bash
uv run pytest packages/python/shared-utils/tests
```
