#!/usr/bin/env python

import wnix
from wnix import List, Dict

def module_getsource(module):
    d = {}
    import inspect
    for name in dir(module):

        object = getattr(module, name)

        try:    src = inspect.getsource(object)
        except: src = None

        try:    doc = inspect.getdoc(object)
        except: doc = None

        for val in (src, doc, name):
            if val is not None:
                d[name] = val
                break
    return d


def test_grep_module():
    import tempfile
    d = module_getsource(tempfile)
    g = wnix.grep('Make a directory', d, n=1)
    assert np.all(g == 'tempdir')

    import asyncio
    d = module_getsource(asyncio)
    g = wnix.grep('Run a thing', d, n=1)
    assert np.all(g == 'run')
    g = wnix.grep('Run a coroutine from another thread', d, n=1)
    assert np.all(g == 'run_coroutine_threadsafe')
    g = wnix.grep('Concurrency primitives', d, n=1)
    assert np.all(g == 'locks')

