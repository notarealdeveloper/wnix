from .bin import *
from .lib import *
from .etc import *
from .usr import *

def pwd():
    import os
    return os.path.dirname(__file__)

def ls(path='/'):
    return [p.stem for p in file(path).glob('*')]

def find(path='/'):
    return [p for p in file(path).rglob('*')]

def cat(path):
    return file(path).read_bytes()

def file(path):
    import importlib.resources
    path = path.strip('/')
    path = importlib.resources.files(__name__).joinpath(path)
    return path

def lines(path):
    return cat(path).decode().splitlines()
