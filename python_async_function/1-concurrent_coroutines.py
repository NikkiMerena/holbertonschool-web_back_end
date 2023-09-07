#!/usr/bin/env python3
"""This module contains an asynchronous routine that concurrently runs
wait_random n times and returns the list of delay values in ascending order.
"""

from typing import List
import asyncio
from random import uniform
wait_random = async_generator = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """An asynchronous routine that concurrently calls 'wait_random' n times
    with the specified max_delay, and returns a list of the float values
    representing the delays, sorted in ascending order.

    Args:
    - n: int - The number of times to call 'wait_random'.
    - max_delay: int - The maximum delay value to pass to 'wait_random'.

    Returns:
    - List[float] - The list of delay values in ascending order.
    """
    delay_list = []
    for i in range(n):
        delay_list.append(wait_random(max_delay))

    completed_tasks = await asyncio.gather(*delay_list)
    return sorted(completed_tasks)
