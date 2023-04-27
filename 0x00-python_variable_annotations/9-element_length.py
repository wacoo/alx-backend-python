#!/usr/bin/env python3

""" Annotate the below function’s parameters and
return values with the appropriate types
def element_length(lst):
    return [(i, len(i)) for i in lst]
"""

from typing import Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> Tuple[Sequence, int]:
    """ return a Tuple with (element, length-of-lement) """
    return [(i, len(i)) for i in lst]
