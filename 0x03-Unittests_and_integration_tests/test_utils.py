#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from typing import Mapping, Sequence
from unittest.mock import MagicMock, patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Class to test utils.access_nested_map function.
    """
    @parameterized.expand([
        ("test_1nest", {"a": 1}, ["a"], 1),
        ("test_1step", {"a": {"b": 2}}, ["a"], {"b": 2}),
        ("test_2steps", {"a": {"b": 2}}, ["a", "b"], 2)
    ])
    def test_access_nested_map(self, name: str, mapp: Mapping,
                               key: Sequence, expected_output: int) -> None:
        """Tests that access_nested_map returns the correct output."""
        self.assertEqual(access_nested_map(mapp, key), expected_output)

    @parameterized.expand([
        ("test_empty", {}, ["a"]),
        ("test_wrong_path", {"a": 1}, ["a", "b"])
    ])
    def test_access_nested_map_exception(self, name: str, mapp: Mapping,
                                         key: Sequence) -> None:
        """Tests that access_nested_map raises an Exception on error."""
        with self.assertRaises(Exception):
            access_nested_map(mapp, key)


class TestGetJson(unittest.TestCase):
    """Class to test utils.get_json function.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        """ Test the get_json method to ensure it returns the expected output.
        """
        mock_requests_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_requests_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Test the memoization decorator, memoize
    """
    def test_memoize(self):
        """
        Test that utils.memoize decorator works as intended
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock_object:
            test = TestClass()
            test.a_property()
            test.a_property()
            mock_object.assert_called_once()
