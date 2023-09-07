#!/usr/bin/env python3
"""Module for getting the length of elements in a list"""

from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes an iterable of sequences and returns a list of
    tuples with each sequence and its length

    Args:
        lst (Iterable[Sequence]): An iterable of sequences

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples
        containing each sequence and its length
    """
    return [(i, len(i)) for i in lst]
