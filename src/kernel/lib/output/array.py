#!/usr/bin/env python3

__all__ = [
    'norm',
    'unit',
    'softmax',
    'argsort',
    'similarities',
    'permute',
]

import numpy as np
import scipy.special

def norm(A, axis=-1, keepdims=True):
    return np.linalg.norm(A, axis=axis, keepdims=keepdims)

def unit(A, axis=-1, keepdims=True):
    return A/norm(A, axis=axis, keepdims=keepdims)

def softmax(A):
    return scipy.special.softmax(A, axis=-1)

def argsort(A):
    return np.argsort(A)

def similarities(q, K):
    Q = q[None, :]
    K = unit(K)
    sims = softmax(Q @ K.T)
    return sims

def permute(keys, I):
    return np.array(keys)[I]

