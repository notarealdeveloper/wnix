#!/usr/bin/env python3

__all__ = ['what']

def what(query, keys, n=1):
    from .grep import Grep
    g = Grep(query, keys)
    return g.what(n=n)
