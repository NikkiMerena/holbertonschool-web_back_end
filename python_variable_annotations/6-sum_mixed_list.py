#!/usr/bin/env python3
"""This module contains a function that sums a list of integers and floats."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums a list of integers and floats and returns the sum as a float.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers & floats to sum.

    Returns:
        float: The sum of all values in the input list.
    """
    return sum(mxd_lst)
