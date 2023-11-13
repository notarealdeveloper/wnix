#!/usr/bin/env python3

__all__ = ['main']

import os
import sys
import argparse

import wnix

def get_values(arg):
    if os.path.exists(arg):
        return open(arg).read().splitlines()
    else:
        return arg.split()

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser('Grep')
    parser.add_argument('search')
    args = parser.parse_args(argv)

    search = get_values(args.search)

    inputs = sys.stdin.read().splitlines()
    matches = wnix.Grep(inputs, search)
    output = '\n'.join(matches[0])
    print(output)

if __name__ == '__main__':
    main(sys.argv[1:])
