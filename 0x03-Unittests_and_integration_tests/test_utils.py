#!/usr/bin/python3
''' reate a TestAccessNestedMap class that inherits from unittest.TestCase.
Implement the TestAccessNestedMap.test_access_nested_map method to test that
the method returns what it is supposed to.

Decorate the method with @parameterized.expand to test the function for
following inputs:
'''
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Dict, Union, Tuple


class TestAccessNestedMap(unittest.TestCase):
    ''' TestAccessMap test class that inherits from TestCase '''

    def setUp(self):
        ''' setup test data '''
        self.nested_map = {"a": {"b": {"c": 1}}}

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self, nested: Dict,
            path: Tuple[str],
            expected: [Dict, int]
            ) -> None:
        ''' tests if the function access_nested_map
        returns what it is suppose to '''
        self.assertEqual(access_nested_map(nested, path), expected)
