#!/usr/bin/env python3

import wnix
import rootfs

# recompute these every time without any explicit caching, as a speed check

def test_wnix_image_and_text_to_text_correctness():
    file = rootfs.file('/usr/share/cats.jpg')
    assert wnix.image_and_text_to_text(file, "What animal is this?") == 'cat'
    assert wnix.image_and_text_to_text(file, "What animals are these?") == 'cats'
    assert wnix.image_and_text_to_text(file, "How many are there") == '2'
    assert wnix.image_and_text_to_text(file, "How many cats are there") == '2'
    assert wnix.image_and_text_to_text(file, "How many dogs are there") == '0'

IMAGES = [
    '/usr/share/cats.jpg',
    '/usr/share/bluecow.jpg',
    '/usr/share/redcow.jpg',
    '/usr/share/soccer.jpg',
    '/usr/share/cooked.jpg',
    '/usr/share/chicken.jpg',
    '/usr/share/chick.jpg',
]

PDFS = [
    '/usr/share/chicken.pdf',
    '/usr/share/cow.pdf',
]

class File:
    def __init__(self, file):
        self.bytes = rootfs.cat(file)
        self.file  = rootfs.file(file)

    def __repr__(self):
        cls = self.__class__.__name__
        name = self.file.as_posix()
        return f"{cls}({name})"

    def embed(self):
        return wnix.think(self.text())

    def name(self):
        return self.file.name

    def stem(self):
        return self.file.stem

class Image(File):
    def text(self):
        text1 = wnix.image_to_text(self.bytes)
        text2 = wnix.image_to_text(self.file)
        assert text1 == text2
        return text1

class ImageAndText(Image):
    def text(self, query):
        text1 = wnix.image_and_text_to_text(self.bytes, query)
        text2 = wnix.image_and_text_to_text(self.file, query)
        assert text1 == text2
        return text1

class Pdf(File):
    def text(self):
        text1 = wnix.pdf_to_text(self.bytes)
        text2 = wnix.pdf_to_text(self.file)
        assert text1 == text2
        return text1


def get_pdfs():
    return [Pdf(file) for file in PDFS]

def get_images():
    return [Image(file) for file in IMAGES]

def get_files():
    return get_pdfs() + get_images()

def get_texts():
    files = get_files()
    return [file.text() for file in files]

def get_embeds():
    files = get_files()
    return [file.embed() for file in files]

def test_wnix_image_to_text_correctness():
    images = {p.stem(): p for p in get_images()}
    assert 'cat'    in images['cats'].text()
    assert 'blue'   in images['bluecow'].text()
    assert 'cow'    in images['bluecow'].text()
    assert 'red'    in images['redcow'].text()
    assert 'cow'    in images['redcow'].text()
    assert 'soccer' in images['soccer'].text()

def test_wnix_pdf_to_text_correctness():
    pdfs = {p.stem(): p for p in get_pdfs()}
    assert 'chicken' in pdfs['chicken'].text()
    assert 'CoW'     in pdfs['cow'].text()

def test_wnix_thought_correctness():
    files = {p.name(): p for p in get_files()}
    import itertools
    import collections
    keys = list(files.keys())
    dots = collections.defaultdict(dict)
    for a,b in itertools.product(keys, keys):
        A = files[a]
        B = files[b]
        va = A.embed()
        vb = B.embed()
        dots[a][b] = (va * vb).sum()
    pairs = dict(dots)
    ranks = {}
    for a,d in dots.items():
        pairs[a] = sorted(d.items(), key=lambda pair: pair[1], reverse=True)
        ranks[a] = [k for k,v in pairs[a]]

    r = ranks['bluecow.jpg']
    assert r.index('redcow.jpg') < r.index('chicken.jpg')
    assert r.index('redcow.jpg') < r.index('soccer.jpg')
    assert r.index('redcow.jpg') < r.index('chicken.pdf')
    assert r.index('redcow.jpg') < r.index('cow.pdf') # same word diff topic

    r = ranks['chicken.jpg']
    assert r.index('chick.jpg') < r.index('bluecow.jpg')
    assert r.index('chick.jpg') < r.index('soccer.jpg')
    assert r.index('chick.jpg') < r.index('chicken.pdf')

