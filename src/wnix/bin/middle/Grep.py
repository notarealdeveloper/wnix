#!/usr/bin/env python3

__all__ = ['main']

import os
import sys
import argparse

from wnix import grep, format_grep

def get_values(arg):
    if os.path.exists(arg):
        return open(arg).read().splitlines()
    else:
        return [a.strip() for a in arg.split('|')]

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser('Grep')
    parser.add_argument('keys')
    parser.add_argument('-n', '--num')
    parser.add_argument('-w', '--whole')
    args = parser.parse_args(argv)

    if args.whole:
        queries = [sys.stdin.read()]
    else:
        queries = sys.stdin.read().splitlines()

    keys = get_values(args.keys)
    g = grep(queries, keys)
    output = format_grep(g, n=args.num)
    print(output)

if __name__ == '__main__':
    main(sys.argv[1:])
