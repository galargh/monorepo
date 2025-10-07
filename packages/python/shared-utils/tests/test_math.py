"""Tests for math utilities."""

import pytest
from shared_utils.math import add, multiply


class TestAdd:
    """Tests for add function."""

    def test_add_positive_integers(self) -> None:
        """Test adding positive integers."""
        assert add(2, 3) == 5

    def test_add_negative_integers(self) -> None:
        """Test adding negative integers."""
        assert add(-2, -3) == -5

    def test_add_mixed_integers(self) -> None:
        """Test adding mixed sign integers."""
        assert add(-2, 3) == 1

    def test_add_floats(self) -> None:
        """Test adding floats."""
        assert add(2.5, 3.7) == pytest.approx(6.2)

    def test_add_zero(self) -> None:
        """Test adding zero."""
        assert add(5, 0) == 5


class TestMultiply:
    """Tests for multiply function."""

    def test_multiply_positive_integers(self) -> None:
        """Test multiplying positive integers."""
        assert multiply(2, 3) == 6

    def test_multiply_negative_integers(self) -> None:
        """Test multiplying negative integers."""
        assert multiply(-2, -3) == 6

    def test_multiply_mixed_integers(self) -> None:
        """Test multiplying mixed sign integers."""
        assert multiply(-2, 3) == -6

    def test_multiply_floats(self) -> None:
        """Test multiplying floats."""
        assert multiply(2.5, 3.0) == pytest.approx(7.5)

    def test_multiply_by_zero(self) -> None:
        """Test multiplying by zero."""
        assert multiply(5, 0) == 0
