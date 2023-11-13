#!/usr/bin/env python3

__all__ = ['main']

import os
import sys
import argparse

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser('output')
    parser.add_argument(
        'to',
        nargs='?',
        choices=['string', 'bytes', 'json', 'pickle'],
        default='string'
    )

    # a tensor comes from stdin, in exactly one format
    import wnix
    args = parser.parse_args(argv)
    tensor = wnix.stdin_to_tensor()

    # a tensor goes to stdout, in any format we want
    if   args.to == 'string':
        output = wnix.tensor_to_string(tensor)
        print(output)
    elif args.to == 'bytes':
        output = wnix.tensor_to_bytes(tensor)
        sys.stdout.buffer.write(output)
    elif args.to == 'json':
        output = wnix.tensor_to_json(tensor)
        print(output)
    elif args.to == 'pickle':
        output = wnix.tensor_to_pickle(tensor)
        sys.stdout.buffer.write(output)
    else:
        raise TypeError

if __name__ == '__main__':
    main(sys.argv[1:])
