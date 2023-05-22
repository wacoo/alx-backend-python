#!/usr/bin/env python3
''' test if githuborgclient.org returns ther correct value
use patch decorator '''
import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    ''' TestGithubClient class '''
    @parameterized.expand([
            ("google"),
            ("abc")
        ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org, m_org):
        ''' make sure get_json is colled once '''
        test_org = GithubOrgClient(org)
        test_res = test_org.org
        self.assertEqual(test_res, m_org.return_value)
        m_org.assert_called_once()
