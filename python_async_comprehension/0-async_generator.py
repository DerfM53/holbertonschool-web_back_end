#!/usr/bin/env python3
"""This module contain a generator asynchron"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    This function return a float random
    for 10 loops with 1 second between loops
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random()
