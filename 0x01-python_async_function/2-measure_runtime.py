#!/usr/bin/env python3
''' From the previous file, import wait_n into 2-measure_runtime.py.

Create a measure_time function with integers n and max_delay
as arguments that measures the total execution time for
wait_n(n, max_delay), and returns total_time / n. Your function
should return a float.

Use the time module to measure an approximate elapsed time.
'''
import importlib
import time
import asyncio

delayf = importlib.import_module('1-concurrent_coroutines')

async def measure_time(n: int, max_delay: int) -> float:
    #s = time.perf_counter()
    asyncio.run(gather(n, max_delay))
    #elapsed = time.perf_counter() - s
    #return elapsed / n
async def gather(n: int, max_delay: int) -> float:
	await asyncio.gather(delayf.wait_n(n, max_delay))
