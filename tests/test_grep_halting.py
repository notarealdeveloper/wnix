#!/usr/bin/python3

from wnix import grep

def foo(n):
    while True:
        n += 1
    return n

def bar(n):
    s = 0
    for k in range(n):
        s += k
    return s

def baz(n):
    while n > 0:
        n -= 1
    return n

def doo(n):
    n = abs(n)+1
    for j in range(n):
        pass
    return j

def boo(n):
    x = n
    for k in range(n**2):
        x += k**2
    return x


def test_simple_halting():
    import inspect
    functions  = (foo, bar, baz, doo, boo)
    sources    = [inspect.getsource(f) for f in functions]
    names      = [f.__name__ for f in functions]

    answers    = ['for loop', 'while loop']
    g = grep(sources, answers, n=1)
    assert g[1].tolist() == [
        'while loop', 'for loop', 'while loop', 'for loop', 'for loop'
    ]

