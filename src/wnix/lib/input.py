"""
    sensory system

    turns hard-to-embed data types (pdfs, images, etc)
    into easy-to-embed data types (collections of tokens)
"""

from drivers import pdf
from drivers import html
from drivers import image

from drivers.pdf.lib import *
from drivers.html.lib import *
from drivers.image.lib import *
