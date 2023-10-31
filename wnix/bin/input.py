#!/usr/bin/env python3

import os
import sys
import argparse

import wnix

TYPES = ['pdf']

def main():
    parser = argparse.ArgumentParser('input')
    parser.add_argument('path', nargs='?')
    parser.add_argument('-t', '--type', choices=TYPES, default='pdf')
    args = parser.parse_args()

    if args.path is not None:
        file = open(args.path, 'rb')
    else:
        file = sys.stdin.buffer

    if args.type == 'pdf':
        text = wnix.pdf_to_text(file)
    else:
        raise TypeError(f"Type must be one of: {TYPES}")

    # write to stdout
    sys.stdout.write(text)

if __name__ == '__main__':
    main()
