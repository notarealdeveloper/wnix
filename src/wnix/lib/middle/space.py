__all__ = [
    'Space',
]

import wnix

class Space:

    def __init__(self, embed=None, cache=None):
        self.embed = embed or wnix.embed.EmbedDefault()
        self.cache = cache or wnix.cache.CacheDefault()

    def think(self, blob):
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
