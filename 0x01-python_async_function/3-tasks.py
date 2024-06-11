#!/usr/bin/env python3
"""A module that defines a function that returns asyncio.Task."""

import asyncio
import typing

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> typing.Awaitable:
    """Creates a task with asyncio.
    Args:
        max_delay: The upper bound of delaying seconds.

    Returns:
        A task of asyncio.Task type.
    """
    return (asyncio.create_task(wait_random(max_delay)))
