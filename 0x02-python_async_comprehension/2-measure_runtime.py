#!/usr/bin/env python3
"""A module that defines a coroutine with the help of asyncio."""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Measures the total time of executing a coroutine 4 times in parallel.

    Args:
        NOTHING

    Returns:
        The total time of execution.
    """
    start: float = time.perf_counter()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    end: float = time.perf_counter()
    total_time: float = end - start

    return (total_time)
