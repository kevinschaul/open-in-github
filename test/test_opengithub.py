#!/usr/bin/env python

import unittest

from opengithub.opengithub import get_branch_from_git_status_output

class TestGetBranchFromGitStatusOutput(unittest.TestCase):

    def test_simple(self):
        status_output = """## master...origin/master
 M setup.py"""
        expected = 'master'
        actual = get_branch_from_git_status_output(status_output)
        self.assertEqual(expected, actual)

    def test_git_flow_style(self):
        status_output = '## hotfix/1'
        expected = 'hotfix/1'
        actual = get_branch_from_git_status_output(status_output)
        self.assertEqual(expected, actual)
