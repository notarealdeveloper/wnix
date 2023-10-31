#!/usr/bin/env python3

import sys
import argparse

def main():
    MODELS = ['small', 'base', 'large']

    parser = argparse.ArgumentParser('think')
    parser.add_argument('path', nargs='?')
    parser.add_argument('-s', '--size', choices=MODELS, default='small')
    args = parser.parse_args()

    import wnix
    model = wnix.think.Flag(args.size)

    if args.path:
        text = open(args.path).read()
    else:
        text = sys.stdin.read()

    embed = model(text)
    embed = embed.tobytes()
    sys.stdout.buffer.write(embed)

if __name__ == '__main__':
    main()
