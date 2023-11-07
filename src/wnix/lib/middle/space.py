"""
Embeddings
* automatically cached by content
* persisted between processes 
* namespaced by model and args
* support for tokenizer independent names
"""

__all__ = [
    'think',
    'Space',
]

import wnix
import numpy as np

def think(arg, space=None):
    if space is None:
        space = Space()
    return space.think(arg)

class Space:

    def __init__(self, embed=None, cache=None):
        self.embed = embed or wnix.embed.EmbedDefault()
        self.cache = cache or wnix.cache.CacheDefault()

    def think(self, arg):
        if isinstance(arg, str):
            return self.get(arg)
        if isinstance(arg, (list, tuple, set)):
            return np.stack([self.get(key) for key in arg])
        raise TypeError(f"Not sure how to think about {arg.__class__.__name__}: {arg!r}")

    def get(self, arg):
        embed = self.load(blob)
        if embed is not None:
            return embed
        embed = self.embed(blob)
        self.save(blob, embed)
        return embed

    def save(self, blob, embed):
        bytes = wnix.tensor_to_bytes(embed)
        self.cache.save(blob, bytes)

    def load(self, blob):
        bytes = self.cache.load(blob)
        if bytes is not None:
            return wnix.bytes_to_tensor(bytes)
        return None
