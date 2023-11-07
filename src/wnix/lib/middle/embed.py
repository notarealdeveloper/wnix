"""
Turn software 1.0 types (e.g., text)
into software 2.0 types (e.g., vect)

The functions here are implemented as classes,
for the same reasons that neural networks are.
"""

__all__ = [
    'EmbedDefault',
    'EmbedFlag',
]

class EmbedFlag:

    from functools import lru_cache

    SIZES = {'small', 'base', 'large'}

    @classmethod
    @lru_cache(maxsize=1)
    def load_model(cls, name):
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer(name)
        return model

    def __init__(self, size='large'):
        if size not in self.SIZES:
            raise ValueError(f"size must be one of: {self.SIZES}")
        self.name = f"BAAI/bge-{size}-en-v1.5"

    @property
    def model(self):
        # lazily load model
        try:
            return self._model
        except:
            self._model = self.load_model(self.name)
            return self._model

    def __call__(self, text, normalize=False):
        # the large flag model has a crazy non-constant embedding size
        # depending on whether or not we feed it a token length string
        return self.model.encode(text, normalize_embeddings=normalize)

EmbedDefault = EmbedFlag
