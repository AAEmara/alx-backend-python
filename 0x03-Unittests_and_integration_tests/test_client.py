#!/usr/bin/env python3
"""A module that include test cases for `client` module."""


from client import GithubOrgClient
from parameterized import parameterized
from typing import Dict
import unittest
from unittest.mock import patch, MagicMock


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
        test_instance = GithubOrgClient(org)  # Instance of the class.
        url = f"https://api.github.com/orgs/{org}"

        # Assigning the return value of the mocked method.
        mock_get.return_value = MagicMock(return_value=result)
        test_result = test_instance.org()
        mock_get.assert_called_once_with(url)  # Checking the call is done once
        self.assertEqual(test_result, result)
