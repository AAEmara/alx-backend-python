#!/usr/bin/env python3
"""A module that include test cases for `client` module."""


from client import GithubOrgClient
from parameterized import parameterized
from typing import Dict, Callable
import unittest
from unittest.mock import patch, Mock


class TestGithubOrgClient(unittest.TestCase):
    """A Class that includes tests for `GithubOrgClient` class.
    """

    @parameterized.expand([
        ["google", "https://api.github.com/orgs/google"],
        ["abc", "https://api.github.com/orgs/abc"]
    ])
    @patch("client.get_json")
    def test_org(self, org: str, url: str, mock_get_json: Mock) -> None:
        """Testing the `GithubOrgClient.org` returned value.
        Args:
            org: The name of the organization used in GitHub.
            url: The expected payload returned result.
            mock_get_json: The mocked function used in the method.
        """
        instance = GithubOrgClient(org)
        result1 = instance.org
        result2 = instance.org
        result3 = instance.org

        mock_get_json.assert_called_once_with(url)
