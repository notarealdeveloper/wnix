#!/usr/bin/env python3

__all__ = ['what']

# TODO: this module is a legacy implementation and will soon be replaced
# with a call to soft Grep with different arguments once we can make this work:
#
# from .grep import Grep
# def what(query, keys):
#     return Grep(query, keys, n=1)

import wnix
import assure
import numpy as np
from .types import List

def norm(A, axis=-1, keepdims=True):
    return np.linalg.norm(A, axis=axis, keepdims=keepdims)

def unit(A, axis=-1, keepdims=True):
    return A / norm(A, axis=axis, keepdims=keepdims)

def similarities(q, K):
    Q = q[None, :]
    K = unit(K)
    import scipy.special
    sims = scipy.special.softmax(Q @ K.T, axis=-1)
    return sims

def what(query, keys):
    q = assure.vector(query)
    K = List(keys).f.values.T
    s = similarities(q, K)
    I = np.argsort(s.ravel())[::-1]
    return np.array(keys)[I].tolist()
