#!/usr/bin/env python3

__all__ = ['main']

import os
import sys
import argparse
import itertools

def get_values(arg):
    if os.path.exists(arg):
        return open(arg).read().splitlines()
    else:
        return arg.split()

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser('product')
    parser.add_argument('inputs', nargs='+')
    args = parser.parse_args(argv)

    lists = [get_values(input) for input in args.inputs]

    for list in itertools.product(*lists):
        print(' '.join(list))

if __name__ == '__main__':
    main(sys.argv[1:])
