#!/usr/bin/env python3
"""A module that defines a function that calls task_wait_random function."""

import asyncio
import typing

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Calls wait_random async function n times and returns a list of delays.
    Args:
        n: Number of wait_random function will be spwaned.
        max_delay: The upper bound of delaying seconds.

    Return:
        A list of the no. of seconds delayed for each function.
    """
    delay_list = await asyncio.gather(*(task_wait_random(max_delay)
                                      for _ in range(n)))
    return (delay_list)
