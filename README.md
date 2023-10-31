# wnix

Unix coreutils for software 2.0

## /bin

### parse

Turns non-text into text.

Currently supports pdfs.

```sh
parse file.pdf

cat file.pdf | parse

cat file.pdf | parse --method pypdf
```

### embed

Turns text into vectors.

Currently supports openai and flag embeddings.

Openai backend requires an API key.

```sh
embed file.txt

cat file.txt | embed

cat file.txt | embed --size base

cat file.txt | embed --size small

cat file.txt | embed --size large
```
