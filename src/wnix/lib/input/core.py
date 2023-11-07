#!/usr/bin/env python3

__all__ = [
    'filelike_to_bytes',
]

def filelike_to_bytes(arg):
    import io
    import os
    import pathlib
    import builtins
    if isinstance(arg, io.IOBase):
        content = arg.read()
        if isinstance(content, str):
            bytes = content.encode()
        elif isinstance(content, builtins.bytes):
            bytes = content
        else:
            raise TypeError()
        return bytes
    if isinstance(arg, builtins.bytes):
        return arg
        bytes = open(path, 'rb').read()
        return bytes
    if isinstance(arg, pathlib.Path):
        arg = arg.to_posix()
    if os.path.exists(arg):
        bytes = open(arg, 'rb').read()
        return bytes
    cls = type(arg)
    raise FileNotFoundError(f"Could not cast to bytes: {cls.__name__!r}")

