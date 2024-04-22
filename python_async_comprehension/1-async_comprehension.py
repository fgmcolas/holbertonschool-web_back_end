#!/usr/bin/env python3
""" coroutine for collecting random numbers asynchronously """
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ coroutine that collects random numbers asynchronously """
    random_numbers = [num async for num in async_generator()]
    return random_numbers
