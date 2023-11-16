#!/usr/bin/env python3

__all__ = ['main']

import os
import sys
import argparse

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser('lines')
    parser.add_argument('inputs', nargs='+')
    args = parser.parse_args(argv)

    for input in args.inputs:
        print(input)

if __name__ == '__main__':
    main(sys.argv[1:])
