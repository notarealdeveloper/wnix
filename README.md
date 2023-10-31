# wnix

Unix coreutils for software 2.0

## /bin

### parse

Turns non-text into text.

Currently supports pdfs.

```sh
parse file.pdf

cat file.pdf | parse

cat file.pdf | parse > file.txt
```

### embed

Turns text into vectors.

Currently supports flag embeddings.

```sh
embed file.txt

cat file.txt | embed

cat file.txt | embed --size base

cat file.txt | embed --size small

cat file.txt | embed --size large > file.vec
```
