#!/usr/bin/python3

"""
This function take a string and a float an arguments and
return à string and the square of the float inside the
tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple with inside k and the square of v
    """
    return (k, v * v)
