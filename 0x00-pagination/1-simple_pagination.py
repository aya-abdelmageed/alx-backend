#!/usr/bin/env python3
"""Simple pagination"""
from typing import Tuple, List
import csv
import math


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """
        The function should return a tuple of size two
        containing a start index and an end index
        corresponding to the range of indexes
        return in a list for those particular pagination parameters.
        """
        end = page * page_size
        start = end - page_size
        return start, end

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        return the appropriate page of the dataset
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        if start > len(self.dataset()):
            return []
        return self.dataset()[start:end]
