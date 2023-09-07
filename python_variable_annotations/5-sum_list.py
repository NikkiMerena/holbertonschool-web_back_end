#!/usr/bin/env python3
"""This module contains a function that sums a list of floats."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums a list of floats and returns the sum.

    Args:
        input_list (List[float]): A list of float values to sum.

    Returns:
        float: The sum of all float values in the input list.
    """
    return sum(input_list)
