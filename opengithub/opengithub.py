#! /usr/bin/env python

import argparse
import os
import posixpath
import re
import subprocess
import sys
import webbrowser

def parse_arguments():
    parser = argparse.ArgumentParser()
    subpage = parser.add_mutually_exclusive_group()
    subpage.add_argument('-c', '--commits', dest='commits', action='store_true',
        help='Open to the GitHub Commits page (for master branch)')
    subpage.add_argument('-i', '--issues', dest='issues', action='store_true',
        help='Open to the GitHub issues page')
    subpage.add_argument('-p', '--pulls', dest='pulls', action='store_true',
        help='Open to the GitHub pull requests page')
    parser.add_argument('-t', '--test', dest='test', action='store_true',
        help='Print out the url instead of browsing to it')
    parser.add_argument('path', nargs='?',
        help='Open to this path in GitHub')
    return parser.parse_args()

def extract_github_address(f):
    url = ''
    content = f.readlines()
    for line in content:
        # These become indices of the substrings, and are only positive when
        # the substring exists.
        on_github_ssh = line.find('git@github.com')
        on_github_http = line.find('https://github.com/')
        if on_github_ssh > 0:
            project_url = line[on_github_ssh + len('git@github.com') + 1:]
            url = 'https://github.com/' + project_url.strip().replace('.git', '')
            # Break after the first match.
            break
        elif on_github_http > 0:
            project_url = line[on_github_http + len('https://github.com/'):]
            url = 'https://github.com/' + project_url.strip().replace('.git', '')
            # Break after the first match.
            break
    return url

def get_current_branch():
    """
    Returns the current git branch
    """
    stdout = execute_git_status()
    return get_branch_from_git_status_output(stdout)

def get_branch_from_git_status_output(stdout):
    """
    Returns the branch given output of the command
    `git status --short --branch`.
    """
    pattern = r'^## ([a-zA-Z0-9\-_]+)'
    match = re.match(pattern, stdout)
    if match:
        return match.groups()[0]

def execute_git_status():
    """
    Returns the stdout of the command `git status --short --branch`.
    """
    (stdout, stderr) = run_shell_command('git status --short --branch')
    return stdout

def run_shell_command(command):
    """
    Runs `command` in a shell, returning any output.
    """
    p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE,
            stdout=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    return (stdout, stderr)

def main():
    args = parse_arguments()

    # Check each directory for a .git folder, from current working directory
    # to the root.
    current_dir = os.getcwd()
    under_git = False
    project_root = current_dir
    while not under_git and not os.path.ismount(current_dir):
        git_config_path = os.path.join(current_dir, '.git', 'config')
        under_git = os.path.isfile(git_config_path)
        current_dir = os.path.dirname(current_dir)
        project_root = current_dir

    if not under_git:
        print 'This directory does not appear to be under git versioning.'
        sys.exit(0)
    else:
        with open(git_config_path) as f:
            base_url = extract_github_address(f)
            url = base_url
            branch = get_current_branch()
            if not base_url:
                print 'Aw, this project is not on GitHub.'
                sys.exit(0)

            if branch != 'master':
                url = base_url + '/tree/%s' % branch

            if args.issues:
                url = base_url + '/issues/'

            if args.pulls:
                url = base_url + '/pulls/'

            if args.commits:
                url = base_url + '/commits/%s' % branch

            if args.path:
                real_path = os.path.realpath(args.path)
                project_path = os.path.relpath(real_path, project_root)

                # Trim off the first item, which is the project's directory
                path = os.path.sep.join(project_path.split(os.path.sep)[1:])
                posix_path = path.replace(os.path.sep, posixpath.sep)
                url = base_url + '/tree/%s' % branch + '/' + posix_path

            if args.test:
                print 'GitHub url:'
                print '\t' + url
            else:
                webbrowser.open(url)

if __name__ == '__main__':
    main()

