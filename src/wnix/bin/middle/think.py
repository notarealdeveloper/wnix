#!/usr/bin/env python3

__all__ = ['main']

import os
import sys
import argparse
import wnix

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser('think')
    parser.add_argument('file', nargs='?')
    parser.add_argument('-l', '--lines', action='store_true')
    args = parser.parse_args(argv)

    if not args.file:
        input = sys.stdin.read()
    else:
        input = open(args.file).read()

    if args.lines:
        texts = input.splitlines()
    else:
        texts = [input]

    space = wnix.Space()

    outputs = []
    for text in texts:
        output = space.think(text)
        outputs.append(output)

    import numpy as np
    tensor = np.stack(outputs)

    if os.isatty(sys.stdout.fileno()):
        print(tensor)
    else:
        sys.stdout.buffer.write(wnix.tensor_to_bytes(output))

if __name__ == '__main__':
    main(sys.argv[1:])