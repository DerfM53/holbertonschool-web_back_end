#!/usr/bin/env python3

"""
This module contain a function who take a list of
the integer and floats and return the sum of the
numbers of the list
"""
from typing import Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    return sum(mxd_lst)
