#!/usr/bin/env python3

__all__ = ['main']

import os
import sys
import argparse

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser('grep2')
    parser.add_argument('keys')
    parser.add_argument('type', nargs='?', help="Context information")
    parser.add_argument('-n', '--num', type=int)
    parser.add_argument('-w', '--whole')
    parser.add_argument('-k', '--keysep', default=',')
    parser.add_argument('-t', '--typesep', default=':')
    parser.add_argument('-d', '--debug', action='store_true')
    parser.add_argument('-o', '--only', action='store_true')

    args = parser.parse_args(argv)

    if args.whole:
        queries = [sys.stdin.read()]
    else:
        queries = sys.stdin.read().splitlines()

    if os.path.exists(args.keys):
        keys = open(args.keys).read().splitlines()
    else:
        keys = [a.strip() for a in args.keys.split(args.keysep)]

    if len(keys) == 1:
        keys.append('other')

    if args.type:
        dict = {key: f"{args.type}{args.typesep}{key}" for key in keys}
    else:
        dict = {key: key for key in keys}

    from wnix import Grep
    grep = Grep(queries, dict)
    if args.debug:
        print('dict:\n', dict, '\n', '='*42, file=sys.stderr)
        print('grep:\n', grep, '\n', '='*42, file=sys.stderr)
    output = grep.csv(n=args.num)
    print(output)

if __name__ == '__main__':
    main(sys.argv[1:])
