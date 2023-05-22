#!/usr/bin/env python3
''' test if githuborgclient.org returns ther correct value
use patch decorator '''
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        ''' tests _public_repos_url '''
        with patch.object(
                GithubOrgClient,
                'org',
                new_callable=PropertyMock
                ) as mock:
            mock.return_value = {'repos_url': 'hello'}
            org_test = GithubOrgClient('org name')
            t_repo_url = org_test._public_repos_url
            self.assertEqual(t_repo_url, mock.return_value.get('repos_url'))
            mock.assert_called_once()
