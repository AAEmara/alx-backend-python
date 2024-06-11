#!/usr/bin/env python3
"""A module that defines an asynchronous coroutine using asyncio."""

import asyncio
import typing

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Calls wait_random async function n times and returns a list of delays.
    Args:
        n: Number of wait_random function will be spwaned.
        max_delay: The upper bound of delaying seconds.

    Return:
        A list of the no. of seconds delayed for each function.
    """
    delay_list = await asyncio.gather(*(wait_random(max_delay)
                                      for _ in range(n)))
    return (delay_list)
