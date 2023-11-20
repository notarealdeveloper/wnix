#!/usr/bin/env python

__all__ = ['main']

import sys
import argparse

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser('wnix')
    parser.add_argument(
        'cmd',
        nargs='?',
        default='pwd',
        choices=['pwd', 'ls', 'find'],
        help="Command to run",
    )
    parser.add_argument('opts', nargs='?', default='')
    args = parser.parse_args(argv)

    import wnix
    if args.cmd == 'pwd':
        results = [wnix.pwd()]
    if args.cmd == 'ls':
        results = wnix.ls(args.opts)
    if args.cmd == 'find':
        results = wnix.find(args.opts)
    if args.cmd == 'cat':
        results = wnix.cat(args.opts)

    for result in results:
        print(str(result))

if __name__ == '__main__':
    main(sys.argv[1:])
