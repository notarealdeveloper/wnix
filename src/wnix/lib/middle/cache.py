"""
    Interface for caching pre-computed embeddings.
"""

__all__ = [
    'CacheDefault',
    'CacheSha1',
]

import os
import hashlib
from functools import lru_cache

import assure
import wnix


class CacheSha1:

    """ Content addressable memory, inspired by git. """

    @staticmethod
    def default_root():
        return os.path.join(os.getenv('HOME'), '.cache', 'wnix')

    def __init__(self, name=None, *, root=default_root()):
        self.root = root
        self.name = name

    def namespace(self, name=None):
        if name is None:
            return self.name
        else:
            self.name = name
            return self

    @property
    def blob(self):
        return os.path.join(self.root, self.name, 'blob')

    @property
    def tree(self):
        return os.path.join(self.root, self.name, 'tree')

    def have(self, blob):
        return os.path.exists(self.path(blob))

    def path(self, blob):
        os.makedirs(self.blob, exist_ok=True)
        return os.path.join(self.blob, self.hash(blob))

    def save(self, blob, bytes):
        path = self.path(blob)
        with open(path, 'wb') as fp:
            fp.write(assure.bytes(bytes))

    def load(self, blob) -> bytes:
        path = self.path(blob)
        with open(path, 'rb') as fp:
            return assure.bytes(fp.read())

    def hash(self, blob):
        return self.hash_bytes(self.encode(blob))

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

CacheDefault = CacheSha1
