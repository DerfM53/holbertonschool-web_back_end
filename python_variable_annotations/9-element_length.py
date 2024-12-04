#!/usr/bin/env python3

"""
Module to calculate the length of elements in a sequence.

This module provides a function `element_length` that takes an iterable
of sequences and returns a list of tuples, where each tuple contains
the sequence and its corresponding length.
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculates the length of each sequence in the iterable.

    This function takes an iterable of sequences (like lists or tuples)
    and returns a list of tuples. Each tuple contains a sequence and
    its length.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences
        (e.g., lists, tuples, strings).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple
        contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
