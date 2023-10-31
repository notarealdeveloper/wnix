"""
Turns text into vectors.

The functions here are implemented as classes,
for the same reasons that neural networks are.
"""

__all__ = [
    'FlagEmbed',
]

class FlagEmbed:

    from functools import lru_cache

    SIZES = {'small', 'base', 'large'}

    @classmethod
    @lru_cache(maxsize=1)
    def load_model(cls, size):
        if size not in cls.SIZES:
            raise ValueError(f"size must be one of: {cls.SIZES}")
        from sentence_transformers import SentenceTransformer
        return SentenceTransformer(f"BAAI/bge-{size}-en-v1.5")

    def __init__(self, size='large'):
        self.model = self.load_model()

    def __call__(self, text, normalize=False):
        return self.model.encode(text, normalize_embeddings=normalize)
