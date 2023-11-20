#!/usr/bin/env python

import wnix

def object_gettext(object):

    import inspect

    methods = [
        inspect.getsource,
        inspect.getdoc,
        lambda object: object.__qualname__,
        lambda object: object.__name__,
    ]

    for method in methods:
        try:
            text = method(object)
            if text is None: raise ValueError
            return text
        except:
            pass
    else:
        return repr(object)

def module_getsource(module):
    texts = {}
    for name in dir(module):
        object = getattr(module, name)
        text = object_gettext(object)
        if text is None: continue
        texts[name] = text
    return texts


def module_getsource_for_classes(module):
    texts = {}
    for name in dir(module):
        object = getattr(module, name)
        if not isinstance(object, type):
            continue
        texts[name] = object_gettext(object)
    return texts

def test_grep_understands_python_module_tempfile():

    import tempfile
    d = module_getsource(tempfile)

    g = wnix.grep('Make a directory', d, n=2)
    i = g.intersect({'tempdir', 'TemporaryDirectory'})
    assert len(i) >= 1


def test_grep_understands_python_module_asyncio():

    import asyncio
    d = module_getsource(asyncio)

    g = wnix.grep('Run a thing', d, n=2)
    assert len(g.intersect({'run'})) >= 1

    g = wnix.grep('Run a coroutine from another thread', d, n=2)
    assert len(g.intersect({'run_coroutine_threadsafe'})) >= 1

    g = wnix.grep('Concurrency primitives', d, n=2)
    assert len(g.intersect({'locks'})) >= 1


def test_grep_understands_python_module_threading():

    import threading
    d = module_getsource_for_classes(threading)

    g = wnix.grep("A re-entrant lock", d, n=2)
    assert len(g.intersect({'RLock', '_RLock'})) >= 1

    g = wnix.grep("A condition variable", d, n=2)
    assert len(g.intersect({'Condition'})) >= 1

    g = wnix.grep("Semaphore released too many times", d, n=2)
    assert len(g.intersect({'BoundedSemaphore'})) >= 1

    g = wnix.grep("Has a .set(), .clear(), and .wait() method", d, n=2)
    assert len(g.intersect({'Event'})) >= 1

