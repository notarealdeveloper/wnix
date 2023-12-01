#!/usr/bin/env python3

__all__ = ['main']

import os
import re
import sys
import argparse
import subprocess

def run(cmd, input):
    p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    input = input.encode() if isinstance(input, str) else input
    stdout, stderr = p.communicate(input)
    return stdout.decode()

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser('sort2')
    parser.add_argument('key')
    parser.add_argument('-c', '--cmd', type=str, default=None)
    parser.add_argument('-p', '--paths', action='store_true', help="Interpret inputs as paths")
    parser.add_argument('-i', '--input', action='store_true', help="Short for '-p -c input'")
    parser.add_argument('-d', '--debug', action='store_true')
    args = parser.parse_args(argv)

    if args.input:
        args.cmd = 'input'
        args.paths = True

    from embd import List, Dict

    lines = sys.stdin.read().splitlines()

    q = {l: l for l in lines}

    if args.paths:
        q = {k: open(v, 'rb').read() for k,v in q.items()}

    if args.cmd:
        q = {k: run(args.cmd, v) for k,v in q.items()}

    q = Dict(q)
    k = List([args.key])
    s = q @ k
    if args.debug:
        print(f'=== q ===')
        import json
        print(json.dumps(q.o, indent=2))
        print(q)
        print(f'=== k ===')
        print(k)
        print(f'=== s ===')
        print(s)
        sys.exit(0)

    o = s[args.key].sort_values(ascending=False).index.tolist()
    for l in o:
        print(l)

if __name__ == '__main__':
    main(sys.argv[1:])
