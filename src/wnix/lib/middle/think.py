__all__ = [
    'think',
]

from .space import Space

def think(arg, space=None, embed=None, cache=None):
    if space is None:
        space = Space(embed, cache)
    if isinstance(arg, str):
        return space.think(arg)
    if isinstance(arg, (list, tuple, set)):
        import numpy as np
        return np.stack([space.think(key) for key in arg])
    raise TypeError(f"Not sure how to think about {arg.__class__.__name__}: {arg!r}")

