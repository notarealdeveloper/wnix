#!/usr/bin/env python

import os
import sys
import embd
import argparse

CACHE_ROOT = os.path.join(
    os.getenv('HOME'),
    '.cache',
    'wnix',
    'man2',
)

def man_dirs():
    for dir in os.popen('manpath').read().split(':'):
        if os.path.exists(dir):
            yield dir

def man_page_paths():
    for man_dir in man_dirs():
        for path in os.popen(f"find {man_dir!r} -type f | grep -E 'man/man1/' | sort | uniq"):
            yield path.strip()

def get_cache_path(man_path):
    cache_path = os.path.join(CACHE_ROOT, man_path.lstrip('/'))
    return cache_path

def man_cat(path):
    cache_path = get_cache_path(path)
    os.makedirs(os.path.dirname(cache_path), exist_ok=True)
    if os.path.exists(cache_path):
        return open(cache_path).read()
    else:
        text = os.popen(f"man {path!r} 2>/dev/null | awk '/^(NAME|DESCRIPTION)$/,/^$/ {{if (NR > 1) print}}'").read()
        with open(f"{cache_path}.tmp", 'w') as fp:
            fp.write(text)
        os.rename(f"{cache_path}.tmp", cache_path)
        return open(cache_path).read()

def summarize(man_path):
    # the man_path will always be coming from the cached text file at this point
    import subprocess
    text = man_cat(man_path)
    p = subprocess.Popen(
        """awk '/^NAME$/,/^$/ {if (!/^NAME$/ && !/^$/) {sub(/^\s*/, ""); print;}}'""",
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    stdout, stderr = p.communicate(text.encode())
    return stdout.decode().strip()

def man_cat_all():
    pages = {}
    for path in man_page_paths():
        pages[path] = man_cat(path)
    return pages

def embed_one(path):
    page = man_cat(path)
    embed = embd.think(page)
    return embed

def embed_all(verbose=False):
    embeds = {}
    for path in man_page_paths():
        embed = embed_one(path)
        embeds[path] = embed
        if verbose:
            print(f"embedded {path!r}")
    return embeds

def main(argv=None):
    argv = argv or sys.argv[1:]
    parser = argparse.ArgumentParser(
        prog='man2',
        description='Unix man command for software 2.0',
    )
    parser.add_argument(
        'keyword',
        nargs='?',
        help="apropos keyword",
    )
    parser.add_argument(
        '-b',
        '--build',
        action='store_true',
        help="Build man-db2 by creating embeddings for all man pages on the system."
    )
    parser.add_argument(
        '-n',
        '--num',
        type = int,
        default = 10,
        help="Number of most relevant man pages to show"
    )

    args = parser.parse_args(argv)

    if args.build:
        embed_all(verbose=True)
        sys.exit(0)

    if args.keyword:
        embeds = embed_all()
        query = embd.think(args.keyword)
        from embd import List, Dict
        man_pages = man_cat_all()
        K = Dict(man_pages)
        Q = List([query])
        sims = K @ Q
        results = sims.sort_values(by=0, ascending=False).index.tolist()[:args.num]
        for result in results:
            summary = summarize(result) or f"No NAME in man page, submit a PR: {result}"
            print(summary, end='\n\n')
        return

    print("usage: man2 [-b] [keyword]")
    sys.exit(1)

if __name__ == '__main__':
    main(sys.argv[1:])

