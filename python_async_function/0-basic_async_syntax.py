#!/usr/bin/env python3
"""This module contains a coroutine that waits for a random delay."""

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that takes in an integer argument
    (max_delay, with a default value of 10) and waits for a random
    delay between 0 and max_delay (included and float value) seconds
    and eventually returns it.

    Args:
    - max_delay: int = 10 - maximum delay time

    Returns:
    - float - the actual delay time
    """
    random_delay = uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
