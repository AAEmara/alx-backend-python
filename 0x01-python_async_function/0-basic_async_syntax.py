#!/usr/bin/env python3
"""A module that defines an asynchronous coroutine."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that wait for random delay and
    returns its value.

    Args:
        max_delay: A random number of seconds to wait for.

    Returns:
        The max_delay argument.
    """
    sleep_time: float = random.uniform(0, max_delay)
    await asyncio.sleep(sleep_time)

    return (sleep_time)
