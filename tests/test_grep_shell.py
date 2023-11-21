#!/usr/bin/env python

import os

def test_grep_shell():

    cmd = "echo baseball basketball rugby soccer | fmt -1 | grep2 -n 1 'european,american' sports"
    out = os.popen(cmd).read().splitlines()

    assert out == [
        'american:baseball',
        'american:basketball',
        'european:rugby',
        'european:soccer',
    ]
