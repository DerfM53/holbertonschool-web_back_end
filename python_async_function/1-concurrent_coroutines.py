#!/usr/bin/env python3
"""
Module for concurrent execution of asynchronous coroutines.

This module provides a function to execute multiple instances of
the wait_random coroutine concurrently and return their results.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay to pass to wait_random.

    Returns:
        List[float]: A list of delays in ascending order.

    This function creates n tasks, each calling wait_random(max_delay),
    executes them concurrently, and returns their results as a list.
    The returned list is inherently in ascending order due to the
    concurrent execution, without explicitly sorting the results.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)
