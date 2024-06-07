#!/usr/bin/env python3
"""A module for the concat() function using type annotations."""


def concat(str1: str, str2: str) -> str:
    """Returns a concatenated string.

    Args:
        str1: The first string to be concatenated.
        str2: The second string to be concatenated.

    Returns:
        A concatenated string of args `str1` and `str2`.
    """
    return (str1 + str2)
