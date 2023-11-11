#!/usr/bin/env python3

__all__ = ['main']

import os
import sys
import argparse
import wnix

import ensure
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

def what(query, keys):
    q = ensure.vector(query)
    K = ensure.vectors([wnix.think(key) for key in keys])
    I = What(q, K)
    return np.array(keys)[I].tolist()

def What(q, K):
    Q = q[None, :]
    K = unit(K)
    sims = softmax(Q @ K.T)
    I = np.argsort(sims.ravel())[::-1]
    return I

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser('what')
    parser.add_argument('list')
    args = parser.parse_args(argv)

    if os.path.exists(args.list):
        keys = open(args.list).read().splitlines()
    else:
        keys = args.list.split(',')

    q = wnix.stdin_to_tensor()
    ranks = what(q, keys)
    output = '\n'.join(ranks)
    print(output)

if __name__ == '__main__':
    main(sys.argv[1:])
