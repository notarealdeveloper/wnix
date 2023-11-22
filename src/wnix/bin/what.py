#!/usr/bin/env python3

__all__ = ['main']

import os
import sys

def main(argv=None):
    import argparse
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser('what')
    parser.add_argument('keys')
    parser.add_argument('-k', '--keysep', default=',')
    parser.add_argument('-n', '--num', type=int, default=1)
    args = parser.parse_args(argv)

    if os.path.exists(args.keys):
        keys = open(args.keys).read().splitlines()
    else:
        keys = [a.strip() for a in args.keys.split(args.keysep)]

    import embd
    import wnix
    space = embd.Space()
    shape = space.embed.shape()

    # receive a tensor across a pipe! 🎉
    Q = embd.stdin_to_tensor().reshape((-1, shape))
    output = wnix.Grep(Q, keys).fmt_what(n=args.num)
    print(output)

if __name__ == '__main__':
    main(sys.argv[1:])
