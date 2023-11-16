#!/usr/bin/env python

import os

def test_grep_shell():

    lines = os.popen("cat $(rootfs)/etc/sports | Grep 'european,american' sports").read().splitlines()

    assert lines == [
        'american:basketball',
        'american:baseball',
        'american:football',
        'european:hockey',
        'european:soccer',
        'european:rugby',
    ]
