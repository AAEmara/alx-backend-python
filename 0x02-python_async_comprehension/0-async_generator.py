#!/usr/bin/env python3
"""A module that defines a coroutine."""

import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """Generates a list of random numbers asynchronously.

    Args:
        NOTHING

    Returns:
        A list of random numbers.
    """
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
