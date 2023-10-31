__all__ = [
    'pdf_to_text',
]

from langchain import document_loaders

DEFAULT_METHOD = 'PyPDF'

LOADERS = {k:v for k,v in vars(document_loaders).items() if 'PDF' in k}
LOADERS = {k.lower().replace('loader', ''):v for k,v in LOADERS.items()}

def pdf_to_langchain_documents(path, method):
    """ Returns a list of langchain Document objects. """
    Loader = LOADERS[method]
    loader = Loader(path)
    return loader.load()

def pdf_to_text(path, method=DEFAULT_METHOD):
    docs = pdf_to_langchain_documents(path, method)
    pages = [doc.page_content for doc in docs]
    return '\n'.join(pages)

