#!/usr/bin/env python3
''' reate a TestAccessNestedMap class that inherits from unittest.TestCase.
Implement the TestAccessNestedMap.test_access_nested_map method to test that
the method returns what it is supposed to.

Decorate the method with @parameterized.expand to test the function for
following inputs:
'''
import json
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize

from typing import Dict, Union, Tuple
from unittest.mock import patch, MagicMock


class TestAccessNestedMap(unittest.TestCase):
    ''' TestAccessMap test class that inherits from TestCase '''

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

    @parameterized.expand([
            ({}, ("a",)),
            ({"a": 1}, {"a", "b"})
        ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Union[Dict, Tuple]
            ) -> None:
        ''' tests for KeyError exception '''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    ''' a class that tests get_json '''

    @parameterized.expand([
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        ''' test the results of utils.get_json ,use Mock '''
        with patch('utils.requests.get') as mock_requests:
            res = MagicMock()
            res.status_code = 200
            res.json.return_value = test_payload
            mock_requests.return_value = res
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    ''' class that tests if a_method is called once inside a_property '''
    def test_memoize(self):
        ''' test that when calling a_property_] twice, the correct
        result is returned but a_method is called only once using
        assert_called_once '''
        class TestClass:
            def a_method():
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42
                ) as mem_func:
            t_cls = TestClass()
            self.assertEqual(t_cls.a_property(), 42)
            self.assertEqual(t_cls.a_property(), 42)
            mem_func.assert_called_once()
