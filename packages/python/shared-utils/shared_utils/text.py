"""Text manipulation utilities."""


def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word in the text.

    Args:
        text: The input text to capitalize.

    Returns:
        The text with each word capitalized.
    """
    return " ".join(word.capitalize() for word in text.split())


def reverse_string(text: str) -> str:
    """Reverse a string.

    Args:
        text: The input text to reverse.

    Returns:
        The reversed text.
    """
    return text[::-1]
