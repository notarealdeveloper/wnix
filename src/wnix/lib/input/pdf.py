__all__ = [
    'pdf_to_text',
]

import io

def pdf_to_text(file):
    import pypdf
    if hasattr(file, 'read'):
        # ensure file is seekable to support stdin.
        file = io.BytesIO(file.read())
    reader = pypdf.PdfReader(file)
    pages = [page.extract_text() for page in reader.pages]
    return '\n\n'.join(pages)

to_text = pdf_to_text
