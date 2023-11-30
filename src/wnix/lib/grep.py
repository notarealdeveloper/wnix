__all__ = [
    'Attn',
    'Grep',
    'grep',
    'greps',
]

import assure
import embd

SIMILARITY_DEFINITIONS = [
    'a @ b',
    'a @ b(a)',
    'a @ b(b)',
    'a(a) @ b',
    'a(a) @ b(a)',
    'a(a) @ b(b)',
    'a(b) @ b',
    'a(b) @ b(a)',
    'a(b) @ b(b)',
]


class Attn:

    def __init__(self, queries, keys, *, sims='a @ b'):

        q = embd.promote(queries)
        k = embd.promote(keys)

        if sims not in self.sims_defs():
            raise ValueError(f"sims must be one of: {self.sims_defs()}")

        s = self.sims(q, k, sims)

        import numpy as np
        i = np.argsort(-s)

        self.queries = queries
        self.keys = keys
        self.q = q
        self.k = k
        self.s = s
        self.i = i

    @classmethod
    def all(cls, queries, keys, *, sims='a @ b', **kwds):
        """ Evaluate possible definitions of similarity """
        return [cls(queries, keys, sims=sims, **kwds) for sims in cls.sims_defs()]

    @classmethod
    def sims_defs(cls):
        return SIMILARITY_DEFINITIONS

    @classmethod
    def sims(cls, q, k, sims):
        return (lambda a,b: eval(sims))(q,k)

    def __repr__(self):
        return repr(self.s)


class Grep(Attn):

    def __init__(self, queries, keys, *, sims='a @ b', n=None):

        super().__init__(queries, keys, sims=sims)
        s = self.s
        i = self.i

        g = 0*s
        g.iloc[:, :] = s.columns.values[i]
        g.columns = list(range(1, len(g.columns)+1))
        g.columns.name = sims
        g = g.iloc[:, 0:n]

        # attributes
        self.i = i
        self.g = g

    def __repr__(self):
        return repr(self.g)

    def __getitem__(self, n):
        return self.g[n]

    def what(self, n=None):
        l = self.g.values.tolist()
        import numpy as np
        return np.array([a[:n] for a in l])

    def fmt_what(self, n=None):
        ll = self.what(n=n)
        l = [','.join(a) for a in ll]
        return '\n'.join(l)

    def fmt_grep(self, n=1):
        return self.csv(n=n)

    def csv(self, n=1):
        import pandas as pd
        g = self.g
        g = g.iloc[:, 0:n]
        qs = g.index.tolist()
        Ks = g.values
        lines = []
        for q,K in zip(qs,Ks):
            k = ','.join(K)
            line = f"{k}:{q}"
            lines.append(line)
        o = '\n'.join(lines)
        return o

    def tolist(self):
        return self.g.values.ravel().tolist()

    def intersect(self, s):
        return set(self.tolist()) & set(s)

grep = Grep
greps = Grep.all
