#!/usr/bin/env python3
"""Task 1"""

import csv
import math
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns the appropriate page of the dataset based
        on the pagination parameters.

        Parameters:
            page (int): The page number (1-indexed). Default is 1.
            page_size (int): The size of each page. Default is 10.

        Returns:
            List[List]: The list of rows representing the appropriate
            page of the dataset.
        """

        assert isinstance(page, int) and page > 0, "Page must be +ve"
        assert isinstance(page_size, int) and page_size > 0, "Has to be +ve"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        return dataset[start_index:end_index]
