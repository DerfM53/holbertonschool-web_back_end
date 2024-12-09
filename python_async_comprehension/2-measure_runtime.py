#!/usr/bin/env python3
"""
This module contain a function for
measure a execution time
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    This function measure the time for
    execution an other function for 4 loops
    """
    start_time = time.time()
    result = await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    total_time = end_time - start_time
    return total_time
