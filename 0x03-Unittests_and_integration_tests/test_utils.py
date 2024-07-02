#!/usr/bin/env python3
"""A module that includes a unit test for utils.py file."""


import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """A class that includes tests for the `access_nested_map` function.
    """

    @parameterized.expand([
        [{"a": 1}, ("a",), 1],
        [{"a": {"b": 2}}, ("a",), {"b": 2}],
        [{"a": {"b": 2}}, ("a", "b"), 2]
    ])
    def test_access_nested_map(self, nested_map, path, value):
        """Testing the return output of the function.
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, value)

    @parameterized.expand([
        [{}, ("a",), "a"],
        [{"a": 1}, ("a", "b"), "b"]
    ])
    def test_access_nested_map_exception(self, nested_map, path, value):
        """Testing the raised exception of the function.
        """
        with self.assertRaises(KeyError) as context_manager:
            access_nested_map(nested_map, path)

        exception = context_manager.exception
        self.assertEqual(str(exception), str(KeyError(value)))


class TestGetJson(unittest.TestCase):
    """A class that includes tests for the `get_json` function.
    """

    @parameterized.expand([
        ["http://example.com", {"payload": True}],
        ["http://holberton.io", {"payload": False}]
    ])
    def test_get_json(self, url, payload):
        """Testing the return output of the function.
        """
        with patch("requests.get") as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = payload
            mock_get.return_value = mock_response
            result = get_json(url)
            mock_get.assert_called_once_with(url)
            self.assertEqual(result, payload)
