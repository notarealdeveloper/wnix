"""
stdin to tensor

support for piping tensors between processes
"""

__all__ = [
    'stdin_to_tensor',
]

import sys
import numpy as np

def bytes_to_tensor(bytes):
    array = np.frombuffer(bytes)
    assert isinstance(array, np.ndarray)
    return array

def stdin_to_tensor():
    bytes = sys.stdin.buffer.read()
    return bytes_to_tensor(bytes)
