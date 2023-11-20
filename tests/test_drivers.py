#!/usr/bin/env python3

import embd
import assure
import pathlib
from drivers import pdf
from drivers import image

IMAGES = [
    'root/usr/share/cats.jpg',
    'root/usr/share/bluecow.jpg',
    'root/usr/share/redcow.jpg',
    'root/usr/share/soccer.jpg',
    'root/usr/share/cooked.jpg',
    'root/usr/share/chicken.jpg',
    'root/usr/share/chick.jpg',
]

PDFS = [
    'root/usr/share/chicken.pdf',
    'root/usr/share/cow.pdf',
]

class File:
    def __init__(self, file):
        self.file  = pathlib.Path(file)
        self.bytes = assure.bytes(open(file, 'rb'))

    def __repr__(self):
        cls = self.__class__.__name__
        name = self.file.as_posix()
        return f"{cls}({name})"

    def embed(self):
        return embd.think(self.text())

    def name(self):
        return self.file.name

    def stem(self):
        return self.file.stem

class Image(File):
    def text(self):
        text1 = image.to_text(self.bytes)
        text2 = image.to_text(self.file)
        assert text1 == text2
        return text1

class ImageAndText(Image):
    def text(self, query):
        text1 = image.and_text_to_text(self.bytes, query)
        text2 = image.and_text_to_text(self.file, query)
        assert text1 == text2
        return text1

class Pdf(File):
    def text(self):
        text1 = pdf.to_text(self.bytes)
        text2 = pdf.to_text(self.file)
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

def test_image_to_text_correctness():
    images = {p.stem(): p for p in get_images()}
    assert 'cat'    in images['cats'].text()
    assert 'blue'   in images['bluecow'].text()
    assert 'cow'    in images['bluecow'].text()
    assert 'red'    in images['redcow'].text()
    assert 'cow'    in images['redcow'].text()
    assert 'soccer' in images['soccer'].text()

def test_pdf_to_text_correctness():
    pdfs = {p.stem(): p for p in get_pdfs()}
    assert 'chicken' in pdfs['chicken'].text()
    assert 'CoW'     in pdfs['cow'].text()
