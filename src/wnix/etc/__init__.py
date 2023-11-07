__all__ = [
    'get_text',
    'get_type',
]

import importlib.resources

def get_text(name):
    return importlib.resources.read_text('wnix.etc', name)

def get_type(name):
    return get_text(name).strip().splitlines()

