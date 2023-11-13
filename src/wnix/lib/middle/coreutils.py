#!/usr/bin/env python3

# cat lines/colors.easy | Grep colors
# cat lines/colors.medium | Grep colors
# cat lines/colors.hard | Grep colors

__all__ = [
    'Sims',
    'What',
    'Attn',
    'Grep',
    'Sed',
]

import wnix
import assure
import numpy as np
import scipy.special

def softmax(S):
    return scipy.special.softmax(S, axis=-1)

def to_tensor(query):
    if isinstance(query, np.ndarray): return query
    query = assure.plural(query)
    Q = assure.vectors([wnix.think(q) for q in query])
    return Q


############
### Sims ###
############

def Sims(query, keys):
    Q = to_tensor(query)
    K = to_tensor(keys)
    return _Sims(Q, K, query, keys)


def _Sims(Q, K, query, keys):
    std = lambda X: X.std(0, keepdims=True)
    avg = lambda X: X.mean(0, keepdims=True)
    #Q = (Q  - avg(Q)) / np.sqrt(std(Q))
    #K = (K  - avg(K)) / np.sqrt(std(K))
    Q = (Q  - avg(Q)) / std(Q)
    K = (K  - avg(K)) / std(K)
    W = softmax(Q @ K.T)
    return W


############
### What ###
############

def What(query, keys):
    Q = to_tensor(query)
    K = to_tensor(keys)
    return _What(Q, K, query, keys)

def _What(Q, K, query, keys):
    S = _Sims(Q, K, query, keys)
    I = np.argsort(S, axis=-1)[..., ::-1]
    V = np.array(keys)[I]
    return V.T


############
### Attn ###
############

def Attn(query, keys, values=None):
    if values is None:
        values = keys
    Q = to_tensor(query)
    K = to_tensor(keys)
    V = to_tensor(values)
    return _Attn(Q, K, V, query, keys, values)

def _Attn(Q, K, V, query, keys, values):
    W = _Sims(Q, K, query, keys)
    return W @ V


############
### Grep ###
############

def Grep(query, keys):
    A = Attn(query, keys)
    return What(A, keys)


###########
### Sed ###
###########

def Sed(query, keys, values):
    A = Attn(query, keys, values)
    return What(A, values)

