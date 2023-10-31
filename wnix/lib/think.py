"""
Turns text into vectors.

The functions here are implemented as classes,
for the same reasons that neural networks are.
"""

__all__ = [
    'Flag',
]

class Flag:

    from functools import lru_cache

    SIZES = {'small', 'base', 'large'}

    @classmethod
    @lru_cache(maxsize=1)
    def load_model(cls, name):
        from sentence_transformers import SentenceTransformer
        return SentenceTransformer(name)

    def __init__(self, size='large'):
        if size not in self.SIZES:
            raise ValueError(f"size must be one of: {self.SIZES}")
        self.name = f"BAAI/bge-{size}-en-v1.5"
        self.model = self.load_model(self.name)

    def __call__(self, text, normalize=False):
        return self.model.encode(text, normalize_embeddings=normalize)
