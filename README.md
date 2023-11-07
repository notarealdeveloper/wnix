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
