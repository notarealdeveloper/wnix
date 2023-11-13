#!/usr/bin/env python3

__all__ = ['main']

import sys
import argparse

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser('input-image')
    parser.add_argument('query', nargs='?')
    args = parser.parse_args(argv)

    import wnix
    file = sys.stdin.buffer

    if args.query is None:
        text = wnix.image_to_text(file)
    else:
        text = wnix.image_and_text_to_text(file, args.query)
    print(text)

if __name__ == '__main__':
    main(sys.argv[1:])
