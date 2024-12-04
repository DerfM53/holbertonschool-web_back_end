#!/usr/bin/env python3

"""
Module to create a multiplier function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function.

    This function takes a float 'multiplier' as an argument and returns
    a new function that multiplies any given float by this multiplier.

    Args:
        multiplier (float): The factor by which to multiply the input.

    Returns:
        Callable[[float], float]: A function that takes a float as input
        and returns the product of the input and the multiplier.
    """
    def multiply(n: float) -> float:
        """
        Multiplies the input number by the predefined multiplier.

        Args:
            n (float): The number to be multiplied.

        Returns:
            float: The product of 'n' and the multiplier.
        """
        return n * multiplier
    return multiply
