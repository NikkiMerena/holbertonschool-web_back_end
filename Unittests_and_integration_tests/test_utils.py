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

class TestAccessNestedMap(unittest.TestCase):
    """Class for testing access_nested_map function"""
    
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map raises a KeyError"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        
        # If you need to check the exception message, you can use:
        # self.assertEqual(str(e.exception), "Your expected exception message")
