#!/usr/bin/env python3

__all__ = ['main']

import os
import sys
import argparse
import subprocess

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser('cat2')
    parser.add_argument('files', nargs='*')
    args = parser.parse_args(argv)

    streams = []
    if not os.isatty(sys.stdin.fileno()):
        stream = sys.stdin.buffer
        streams.append(stream)

    for file in args.files:
        stream = open(file, 'rb')
        streams.append(stream)

    for stream in streams:
        blob = stream.read()
        proc = subprocess.Popen(["input"], stdin=subprocess.PIPE)
        proc.communicate(blob)

if __name__ == '__main__':
    main(sys.argv[1:])
