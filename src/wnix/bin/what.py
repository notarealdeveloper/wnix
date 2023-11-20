#!/usr/bin/env python3

__all__ = ['main']

import os
import sys

def main(argv=None):
    import argparse
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser('What')
    parser.add_argument('file')
    parser.add_argument('-n', type=int, default=1)
    args = parser.parse_args(argv)

    if args.file and os.path.exists(args.file):
        keys = open(args.file).read().splitlines()
    else:
        keys = sys.argv[1:]

    import embd
    import wnix
    space = embd.Space()
    shape = space.embed.shape()

    # receive a tensor across a pipe! 🎉
    Q = embd.stdin_to_tensor().reshape((-1, shape))
    output = wnix.Grep(Q, keys).fmt_what(n=args.n)
    print(output)

if __name__ == '__main__':
    main(sys.argv[1:])
