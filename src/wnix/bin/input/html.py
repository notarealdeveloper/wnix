#!/usr/bin/env python3

__all__ = ['main']

import sys
import bs4
import argparse

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser('input-html')
    parser.add_argument('path', nargs='?')
    args = parser.parse_args(argv)

    if args.path is not None:
        html = open(args.path).read()
    else:
        html = sys.stdin.buffer.read().decode()

    soup = bs4.BeautifulSoup(html, 'html.parser')

    print(soup.text)

if __name__ == '__main__':
    main()
