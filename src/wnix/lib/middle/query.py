__all__ = [
    'what',
    'What',
]

import wnix
import numpy as np

def argsort(keys, I):
    return np.array(keys)[I].tolist()

def what(query, keys):
    q = wnix.ensure_vect(query)
    K = wnix.ensure_rect(keys)
    I = What(q, K)
    return argsort(keys, I)

def What(q, K):
    Q = q[None, :]
    K = wnix.unit(K)
    sims = wnix.softmax(Q @ K.T)
    I = np.argsort(sims.ravel())[::-1]
    return I
