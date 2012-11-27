#! /usr/bin/env python

import argparse
import os
import sys
import webbrowser

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--issues', dest='issues', action='store_true',
        help='Open to the GitHub issues page')
    parser.add_argument('-t', '--test', dest='test', action='store_true',
        help='Print out the url instead of browsing to it')
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
            url = 'https://github.com/' + project_url.strip().strip('.git')
        elif on_github_http > 0:
            project_url = line[on_github_http + len('https://github.com/'):]
            url = 'https://github.com/' + project_url.strip().strip('.git')
    return url

def main():
    args = parse_arguments()

    # Check each directory for a .git folder, from current working directory
    # to the root.
    current_dir = os.getcwd()
    under_git = False
    while not under_git and current_dir != '/': #TODO This is Unix-specific
        git_config_path = current_dir + '/.git/config'
        under_git = os.path.isfile(git_config_path)
        current_dir = os.path.dirname(current_dir)

    if not under_git:
        print 'This directory does not appear to be under git versioning.'
        sys.exit(0)
    else:
        with open(git_config_path) as f:
            url = extract_github_address(f)
            print url
            if not url:
                print 'Aw, this project is not on GitHub.'
                sys.exit(0)
            if args.issues:
                url += '/issues/'
            if args.test:
                print 'GitHub url:'
                print '\t' + url
            else:
                webbrowser.open(url)

if __name__ == '__main__':
    main()

