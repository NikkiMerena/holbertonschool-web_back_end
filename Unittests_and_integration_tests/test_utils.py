#!/usr/bin/env python3
"""Test module for utils.access_nested_map"""
import unittest
from parameterized import parameterized 
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock

class TestAccessNestedMap(unittest.TestCase):
    """Class to test the function 'access_nested"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test method for access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
