#!/bin/usr/env python3
""" Write a type-annotated function concat that takes a string str1
    and a string str2 as arguments and returns a concatenated string """


def concat(str1: str, str2: str) -> str:
    """ returns concatinated string of str1 and str2 """
    return "{}{}".format(str1, str2)
