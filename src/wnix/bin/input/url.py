#!/usr/bin/env python3

__all__ = ['main']

import sys
import argparse

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser('input-url')
    parser.add_argument('url', nargs='?')
    args = parser.parse_args(argv)

    if args.url is not None:
        url = args.url
    else:
        url = sys.stdin.buffer.read().decode().strip()

    import wnix
    text = wnix.url_to_html(url)
    print(text)

if __name__ == '__main__':
    main(sys.argv[1:])
