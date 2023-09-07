#!/usr/bin/env python3
"""Module contain a func that return a function
that multiplies a float by a multiplier."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier to be used in the returned function.

    Returns:
        Callable[[float], float]: A function that takes a float and returns a
        float which is the
        result of multiplying the input by the multiplier.
    """
    def multiplier_func(n: float) -> float:
        """Multiplies the input float n by the multiplier.

        Args:
            n (float): The number to be multiplied.

        Returns:
            float: The result of multiplying n by the multiplier.
        """
        return n * multiplier

    return multiplier_func
