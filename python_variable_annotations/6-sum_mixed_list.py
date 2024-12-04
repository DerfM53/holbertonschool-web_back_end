#!/usr/bin/env python3

"""
This module contain a function who take a list of
the integer and floats and return the sum of the
numbers of the list
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of the mxd_lst"""
    return sum(mxd_lst)
