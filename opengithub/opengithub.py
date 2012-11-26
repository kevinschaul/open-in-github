#! /usr/bin/env python

import argparse
import os
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
            url = 'https://github.com/' + project_url
        elif on_github_http > 0:
            project_url = line[on_github_http + len('https://github.com/'):]
            url = 'https://github.com/' + project_url
    return url

def main():
    args = parse_arguments()
    cwd = os.getcwd()
    git_config_path = cwd + '/.git/config'
    under_git = os.path.isfile(git_config_path)
    if not under_git:
        print 'This directory does not appear to be under git versioning.'
    else:
        with open(git_config_path) as f:
            url = extract_github_address(f)
            if not url:
                print 'Aw, not on GitHub.'
                sys.exit(1)
            if args.test:
                print 'GitHub url:'
                print '\t' + url
            else:
                webbrowser.open(url)

if __name__ == '__main__':
    main()

