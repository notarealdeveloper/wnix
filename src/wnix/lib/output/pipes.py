"""
    pipe tensors between processes
"""

__all__ = [
    'stdin_to_tensor',
    'bytes_to_tensor',
    'tensor_to_bytes',
    'tensor_to_stdout',
    'tensor_to_string',
    'tensor_to_json',
    'tensor_to_pickle',
]

import sys
import numpy as np

# dtype for moving tensors between pipes, sockets, disk.
# dtype for computation is up to the user and the model.
IO_DTYPE = np.float32

def bytes_to_tensor(bytes):
    return np.frombuffer(bytes, dtype=IO_DTYPE)

def tensor_to_bytes(tensor):
    return tensor.astype(IO_DTYPE).tobytes()

def stdin_to_tensor():
    return bytes_to_tensor(sys.stdin.buffer.read())

def tensor_to_stdout(tensor):
    return sys.stdout.buffer.write(tensor_to_bytes(tensor))

def tensor_to_string(tensor):
    return repr(tensor)

def tensor_to_json(tensor):
    import json
    return json.dumps(tensor.tolist())

def tensor_to_pickle(tensor):
    import pickle
    return pickle.dumps(tensor)

