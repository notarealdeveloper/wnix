__all__ = [
    'html_to_text',
]

def to_text(text):
    import bs4
    soup = bs4.BeautifulSoup(html, 'html.parser')
    return soup.text

html_to_text = to_text
