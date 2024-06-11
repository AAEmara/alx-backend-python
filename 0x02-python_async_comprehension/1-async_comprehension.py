#!/usr/bin/env python3
"""A module that defines a coroutine."""

import asyncio
from typing import Generator, List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """Uses a coroutine to return 10 random numbers from it.

    Args:
        NOTHING

    Returns:
        A list of 10 random numbers.
    """
    results = [i async for i in async_generator()]
    return (results)
