#!/usr/bin/env python3
"""A module that include test cases for `client` module."""


from client import GithubOrgClient
from parameterized import parameterized
from typing import Dict
import unittest
from unittest.mock import patch, Mock


class TestGithubOrgClient(unittest.TestCase):
    """A Class that includes tests for `GithubOrgClient` class.
    """

    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google"),
        ("abc", "https://api.github.com/orgs/abc")
    ])
    @patch("client.get_json")
    def test_org(self, org, arg, mock_org):
        """Testing the `GithubOrgClient.org` returned value.
        Args:
            org: The name of the organization used in GitHub.
            url: The expected payload returned result.
            mock_org: The mocked function used in the method.
        """
        git_client = GithubOrgClient(org)
        org_resp_mock = git_client.org
        org_resp_mock = git_client.org
        org_resp_mock = git_client.org

        mock_org.assert_called_once_with(arg)
