#!/usr/bin/env python3

__all__ = ['main']

import os
import sys
import argparse

import wnix

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser('what')
    parser.add_argument('file')
    args = parser.parse_args(argv)

    if args.file and os.path.exists(args.file):
        keys = open(args.file).read().splitlines()
    else:
        keys = sys.argv[1:]

    q = wnix.stdin_to_tensor()
    ranks = wnix.what(q, keys)
    output = '\n'.join(ranks)
    print(output)

if __name__ == '__main__':
    main(sys.argv[1:])
