"""Tests for text utilities."""

from shared_utils.text import capitalize_words, reverse_string


class TestCapitalizeWords:
    """Tests for capitalize_words function."""

    def test_capitalize_single_word(self) -> None:
        """Test capitalizing a single word."""
        assert capitalize_words("hello") == "Hello"

    def test_capitalize_multiple_words(self) -> None:
        """Test capitalizing multiple words."""
        assert capitalize_words("hello world") == "Hello World"

    def test_capitalize_already_capitalized(self) -> None:
        """Test capitalizing already capitalized text."""
        assert capitalize_words("Hello World") == "Hello World"

    def test_capitalize_empty_string(self) -> None:
        """Test capitalizing empty string."""
        assert capitalize_words("") == ""


class TestReverseString:
    """Tests for reverse_string function."""

    def test_reverse_simple_string(self) -> None:
        """Test reversing a simple string."""
        assert reverse_string("hello") == "olleh"

    def test_reverse_with_spaces(self) -> None:
        """Test reversing a string with spaces."""
        assert reverse_string("hello world") == "dlrow olleh"

    def test_reverse_empty_string(self) -> None:
        """Test reversing empty string."""
        assert reverse_string("") == ""

    def test_reverse_palindrome(self) -> None:
        """Test reversing a palindrome."""
        assert reverse_string("racecar") == "racecar"
