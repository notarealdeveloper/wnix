__all__ = [
   'url_to_html',
   'url_to_text',
]

def url_to_html(url):
    import requests
    return requests.get(url).content.decode()

def url_to_text(url):
    from . import html_to_text
    html = url_to_html(url)
    text = html_to_text(html)
    return text
