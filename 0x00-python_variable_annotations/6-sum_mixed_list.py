#!/usr/bin/env python3
"""A module that defines a sum_mixed_list() function with type-annotation."""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """Returns the sum of items in a list.

    Args:
        mxd_lst: A list of numbers that could be an int or float.

    Returns:
        The sum of the numbers in the argument's list.
    """
    total: float = 0.00

    for num in mxd_lst:
        total += num

    return (total)
