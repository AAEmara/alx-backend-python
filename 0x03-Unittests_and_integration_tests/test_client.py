#!/usr/bin/env python3
"""A module that include test cases for `client` module."""


from client import GithubOrgClient
from parameterized import parameterized
from typing import Dict
import unittest
from unittest.mock import patch
import utils


class TestGithubOrgClient(unittest.TestCase):
    """A Class that includes tests for `GithubOrgClient` class.
    """

    @parameterized.expand([
        ["google", {"payload": True}],
        ["abc", {"payload": False}]
    ])
    @patch("client.get_json")
    def test_org(self,
                 org_name: str,
                 expected_result: Dict,
                 mock_get_json: Callable):
        """Testing the `GithubOrgClient.org` returned value.
        """
        test_instance = GithubOrgClient(org_name)
        url: str = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.return_value: str = expected_result
        test_result: str = test_instance.org
        mock_get_json.assert_called_once_with(url)
        self.assertEqual(test_result, expected_result)
