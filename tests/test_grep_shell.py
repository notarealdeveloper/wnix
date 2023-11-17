#!/usr/bin/env python

import os

def test_grep_shell():

    cmd = "echo baseball basketball rugby soccer | fmt -1 | Grep 'european,american' sports"
    out = os.popen(cmd).read().splitlines()

    assert out == [
        'american:baseball',
        'american:basketball',
        'european:rugby',
        'european:soccer',
    ]
