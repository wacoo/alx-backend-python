#!/usr/bin/env python3
""" Write a type-annotated function floor which takes a float n as
argument and returns the floor of the float.
"""
import math
from typing import TypeVar

T = TypeVar('T')


def floor(n: float) -> int:
    """ returns the floor integer of n """
    return math.floor(n)
