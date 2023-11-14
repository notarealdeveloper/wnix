#!/usr/bin/python3

from wnix import grep, greps

# queries have no type, they're just sentences, lines, or blobs.
queries = [
    'wolf', 'chihuahua', 'puppy',
    'lion', 'tabby', 'kitten',
]

# keys are a specification of a pattern, like a regex.
# they have a type (the regex) and a value (the actual matched text)
animals  = ['dog', 'cat']
sizes    = ['big animal', 'small animal']
domestic = ['pet animal', 'wild animal']


ANSWERS_GENUS = ['dog', 'dog', 'dog', 'cat', 'cat', 'cat']

ANSWERS_SIZE = [
    f"{size} animal" for size in
    ['big', 'small', 'small', 'big', 'small', 'small']
]

ANSWERS_DOMESTIC = [
    f"{size} animal" for size in
    ['wild', 'pet', 'pet', 'wild', 'pet', 'pet']
]

def test_simple_animals():
    a = grep(queries, animals)[1].tolist()
    assert a == ANSWERS_GENUS

def test_simple_sizes():
    a = grep(queries, sizes)[1].tolist()
    assert a == ANSWERS_SIZE

def test_simple_domestic():
    a = grep(queries, domestic)[1].tolist()
    assert a == ANSWERS_DOMESTIC

