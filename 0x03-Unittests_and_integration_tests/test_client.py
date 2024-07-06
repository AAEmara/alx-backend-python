#!/usr/bin/env python3
"""Testing functions of the client module
using patchers as decorator and as context manager
- This file has unit-tests and integration tests.
"""


import unittest
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Class for testing: client.GithubOrgClient.org
    - This class has unit-tests.
    """
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test GithubOrgClient.org function."""
        org_client = GithubOrgClient(org_name)
        url = f'https://api.github.com/orgs/{org_name}'
        mock_get_json.return_value = {"name": "abd"}
        self.assertEqual(org_client.org, {"name": "abd"})
        mock_get_json.assert_called_once_with(url)
