#!/usr/bin/env python3

__all__ = ['main']

import os
import re
import sys
import argparse

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser('grep2')
    parser.add_argument('keys', nargs='?')
    parser.add_argument('-n', '--num', type=str, default='1')
    parser.add_argument('-w', '--whole')
    parser.add_argument('-f', '--file', type=str, default=None)
    parser.add_argument('-d', '--debug', action='store_true')
    parser.add_argument('-o', '--only', type=str)
    parser.add_argument('-s', '--sims', type=str, default='a(a) @ b')
    parser.add_argument('-q', '--only-first', action='store_true')
    parser.add_argument('-v', '--invert-match', action='store_true')
    parser.add_argument('-t', '--type', default=None)
    parser.add_argument('-T', '--typesep', default=':')
    parser.add_argument('-K', '--keysep', default=',')
    parser.add_argument('-A', '--after', type=int, default=0)
    parser.add_argument('-B', '--before', type=int, default=0)
    parser.add_argument('-C', '--context', type=int, default=0)
    args = parser.parse_args(argv)

    if args.num == 'all':
        args.num = None
    else:
        args.num = int(args.num)

    before = after = 0
    if args.context:
        before = after = args.context
    if args.before:
        before = args.before
    if args.after:
        after = args.after

    if args.whole:
        queries = [sys.stdin.read()]
    else:
        queries = sys.stdin.read().splitlines()

    # handle context arguments
    qdict = {}
    for n in range(len(queries)):
        query = queries[n]
        window = queries[n-before:n+after+1]
        if len(window) == 0:
            continue
        qdict[query] = '\n'.join(window)
    queries = qdict

    if os.path.exists(args.keys):
        keys = open(args.keys).read().splitlines()
    elif args.file:
        keys = open(args.file).read().splitlines()
    else:
        keys = [a.strip() for a in args.keys.split(args.keysep)]

    if args.only_first:
        args.only = keys[0]

    if len(keys) == 1:
        keys.append('other')

    if args.type:
        dict = {key: f"{args.type}{args.typesep}{key}" for key in keys}
    else:
        dict = {key: key for key in keys}

    from wnix import Grep
    grep = Grep(queries, dict, sims=args.sims)
    if args.debug:
        print('dict:\n', dict, '\n', '='*42, file=sys.stderr)
        print('grep:\n', grep, '\n', '='*42, file=sys.stderr)
    output = grep.csv(n=args.num)

    if args.only:
        lines = output.splitlines()
        # filter to lines that start with the provided regex
        is_match = lambda line: re.match(f"^{args.only}.*", line.split(':')[0])
        orig_line = lambda line: line[line.index(':')+1:]
        if args.invert_match:
            is_good = lambda line: not is_match(line)
        else:
            is_good = lambda line: is_match(line)
        lines = [orig_line(line) for line in lines if is_good(line)]
        output = '\n'.join(lines)

    print(output)

if __name__ == '__main__':
    main(sys.argv[1:])
