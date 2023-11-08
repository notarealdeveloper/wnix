#!/usr/bin/env python3

__all__ = ['main']

import sys
import argparse
import subprocess

TYPES = ['pdf', 'image', 'url', 'html']

def infer_ext_from_path(path):
    ext = path.split('.')[-1]
    return ext

def infer_ext_from_bytes(bytes):
    import fleep
    info = fleep.get(bytes)
    exts = set(info.extension)
    for ext in {'png', 'jpg', 'pdf'}:
        if ext in exts:
            return ext
    return None

def ext_to_type(ext):
    if ext in {'jpg', 'png'}:
        return 'image'
    return ext

def die(msg=None):
    print(f"usage: input <type> <file>", file=sys.stderr)
    if msg:
        print(f" * error: {msg}", file=sys.stderr)
    sys.exit(1)

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser('input')
    parser.add_argument('type', nargs='?', choices=TYPES)
    args = parser.parse_args(argv)

    if args.type:
        import shutil
        cmd = f'input-{args.type}'
        if not shutil.which(cmd):
            die(f"No such command: {cmd}")
        proc = subprocess.run([cmd, *sys.argv[2:]])
    else:
        # type not passed, infer it from byte stream ;)
        bytes = sys.stdin.buffer.read()
        ext = infer_ext_from_bytes(bytes)
        args.type = ext_to_type(ext)
        if args.type is None:
            die(f"could not infer ext from bytes")
        cmd = f'input-{args.type}'
        proc = subprocess.Popen([cmd, *sys.argv[2:]], stdin=subprocess.PIPE)
        proc.communicate(bytes)

if __name__ == '__main__':
    main(sys.argv[1:])