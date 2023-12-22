#!/usr/bin/env python

import os
import sys
import embd
import argparse

def man_dirs():
    for dir in os.popen('manpath').read().split(':'):
        if os.path.exists(dir):
            yield dir

def man_page_paths():
    for man_dir in man_dirs():
        for path in os.popen(f"find {man_dir!r} -type f -name '*.gz' | grep -P 'motd|whois|hostname'"):
            yield path.strip()

def man_cat(path):
    text = os.popen(f"cat {path!r} | gunzip | nroff -man 2>/dev/null").read()
    return text

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
            print(result)
        return

    print("usage: man2 [-b] [keyword]")
    sys.exit(1)

if __name__ == '__main__':
    main(sys.argv[1:])
