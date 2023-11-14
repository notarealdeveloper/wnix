#!/usr/bin/env python

__all__ = ['main']

import sys
import argparse

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser('rootfs')
    parser.add_argument('--show', action='store_true',  help="Show root directory")
    parser.add_argument('--list', type=str, default=None, help="Run ls on a directory")
    parser.add_argument('--find', type=str, default=None, help="Run find on a directory")
    args = parser.parse_args(argv)

    if [args.show, args.list, args.find].count(True) > 1:
        print(f"at most one of --show, --list, --find allowed", file=sys.stderr)
        sys.exit(1)
    if [args.show, args.list, args.find].count(True) == 0:
        args.show = True

    import wnix

    if args.show:
        results = [wnix.root()]
    if args.list:
        results = wnix.list(args.list)
    if args.find:
        results = wnix.find(args.find)

    for result in results:
        print(str(result))

if __name__ == '__main__':
    main(sys.argv[1:])
