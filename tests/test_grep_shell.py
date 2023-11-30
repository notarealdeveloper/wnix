#!/usr/bin/env python

import os

def test_grep_shell():

    cmd = "echo baseball basketball rugby soccer | fmt -1 | grep2 -n 1 'european sport,american sport'"
    out = os.popen(cmd).read().splitlines()

    assert out == [
        'american sport:baseball',
        'american sport:basketball',
        'european sport:rugby',
        'european sport:soccer',
    ]
