#!/usr/bin/env python3
"""Module for storing the measure_runtime coroutine."""

import asyncio
from time import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Coroutine to execute async_comprehension four times in parallel
    using asyncio.gather and measure the total runtime."""
    start_time = time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time()

    return end_time - start_time
