#!/usr/bin/env python3
"""
This module contain a function for
manipulation data
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    This function take two argument
    and return a data sort
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
