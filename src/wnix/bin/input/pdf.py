#!/usr/bin/env python3

__all__ = ['main']

import sys
import argparse

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser('input-pdf')
    parser.add_argument('path', nargs='?')
    args = parser.parse_args(argv)

    if args.path is not None:
        file = open(args.path, 'rb')
    else:
        file = sys.stdin.buffer

    import wnix
    text = wnix.pdf_to_text(file)
    print(text)

if __name__ == '__main__':
    main(sys.argv[1:])
