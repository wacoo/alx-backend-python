#!/usr/bin/env python3

''' Write an asynchronous coroutine that takes in an integer argument
    max_delay = 10...
'''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> None:
    ''' returns a random delay float '''
    delay_time = random.random() * max_delay
    await asyncio.sleep(delay_time)
    return delay_time
