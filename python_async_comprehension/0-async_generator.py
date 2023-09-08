#!/usr/bin/env python3
"""Module for storing the async_generator coroutine."""

from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """Coroutine to loop 10 times, wait 1 sec, yield
    random number between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
