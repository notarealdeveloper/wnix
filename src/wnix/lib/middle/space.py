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
    'shape',
    'Space',
]

import wnix
import numpy as np

def think(arg, space=None):
    if space is None:
        space = Space()
    return space.think(arg)

def shape(space=None):
    if space is None:
        space = Space()
    return space.embed.shape()

class Space:

    """ An embedding space """

    def __init__(self, embed=None, cache=None):
        self.embed = embed or wnix.embed.EmbedDefault()
        self.cache = cache or wnix.cache.CacheDefault()
        self.cache.namespace(self.embed.namespace())

    def think(self, arg):
        if isinstance(arg, (str, bytes)):
            return self.get(arg)
        if isinstance(arg, (list, tuple, set)):
            return np.stack([self.get(a) for a in arg])
        if isinstance(arg, dict):
            keys = list(arg.keys())
            vals = list(arg.values())
            embs = self.gets(vals)
            return dict(zip(keys, embs))
        raise TypeError(f"Can't think about {arg.__class__.__name__}: {arg!r}")

    def gets(self, blobs):
        embeds = {}
        todos = {}
        for n, blob in enumerate(blobs):
            try:
                embeds[n] = self.load(blob)
            except:
                todos[n] = blob
        ns = list(todos.keys())
        bs = list(todos.values())
        es = self.embed(bs)
        for n, b, e in zip(ns, bs, es):
            embeds[n] = e
            self.save(b, e)
        return np.stack([e for n,e in sorted(embeds.items())])

    def get(self, blob):
        try:
            embed = self.load(blob)
            return embed
        except:
            embed = self.embed(blob)
            self.save(blob, embed)
            return embed

    def save(self, blob, embed):
        bytes = wnix.tensor_to_bytes(embed)
        self.cache.save(blob, bytes)

    def load(self, blob):
        bytes = self.cache.load(blob)
        return wnix.bytes_to_tensor(bytes)
