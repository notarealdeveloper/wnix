"""
    input tensors
"""

__all__ = [
    'stdin_to_tensor',
    'bytes_to_tensor',
    'tensor_to_bytes',
    'tensor_to_stdout',
]

import sys
import numpy as np

def stdin_to_tensor():
    return bytes_to_tensor(sys.stdin.buffer.read())

def bytes_to_tensor(bytes):
    return np.frombuffer(bytes)

def tensor_to_bytes(tensor):
    return tensor.tobytes()

def tensor_to_stdout(tensor):
    return sys.stdout.buffer.write(tensor_to_bytes(tensor))
