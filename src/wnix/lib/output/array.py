
__all__ = [
    'ensure_vect',
    'ensure_vects',
    'ensure_rect',
    'ensure_rects',
]

import wnix
import numpy as np

def ensure_vect(arg):
    if isinstance(arg, str):
        a = wnix.think(arg)
    elif isinstance(arg, np.ndarray):
        assert arg.ndim == 1
        a = arg
    else:
        raise TypeError(arg)
    return a

def ensure_vects(*args):
    return [ensure_vect(arg) for arg in args]

def ensure_rect(arg):
    if isinstance(arg, str):
        a = wnix.think(arg)
        A = a[None, :]
    elif isinstance(arg, (list, tuple)):
        A = np.stack(ensure_vects(*arg))
    elif isinstance(arg, np.ndarray):
        assert arg.ndim == 2
        A = arg
    else:
        raise TypeError(arg)
    return A

def ensure_rects(*args):
    return [ensure_rect(arg) for arg in args]

