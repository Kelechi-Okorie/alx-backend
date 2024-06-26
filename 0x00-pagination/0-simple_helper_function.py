#!/usr/bin/env python3
"""returns start and end index for a given pagination parameters"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple containing a start index and an end index
    corresponding to the range of indexes
    to return in a list for the given pagination parameters.

    Parameters:
        page (int): The page number (1-indexed).
        page_size (int): The size of each page.

    Returns:
        tuple: A tuple containing the start index and end index of the range.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Page and page_size must be positive integers.")

    start_index = (page - 1) * page_size
    # end_index = start_index + page_size - 1
    end_index = start_index + page_size
    return start_index, end_index
