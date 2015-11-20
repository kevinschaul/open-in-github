#!/usr/bin/env python

import unittest

from opengithub.opengithub import (extract_github_address,
        get_branch_from_git_status_output)

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

class TestExtractGithubAddress(unittest.TestCase):

    def test_ssh(self):
        git_config = """
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
	ignorecase = true
	precomposeunicode = true
[remote "origin"]
	url = git@github.com:kevinschaul/open-in-github.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
"""
        expected = 'https://github.com/kevinschaul/open-in-github'
        actual = extract_github_address(git_config)
        self.assertEqual(expected, actual)

    def test_https(self):
        git_config = """
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
	ignorecase = true
	precomposeunicode = true
[remote "origin"]
	url = https://github.com/kevinschaul/open-in-github.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
"""
        expected = 'https://github.com/kevinschaul/open-in-github'
        actual = extract_github_address(git_config)
        self.assertEqual(expected, actual)

    def test_multiple_remotes(self):
        git_config = """
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
	ignorecase = true
	precomposeunicode = true
[remote "origin"]
	url = https://github.com/kevinschaul/open-in-github.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[remote "adjohnson916"]
	url = https://github.com/adjohnson916/open-in-github.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
"""
        expected = 'https://github.com/kevinschaul/open-in-github'
        actual = extract_github_address(git_config)
        self.assertEqual(expected, actual)

