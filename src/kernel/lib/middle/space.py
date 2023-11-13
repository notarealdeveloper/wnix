""" space
    =====
    compute embeddings that are
    * automatically cached by content
    * persisted between processes 
    * namespaced by model and args
    * supports model independent name assignment
"""

__all__ = [
    'think',
    'Space',
]

import kernel
import numpy as np

def think(arg, space=None):
    if space is None:
        space = Space()
    return space.think(arg)

class Space:

    """ An embedding space """

    def __init__(self, embed=None, cache=None):
        self.embed = embed or kernel.embed.EmbedDefault()
        self.cache = cache or kernel.cache.CacheDefault()
        self.cache.namespace(self.embed.namespace())

    def think(self, arg):
        if isinstance(arg, str):
            return self.get(arg)
        if isinstance(arg, (list, tuple, set)):
            return np.stack([self.get(blob) for blob in arg])
        raise TypeError(f"Not sure how to think about {arg.__class__.__name__}: {arg!r}")

    def get(self, blob):
        try:
            embed = self.load(blob)
            return embed
        except:
            embed = self.embed(blob)
            self.save(blob, embed)
            return embed

    def save(self, blob, embed):
        bytes = kernel.tensor_to_bytes(embed)
        self.cache.save(blob, bytes)

    def load(self, blob):
        bytes = self.cache.load(blob)
        return kernel.bytes_to_tensor(bytes)
