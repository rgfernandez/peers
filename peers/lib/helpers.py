"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
#from webhelpers.html.tags import checkbox, password

from webhelpers.html import escape, HTML, literal, url_escape
from webhelpers.html.tags import *
from webhelpers.date import *
from webhelpers.text import *
from webhelpers.html.converters import *
from webhelpers.html.tools import *
from webhelpers.util import *
from routes import url_for

def test(r):
    # normally, r is request.environ
    return '<br>'.join(['%s: %r' % (key, value) for (key,value) in r.items()])