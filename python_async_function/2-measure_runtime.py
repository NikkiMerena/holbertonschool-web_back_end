#!/usr/bin/env python3
"""
Module for measuring runtime
"""
from time import perf_counter
from asyncio import run
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the runtime
    """
    start_time = perf_counter()

    # Run the wait_n function and wait for it to complete
    run(wait_n(n, max_delay))

    end_time = perf_counter()

    # Calculate the total and average time
    total_time = end_time - start_time
    avg_time = total_time / n

    return avg_time
