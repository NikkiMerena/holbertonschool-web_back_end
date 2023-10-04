#!/usr/bin/env python3
"""Test module for client.GithubOrgClient"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Class for testing GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value
        and calls `get_json` once with the expected argument.
        """

        test_class_instance = GithubOrgClient(org_name)
        self.assertEqual(test_class_instance.org, {"payload": True})
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test that the result of _public_repos_url is the
        expected one based on the mocked payload."""

        # Creating a payload that org is expected to return
        payload = {"repos_url": "https://api.github.com/orgs/example/repos"}

        # Setting the return_value of the mocked property
        mock_org.return_value = payload

        # Creating an instance of GithubOrgClient
        client = GithubOrgClient("example")

        # Testing _public_repos_url returns the correct value
        self.assertEqual(
            client._public_repos_url,
            "https://api.github.com/orgs/example/repos"
        )
