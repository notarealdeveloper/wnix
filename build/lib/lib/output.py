__all__ = [
    'output_print',
    'output_bytes',
    'output_json',
    'output_pickle',
]

import sys
import json
import pickle

def output_print(array):
    return print(array)

def output_bytes(array):
    sys.stdout.buffer.write(array.tobytes())

def output_json(array):
    import json
    print(json.dumps(array.tolist()))

def output_pickle(array):
    import pickle
    sys.stdout.buffer.write(pickle.dumps(array))
