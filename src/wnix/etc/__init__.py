__all__ = [
    'cat',
    'get',
]

import importlib.resources

def cat(name):
    return importlib.resources.read_text('wnix.etc', name)

def get(name):
    return cat(name).strip().splitlines()

