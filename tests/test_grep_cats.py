#!/usr/bin/python3

from wnix import grep, greps

# queries: aka, questions.
# There are arbitrarily many of these,
# and we never know all of them,
# so any meaningful operation should be a map over queries,
# we should never (for example) move to the center of
# mass of the set of queries.

# note, the word fuck is necessary in queries 2.
# on replacing "meows while you fuck her" with the
# more polite "meows in bed", the model suddenly
# infers biological cat, i.e., "girl cat", which
# is a reasonable guess in retrospect, so let's
# be clear about what we means since this is a
# fucking test suite :p


QUERIES_1 = [
    'a guy pretending to be a cat',
    'a drunk guy who thinks hes a lion',
    'your submissive furry boyfriend',
    'a male biological cat',
    'your obedient pet tabby mister whiskers',
    'a young male tiger at the San Diego zoo',
]

QUERIES_2 = [
    'a girl who meows while you fuck her',
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
        assert g[1].tolist() == ANSWERS_1
        if debug:
            print(g)
            print('='*42)

def test_grep_cats_2(debug=False):
    gs = greps(QUERIES_2, KEYS_2, n=1)
    for g in gs:
        assert g[1].tolist() == ANSWERS_2
        if debug:
            print(g)
            print('='*42)

def test_grep_cats_3(debug=False):
    gs = greps(QUERIES_3, KEYS_3, n=1)
    for g in gs:
        assert g[1].tolist() == ANSWERS_3
        if debug:
            print(g)
            print('='*42)
