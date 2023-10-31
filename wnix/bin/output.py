#!/usr/bin/env python3

import sys
import argparse

def main():
    parser = argparse.ArgumentParser('output')
    parser.add_argument(
        '-o', '--to', nargs='?',
        choices=['print', 'bytes', 'json', 'pickle'],
        default='print'
    )

    # a tensor comes from stdin, in exactly one format
    import wnix
    args = parser.parse_args()
    array = wnix.stdin_to_tensor()

    # a tensor goes to stdout, in any format we want
    if args.to == 'print':
        wnix.output_print(array)
    elif args.to == 'bytes':
        wnix.output_bytes(array)
    elif args.to == 'json':
        wnix.output_json(array)
    elif args.to == 'pickle':
        wnix.output_pickle(array)
    else:
        raise TypeError

if __name__ == '__main__':
    main()
