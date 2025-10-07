"""Tests for the main API."""

import pytest
from api_service.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


class TestRootEndpoint:
    """Tests for root endpoint."""

    def test_read_root(self) -> None:
        """Test root endpoint returns welcome message."""
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Welcome to the API service"}


class TestTextEndpoints:
    """Tests for text manipulation endpoints."""

    def test_capitalize(self) -> None:
        """Test capitalize endpoint."""
        response = client.get("/text/capitalize?text=hello world")
        assert response.status_code == 200
        data = response.json()
        assert data["input"] == "hello world"
        assert data["output"] == "Hello World"

    def test_reverse(self) -> None:
        """Test reverse endpoint."""
        response = client.get("/text/reverse?text=hello")
        assert response.status_code == 200
        data = response.json()
        assert data["input"] == "hello"
        assert data["output"] == "olleh"


class TestMathEndpoints:
    """Tests for math operation endpoints."""

    def test_add(self) -> None:
        """Test add endpoint."""
        response = client.get("/math/add?a=2&b=3")
        assert response.status_code == 200
        data = response.json()
        assert data["a"] == 2
        assert data["b"] == 3
        assert data["result"] == 5

    def test_multiply(self) -> None:
        """Test multiply endpoint."""
        response = client.get("/math/multiply?a=4&b=5")
        assert response.status_code == 200
        data = response.json()
        assert data["a"] == 4
        assert data["b"] == 5
        assert data["result"] == 20

    def test_add_with_floats(self) -> None:
        """Test add endpoint with floats."""
        response = client.get("/math/add?a=2.5&b=3.7")
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == pytest.approx(6.2)
