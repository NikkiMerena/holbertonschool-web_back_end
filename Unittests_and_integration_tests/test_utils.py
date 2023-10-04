#!/usr/bin/env python3
"""Test module for utils.access_nested_map"""
import unittest
from parameterized import parameterized 
from utils import access_nested_map, get_json
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

class TestGetJson(unittest.TestCase):
    """Testing get_Json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"paylaod": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that utils.get_json returns the expected result."""
        
        # Create a Mock object that returns `test_payload` when its `.json()` method is called.
        mock_get.return_value.json.return_value = test_payload
        
        # Call the function and check its return value
        self.assertEqual(get_json(test_url), test_payload)
        
        # Check that `requests.get` was called with `test_url`
        mock_get.assert_called_once_with(test_url)
