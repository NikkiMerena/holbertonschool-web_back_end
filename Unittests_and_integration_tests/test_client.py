#!/usr/bin/env python3
"""Test module for client.GithubOrgClient"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from fixtures import (
    org_payload,
    repos_payload,
    expected_repos,
    apache2_repos
)


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

    @patch('client.get_json', return_value=[
        {'name': 'repo1'},
        {'name': 'repo2'}
    ])
    def test_public_repos(self, mock_get_json):
        """
        Test that the list of repos is what you expect from the chosen payload.
        """
        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            # Define a custom return value for _public_repos_url property
            mock_public_repos_url.return_value = (
                "https://api.github.com/orgs/example/repos"
            )

            # Initialize an object of GithubOrgClient
            client = GithubOrgClient('example')

            # Call the public_repos method, and get the repo names
            repos = client.public_repos()

            # Assertions to validate the outcomes
            self.assertEqual(repos, ['repo1', 'repo2'])
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/example/repos"
            )
            mock_public_repos_url.assert_called_once_with()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_output):
        """Test GithubOrgClient.has_license method"""

        client = GithubOrgClient("example")

        # Testing if has_license returns the expected output
        self.assertEqual(
            client.has_license(repo, license_key),
            expected_output
        )


@parameterized_class([
    {"org_payload": org_payload, "repos_payload": repos_payload,
        "expected_repos": expected_repos, "apache2_repos": apache2_repos},
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient.public_repos method"""

    @classmethod
    def setUpClass(cls):
        """set up class method for setting up the tests"""

        cls.get_patcher = patch('requests.get')

        # Starting the patcher
        cls.get = cls.get_patcher.start()

        # Side effects for the patched method to return desired mock objects
        cls.get.side_effect = [
            cls.org_payload,
            cls.repos_payload,
        ]

    @classmethod
    def tearDownClass(cls):
        """Tear down class method for cleaning up after tests"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test the GithubOrgClient.public_repos method"""

        # Initializing GithubOrgClient
        test_client = GithubOrgClient('example_org_name')

        # Testing public_repos method returns expected repos
        self.assertEqual(test_client.public_repos(), self.expected_repos)

        # Making assertions about calls to the patched requests.get method
        self.get.assert_called_once_with(
            'https://api.github.com/orgs/example_org_name')
