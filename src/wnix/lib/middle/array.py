#!/usr/bin/env python3

__all__ = [
    'softmax',
    'norm',
    'unit',
]

import numpy as np
import scipy.special

def norm(A, axis=-1, keepdims=True):
    return np.linalg.norm(A, axis=axis, keepdims=keepdims)

def unit(A, axis=-1, keepdims=True):
    return A/norm(A, axis=axis, keepdims=keepdims)

def softmax(A):
    return scipy.special.softmax(A, axis=-1)

def sum(A, axis=-1, keepdims=True):
    return A.sum(axis=axis, keepdims=True)

# add to tests
# ============
# A = np.random.normal(size=(8,100))
# sum(softmax(A))
# norm(unit(A))
