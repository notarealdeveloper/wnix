"""
    output tensors

    exit the system
"""

__all__ = [
    'tensor_to_string',
    'tensor_to_json',
    'tensor_to_pickle',
]

import json
import pickle

def tensor_to_string(tensor):
    return repr(tensor)

def tensor_to_json(tensor):
    return json.dumps(tensor.tolist())

def tensor_to_pickle(tensor):
    return pickle.dumps(tensor)

