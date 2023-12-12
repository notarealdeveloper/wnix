#!/usr/bin/python3

from wnix import grep, greps

# queries: aka, questions.
# There are arbitrarily many of these,
# and we never know all of them,
# so any meaningful operation should be a map over queries,
# we should never (for example) move to the center of
# mass of the set of queries.

QUERIES_1 = [
    'a guy pretending to be a cat',
    'a drunk guy who thinks hes a lion',
    'your submissive furry boyfriend',
    'a male biological cat',
    'your obedient pet tabby mister whiskers',
    'a young male tiger at the San Diego zoo',
]

QUERIES_2 = [
    'a quirky tinder match named jane who meows at you',
    'an obnoxious e-girl who wears ears',
    'your submissive furry girlfriend',
    'your fierce pet tabby mrs boots',
    'a young female tiger at the Omaha zoo',
    'an african jaguar mother who recently had cubs',
]

QUERIES_3 = QUERIES_1 + QUERIES_2

KEYS_1 = ['cat boy', 'boy cat']
KEYS_2 = ['cat girl', 'girl cat']
KEYS_3 = KEYS_1 + KEYS_2

ANSWERS_1 = ['cat boy', 'cat boy', 'cat boy', 'boy cat', 'boy cat', 'boy cat']
ANSWERS_2 = ['cat girl', 'cat girl', 'cat girl', 'girl cat', 'girl cat', 'girl cat']
ANSWERS_3 = ANSWERS_1 + ANSWERS_2


def test_grep_cats_1(debug=False):
    gs = greps(QUERIES_1, KEYS_1, n=1)
    for g in gs:
        output = g[1].tolist()
        assert output == ANSWERS_1, output
        if debug:
            print(g)
            print('='*42)

def test_grep_cats_2(debug=False):
    gs = greps(QUERIES_2, KEYS_2, n=1)
    for g in gs:
        output = g[1].tolist()
        assert output == ANSWERS_2, output
        if debug:
            print(g)
            print('='*42)

def test_grep_cats_3(debug=False):
    gs = greps(QUERIES_3, KEYS_3, n=1)
    for g in gs:
        output = g[1].tolist()
        assert output == ANSWERS_3, output
        if debug:
            print(g)
            print('='*42)
