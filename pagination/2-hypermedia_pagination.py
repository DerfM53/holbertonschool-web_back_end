#!/usr/bin/env python3
"""This module contain à class and method
for sort file database
"""
import csv
import math
from typing import List, Dict
index_range = __import__('0-simple_helper_function').index_range


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
        """
        This function take two arguments
        and return the index list asking
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        dataset = self.dataset()
        start, end = index_range(page, page_size)
        if start >= len(dataset):
            return []
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        This function take 2 arguments for self DATA_SET
        and return a dictionnary with multi-values
        """
        dataset = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": len(dataset),
            "page": page,
            "data": dataset,
            "next_page": (page + 1 if page < total_pages else None),
            "prev_pages": (page - 1 if page > 1 else None),
            "total_pages": total_pages
            }
