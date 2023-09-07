#!/usr/bin/env python3
"""module has a function, returns a tuple w/ a string & the square of a #."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple where the 1st element=str & the 2nd is the square of a #.

    Args:
        k (str): The first element in the tuple.
        v (Union[int, float]): The number to be squared.

    Returns:
        Tuple[str, float]:A tuple contain the str & the sq of the # as a float.
    """
    return k, v ** 2
