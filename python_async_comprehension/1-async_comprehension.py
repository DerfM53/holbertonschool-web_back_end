#!/usr/bin/env python3
"""This module contain a async comprehension"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    This function return a list
    of number make to other function
    """
    result = []
    async for i in async_generator():
        result.append(i)
    return result
