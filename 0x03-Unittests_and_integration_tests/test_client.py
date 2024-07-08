#!/usr/bin/env python3
"""A module that include test cases for `client` module."""


from client import GithubOrgClient
from parameterized import parameterized
from typing import Dict
import unittest
from unittest.mock import patch, MagicMock, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """A Class that includes tests for `GithubOrgClient` class.
    """

    @parameterized.expand([
        ["google", {"payload": True}],
        ["abc", {"payload": False}]
    ])
    @patch("client.get_json")
    def test_org(self, org: str, result: Dict, mock_get: MagicMock) -> None:
        """Testing the `GithubOrgClient.org` returned value.
        Args:
            org_name: The name of the organization used in GitHub.
            expected_result: The expected payload returned result.
            mock_get: The mocked function used in the method.
        """
        test_instance = GithubOrgClient(org)
        url: str = f"https://api.github.com/orgs/{org}"
        mock_get.return_value: Dict = result
        test_result: Dict = test_instance.org
        mock_get.assert_called_once_with(url)
        self.assertEqual(test_result, result)

    def test_public_repos_url(self):
        """Testing the `GithubOrgClient._public_repos_url` returned value.
        """
        payload = {"repos_url": "https://api.github.com/google"}  # API Payload
        # Mocking the GithubOrgClient.org method.
        with patch.object(GithubOrgClient, "org") as mock_org:
            mock_org.return_value = payload  # Assigning returned payload.
            org_instance = GithubOrgClient("google")
            expected_repo_url = org_instance.org["repos_url"]  # Expected URL
            tested_repo_url = org_instance._public_repos_url  # Returned URL
            # Testing the returned url vs the expected url.
            self.assertEqual(tested_repo_url, expected_repo_url)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Testing the `GithubOrgClient.public_repos` returned value.
        """
        method: str = "_public_repos_url"
        payload: Dict = [{"name": "repo1"}, {"name": "repo2"}]
        url: str = "https://api.github.com/google"
        with patch.object(GithubOrgClient, method) as mock_public_repos_url:
            mock_public_repos_url.return_value = url
            mock_get_json.return_value = payload
            org_instance = GithubOrgClient("google")
            returned_url = org_instance._public_repos_url
            tested_repos = org_instance.public_repos(None)
            expected_repos = ["repo1", "repo2"]
            self.assertEqual(tested_repos, expected_repos)
