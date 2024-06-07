#!/usr/bin/env python3
"""A module that defines sum_list() function using type-annotations."""

import typing


def sum_list(input_list: typing.List[float]) -> float:
    """Returns the sum of numbers in a list.

    Args:
        input_list: The list that contains float items.

    Returns:
        The sum of the items inside of the given list.
    """
    total: float = 0.0

    for num in input_list:
        total += num

    return (total)
