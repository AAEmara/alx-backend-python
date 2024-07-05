#!/usr/bin/env python3
"""A module that includes a unit test for utils.py file."""


import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
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


class TestMemoize(unittest.TestCase):
    """A class that includes tests for the `memoize` function.
    """
    def test_memoize(self):
        """Test a method that is already cached `memoized`.
        """

        class TestClass:
            """A Class that is going to be tested for memoization.
            """
            def a_method(self):
                """A method that returns a value.
                Args:
                    NOTHING
                Returns:
                    Return an integer of a value equals to 42.
                """
                return 42

            @memoize
            def a_property(self):
                """A method that is going to be memoized.
                """
                return self.a_method()

        with patch.object(TestClass, "a_method") as mock_a_method:
            mock_a_method.return_value = 42
            test_instance = TestClass()
            result1 = test_instance.a_property
            result2 = test_instance.a_property
            mock_a_method.assert_called_once_with()
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
