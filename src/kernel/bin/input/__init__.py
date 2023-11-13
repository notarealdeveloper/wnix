#!/usr/bin/env python3

__all__ = ['main']

import os
import sys
import shutil
import argparse
import subprocess


def infer_ext_from_path(path):
    ext = path.split('.')[-1]
    return ext


def infer_ext_from_bytes(bytes):

    # pdf, jpg, png
    import fleep
    info = fleep.get(bytes)
    exts = set(info.extension)
    for ext in {'png', 'jpg', 'pdf'}:
        if ext in exts:
            return ext

    # url
    import validators
    text = bytes.decode()
    if validators.url(text):
        return 'url'

    for s in ('<html', '<doctype', '<meta'):
        if s in text.lower():
            return 'html'

    raise TypeError

CMDS = {'pdf', 'image', 'url', 'html'}

EXT_TO_CMD = {
    'jpg': 'image',
    'png': 'image',
    'image': 'image',
    'pdf': 'pdf',
    'url': 'url',
    'html': 'html',
}

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser('input')
    parser.add_argument('input', nargs='?')
    parser.add_argument('-t', '--type', action='store_true')
    args = parser.parse_args(argv)

    if args.input is not None and os.path.exists(args.input):
        bytes = open(args.input, 'rb').read()
        ext = infer_ext_from_path(args.input)
        ext2 = infer_ext_from_bytes(bytes)
        assert ext == ext2, f"inference error: ext1={ext}, ext2={ext2}"
        cmd = EXT_TO_CMD[ext]
        del ext, ext2
        args = sys.argv[2:]
    elif args.input in CMDS:
        cmd = args.input
        bytes = sys.stdin.buffer.read()
        ext = infer_ext_from_bytes(bytes)
        cmd2 = EXT_TO_CMD[ext]
        assert cmd == cmd2, f"inference error: cmd1={cmd}, cmd2={cmd2}"
        args = sys.argv[2:]
    elif args.input is not None and not os.path.exists(args.input):
        bytes = sys.stdin.buffer.read()
        ext = infer_ext_from_bytes(bytes)
        cmd = EXT_TO_CMD[ext]
        args = sys.argv[1:]
    else:
        # input is not a command or a file, try to infer it from bytes
        bytes = sys.stdin.buffer.read()
        ext = infer_ext_from_bytes(bytes)
        cmd = EXT_TO_CMD[ext]
        args = sys.argv[2:]

    command = f'input-{cmd}'

    if cmd not in CMDS:
        print(f"could not infer input command", file=sys.stderr)
        sys.exit(1)

    if not shutil.which(command):
        print(f"bad command: {command}", file=sys.stderr)
        sys.exit(1)

    #proc = subprocess.run([command, *args])
    proc = subprocess.Popen([command, *args], stdin=subprocess.PIPE)
    proc.communicate(bytes)

if __name__ == '__main__':
    main(sys.argv[1:])
