# wnix

Unix coreutils for software 2.0

# usage

## bin

### input

Turns non-text into text.

```sh
input file.pdf

cat file.pdf | input

cat file.pdf | input > file.txt
```

### think

Turns text into vectors.

Currently supports flag embeddings.

```sh
think file.txt

cat file.txt | think

cat file.txt | think --size base

cat file.txt | think --size small

cat file.txt | think --size large > file.vec
```

### output

```sh
cat file.vec | output

cat file.vec | output --to json

cat file.vec | output --to pickle

cat file.vec | output --to bytes
```


# Contributing

## How to

This project aims to keep its build system minimal and standard.
The build should use only built-in python tools or tools described in PEPs.

### Why pyproject.toml
- [PEP 518](https://peps.python.org/pep-0518/) introduced `pyproject.toml` as a standard for build systems.
- [The python packaging documentation](https://packaging.python.org/en/latest/tutorials/packaging-projects/#creating-pyproject-toml) description of `pyproject.toml`.
- [The pip documentation on pypa](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/) on how to write a `pyproject.toml`.

### Why not setup.py
- [The pip documentation on pypa](https://pip.pypa.io/en/stable/reference/build-system/setup-py/) explanation that setup.py is deprecated

### What is setup.cfg
- [The setuptools documentation on pypa](https://setuptools.pypa.io/en/latest/userguide/declarative_config.html) describes `setup.cfg`.
