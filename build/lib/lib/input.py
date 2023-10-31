"""
sensory system

turns hard-to-embed data types (pdfs, images, etc)
into easy-to-embed data types (collections of tokens)
"""

__all__ = [
    'pdf_to_text',
]

import io
import pypdf

def pdf_to_text(file):
    if isinstance(file, io.IOBase):
        # ensure file is seekable to support stdin.
        file = io.BytesIO(file.read())
    reader = pypdf.PdfReader(file)
    pages = [page.extract_text() for page in reader.pages]
    return '\n\n'.join(pages)
