#!/usr/bin/env python3
"""Function that takes two integer arguments <page> and <page_size>"""
import csv
import math
from typing import List, Tuple


def index_range(page, page_size):
    """return start and end"""
    end = page * page_size
    start = end - page_size
    return (start, end)


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
        """return the appropriate page of the dataset"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        self.dataset()
        start, end = index_range(page, page_size)
        if start >= len(self.__dataset):
            return []
        return self.__dataset[start:min(end, len(self.__dataset))]
