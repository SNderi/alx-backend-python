#!/usr/bin/env python3
"""Module for measure_runtime coroutine that uses asyncio.gather.
"""

import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes async_comprehension four times in parallel using
    asyncio.gather, measures the total runtime and returns it.
    """
    start = perf_counter()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    return perf_counter() - start
