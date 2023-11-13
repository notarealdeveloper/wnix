__all__ = [
    'pdf_to_text',
]

import io
import assure

def pdf_to_text(file):
    import pypdf
    # assure file is seekable to support stdin.
    file = assure.seekable(file)
    reader = pypdf.PdfReader(file)
    pages = [page.extract_text() for page in reader.pages]
    return '\n\n'.join(pages)

to_text = pdf_to_text
