#!/usr/bin/env python

import os

def test_grep_shell():

    cmd = "lines baseball basketball rugby soccer | Grep 'european,american' sports"
    out = os.popen(cmd).read().splitlines()

    assert out == [
        'american:baseball',
        'american:basketball',
        'european:rugby',
        'european:soccer',
    ]
