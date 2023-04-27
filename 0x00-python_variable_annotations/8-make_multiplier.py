#!/bin/usr/env python3
""" Write a type-annotated function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier. """


def make_multiplier(multiplier: float) -> function:
    return lambda x: x * multiplier
