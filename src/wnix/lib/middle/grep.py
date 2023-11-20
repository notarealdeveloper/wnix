__all__ = [
    'grep',
    'greps',
    'format_grep',
]

import assure
from .types import Object, List, Dict

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


def argsort_reverse(a):
    import numpy as np
    return np.argsort(-a, axis=-1)

def promote(o):
    if isinstance(o, (list, tuple, set)):
        return List(o)
    elif isinstance(o, dict):
        return Dict(o)
    elif isinstance(o, str):
        return Object(o)
    elif isinstance(o, bytes):
        return Object(o.decode())
    elif isinstance(o, (List, Dict, Object)):
        return o
    else:
        raise TypeError(o)

def grep(queries, keys, similarity_definition='a @ b', *, n=None):
    q = promote(assure.plural(queries))
    k = promote(assure.plural(keys))
    s = (lambda a,b: eval(similarity_definition))(q,k)
    i = argsort_reverse(s)
    g = 0*s
    g.iloc[:, :] = s.columns.values[i]
    g.columns = list(range(1, len(g.columns)+1))
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
    import pandas as pd
    if n is None:
        n = 1
    g = g.iloc[:, 0:n]
    q = g.index.tolist()
    k = g.to_csv(index=False, header=False)
    d = pd.DataFrame(q, index=k.splitlines())
    o = d.to_csv(index=True,header=False,sep=':').strip()
    return o

