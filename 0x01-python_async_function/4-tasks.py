#!/usr/bin/env python3
''' Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called.
'''
from typing import List
import importlib
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    ''' return list of delays as float '''
    lst_delay = []
    lst_tasks = []
    for task in range(n):
        tsk = task_wait_random(max_delay)
        lst_tasks.append(tsk)

    lst_delay = [await tsk for tsk in asyncio.as_completed(lst_tasks)]
    return lst_delay
