#!/usr/bin/env python

__all__ = ['main']

import sys
import argparse

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser('rootfs')
    parser.add_argument('--show', action='store_true', help="Show root directory")
    parser.add_argument('--list', action='store_true', help="Run ls on root directory")
    parser.add_argument('--find', action='store_true', help="Run find on root directory")
    # TODO: make --list and --find take an argument
    args = parser.parse_args(argv)

    if [args.show, args.list, args.find].count(True) > 1:
        print(f"at most one of --root, --list, --find allowed", file=sys.stderr)
        sys.exit(1)
    if [args.show, args.list, args.find].count(True) == 0:
        args.show = True
        sys.exit(1)

    import wnix

    if args.show:
        print(wnix.root())
    if args.list:
        print(wnix.list('/'))
    if args.find:
        print(wnix.find('/'))

if __name__ == '__main__':
    main(sys.argv[1:])
