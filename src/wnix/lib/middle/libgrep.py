#!/usr/bin/env python3

__all__ = [
    'grep',
    'greps',
    'format_grep',
    'List',
    'Object',
]

import wnix
import assure
import itertools
import is_instance
import numpy as np
import pandas as pd

def embed(o):
    return wnix.think(o)

def series(o):
    if isinstance(o, pd.Series):
        return o
    if isinstance(o, str):
        return pd.Series(embed(o), name=o)
    raise TypeError

def frame(o):
    if isinstance(o, pd.DataFrame):
        return o
    if isinstance(o, pd.Series):
        return pd.DataFrame(o)
    if is_instance(o, str):
        o = [o]
    if is_instance(o, list[str]):
        return pd.DataFrame(embed(o).T, columns=o)
    raise TypeError(o)

# ======================

class O:
    def __init__(self, o):
        self.o = o

class L(O):
    def __init__(self, o):
        self.l = o
        super().__init__(o)

    def __getitem__(self, i):
        return self.l[i]

    def __len__(self):
        return len(self.l)

    def __iter__(self):
        return iter(self.l)

    def __add__(self, other):
        return L([''.join(pair) for pair in itertools.product(self, other)])

    def __repr__(self):
        return repr(self.l)

class F(O):
    def __init__(self, o):
        self.f = frame(o)
        super().__init__(o)

    def names(self):
        return self.f.columns

    def centerofmass(self):
        # center of mass: different from subtracting mean from self!
        return self.f.mean(axis=1)

    def at(self, other):
        return F(self.f.subtract(other.centerofmass(), axis=0))

    def centered(self):
        return self.at(self)

    def centered_at(self, other):
        return self.at(other)

    def __matmul__(self, other):
        return self.dot(other)

    def __call__(self, other):
        if other is None:
            other = self
        return self.at(other)

    def __repr__(self):
        return repr(self.f)

    def __getitem__(self, i):
        return self.f[i]

    def dot(self, other):
        return self.f.T @ other.f

    def sims(self, other):
        return self.dot(self.at(self), other.at(other))

    def __eq__(self, other):
        return np.allclose(self.f, other.f)

class S(F):
    def __init__(self, o):
        self.s = series(o)
        super().__init__(o)

    def name(self):
        return self.s.name

class Object(S):

    def __init__(self, o):
        super().__init__(o)

    def __repr__(self):
        return repr(self.s)

class List(F, L):

    def __init__(self, o):
        super().__init__(list(o))

    def __getitem__(self, i):
        if isinstance(i, int):
            return self.l[i]
        elif is_instance(i, str | list[str]):
            return self.f[i]
        else:
            raise IndexError(i)

    def __iter__(self):
        return iter(self.o)


def argsort_reverse(a):
    return np.argsort(-a, axis=-1)


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

def grep(queries, keys, similarity_definition='a @ b', *, n=None):
    queries = assure.plural(queries)
    a = List(queries)
    b = List(keys)
    s = eval(similarity_definition)
    i = argsort_reverse(s)
    g = 0*s
    g.iloc[:, :] = s.columns.values[i]
    g.columns = range(1, len(g.columns)+1)
    g.columns.name = similarity_definition
    g = g.iloc[:, 0:n]
    return g

def greps(queries, keys, *, n=None):
    """ Evaluate possible definitions of grep interactively
        by varying the definition of similarity """
    gs = []
    for similarity_definition in SIMILARITY_DEFINITIONS:
        g = grep(queries, keys, similarity_definition, n=n)
        gs.append(g)
    return gs

def format_grep(g, n=None):
    """ format and prepare a grep for stdout """
    if n is None:
        n = 1
    g = g.iloc[:, 0:n]
    q = g.index.tolist()
    k = g.to_csv(index=False, header=False)
    d = pd.DataFrame(q, index=k.splitlines())
    o = d.to_csv(index=True,header=False,sep=':').strip()
    return o

