#!/usr/bin/env python3
"""Module for index_range method"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """A function to return a tuple of size two containing
    a start index and an end index corresponding to the range of
    indexes to return in a list for those particular pagination parameters.

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end index.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
