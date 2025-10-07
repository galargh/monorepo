"""Main application entry point."""

from fastapi import FastAPI
from shared_utils import add, capitalize_words, multiply, reverse_string

app = FastAPI(title="API Service", version="0.1.0")


@app.get("/")
def read_root() -> dict[str, str]:
    """Root endpoint.

    Returns:
        Welcome message.
    """
    return {"message": "Welcome to the API service"}


@app.get("/text/capitalize")
def capitalize(text: str) -> dict[str, str]:
    """Capitalize words in text.

    Args:
        text: Text to capitalize.

    Returns:
        Capitalized text.
    """
    result = capitalize_words(text)
    return {"input": text, "output": result}


@app.get("/text/reverse")
def reverse(text: str) -> dict[str, str]:
    """Reverse text.

    Args:
        text: Text to reverse.

    Returns:
        Reversed text.
    """
    result = reverse_string(text)
    return {"input": text, "output": result}


@app.get("/math/add")
def add_numbers(a: float, b: float) -> dict[str, float]:
    """Add two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        Sum of the numbers.
    """
    result = add(a, b)
    return {"a": a, "b": b, "result": result}


@app.get("/math/multiply")
def multiply_numbers(a: float, b: float) -> dict[str, float]:
    """Multiply two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        Product of the numbers.
    """
    result = multiply(a, b)
    return {"a": a, "b": b, "result": result}
