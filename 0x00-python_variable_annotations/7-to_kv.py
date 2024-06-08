#!/usr/bin/env python3
"""A module that defines to_kv() function with type-annotation."""

import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """Returns tuple out of the arguments given.

    Args:
        k: A string argument.
        v: A number that maybe an integer or a float.

    Returns:
        A tuple composed of two elements (a string, a float).
    """
    return ((k, v*v))
