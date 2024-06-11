#!/usr/bin/env python3
"""A module the defines a function that measures the runtime."""

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the average execution time of wait_n function.
    Args:
        n: The number of function calls.
        max_delay: The maximum delay the function can have in seconds.

    Returns:
        The average execution time for all of the function calls.
    """
    start: int = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end: int = time.perf_counter() - start
    avg_execution: float = end / n

    return (avg_execution)
