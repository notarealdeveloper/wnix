"""
    Interface for caching pre-computed embeddings.
"""

__all__ = [
    'CacheDefault',
    'CacheDisk',
]

import os
import hashlib
from functools import lru_cache

import wnix


class CacheDisk:

    """ Content addressable memory, inspired by git. """

    @staticmethod
    def default_root():
        return os.path.join(os.getenv('HOME'), '.cache', 'wnix')

    def __init__(self, name = 'embed', *, root=default_root()):
        self.root = root
        self.blob = os.path.join(self.root, name, 'blob')
        self.tree = os.path.join(self.root, name, 'tree')

        os.makedirs(self.root, exist_ok=True)
        os.makedirs(self.blob, exist_ok=True)
        os.makedirs(self.tree, exist_ok=True)

    def have(self, blob):
        return os.path.exists(self.path(blob))

    def path(self, blob):
        return os.path.join(self.blob, self.hash(blob))

    def save(self, blob, bytes):
        path = self.path(blob)
        with open(path, 'wb') as fp:
            fp.write(bytes)

    def load(self, blob) -> bytes:
        if self.have(blob):
            return self(blob)
        return None

    def hash(self, blob):
        return self.hash_bytes(self.encode(blob))

    def __call__(self, blob):
        path = self.path(blob)
        with open(path, 'rb') as fp:
            return fp.read()

    @staticmethod
    @lru_cache
    def encode(blob):
        return blob.encode() if isinstance(blob, str) else blob

    @staticmethod
    @lru_cache
    def hash_bytes(blob):
        """ ensure we only cache content once, even if it arrives in
            one call as a unicode string, and in a later call as bytes.
        """
        if not isinstance(blob, bytes):
            raise TypeError(f"blob has type {blob.__class__.__name__!r}")
        return hashlib.sha1(blob).hexdigest()

CacheDefault = CacheDisk
