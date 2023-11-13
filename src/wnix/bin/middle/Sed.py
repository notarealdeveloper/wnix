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
    parser.add_argument('replace')
    args = parser.parse_args(argv)

    search = get_values(args.search)
    replace = get_values(args.replace)
    inputs = sys.stdin.read().splitlines()

    outputs = wnix.Sed(inputs, search, replace)
    output = '\n'.join(outputs[0])
    print(output)

if __name__ == '__main__':
    main(sys.argv[1:])
