#!/usr/bin/env python3
"""A module that creates floor() function with type annotation."""

import math


def floor(n: float) -> float:
    """Returns the floor of the entered argument.

    Args:
        n: The number to be floored.

    Returns:
        The floored number from the args.
    """
    return (math.floor(n))
