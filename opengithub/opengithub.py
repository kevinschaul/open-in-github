#! /usr/bin/env python

import argparse
import os

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--issues', dest='issues', action='store_true',
        help='Open to the GitHub issues page')
    return parser.parse_args()

def main():
    args = parse_arguments()
    print args

if __name__ == '__main__':
    main()

