#!/usr/bin/env python3
"""A module that defines element_length() function using type-annotation."""

import typing


def element_length(lst: typing.Iterable[typing.Sequence])\
        -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """Returning a list of tuples that have a Sequence and length of Sequence.
    """
    return [(i, len(i)) for i in lst]
