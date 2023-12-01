#!/usr/bin/env python3

__all__ = ['main']

import os
import re
import sys
import shlex
import subprocess
import argparse

def run(cmd, input):
    p = subprocess.Popen(shlex.quote(cmd), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    stdout, stderr = p.communicate(input.encode())
    return stdout.decode()

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser('sort2')
    parser.add_argument('key')
    parser.add_argument('-c', '--cmd', type=str, default=None)
    parser.add_argument('-d', '--debug', action='store_true')
    args = parser.parse_args(argv)

    from embd import List, Dict

    lines = sys.stdin.read().splitlines()

    if args.cmd:
        qs = [run(args.cmd, line) for line in lines]
    else:
        qs = lines

    qs = {l:q for l,q in zip(lines, qs)}

    q = Dict(qs)
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
