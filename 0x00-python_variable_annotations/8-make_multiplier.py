#!/usr/bin/env python3
"""A module that defines make_multiplier() function that is type annotated."""

import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """Returns a function that multiplies current arg with a float.
    """
    def another_multiplier(multiplier_2: float) -> float:
        return (multiplier * multiplier_2)

    return (another_multiplier)
