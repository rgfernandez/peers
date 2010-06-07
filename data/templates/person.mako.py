# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1275277557.450774
_template_filename='/Users/NThC/Documents/01-Research/UPM NThC/peers/peers/templates/person.mako'
_template_uri='/person.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(escape(h.form(h.url_for(action='create'), method='POST')))
        __M_writer(u'\n\n<table><tr>\n    <td>First Name:</td>\n    <td>\n        ')
        # SOURCE LINE 6
        __M_writer(escape(h.text('first_name')))
        __M_writer(u'\n    </td>\n</tr><tr>\n    <td>Middle Name:</td>\n    <td>\n        ')
        # SOURCE LINE 11
        __M_writer(escape(h.text('middle_name')))
        __M_writer(u'\n    </td>\n</tr><tr>\n    <td>Last Name:</td>\n    <td>\n        ')
        # SOURCE LINE 16
        __M_writer(escape(h.text('last_name')))
        __M_writer(u'\n    </td>\n</tr><tr>\n    <td>Birthdate:</td>\n    <td>\n        ')
        # SOURCE LINE 21
        __M_writer(escape(h.textarea('birthdate')))
        __M_writer(u'\n    </td>\n</tr><tr>\n    <td>Contact:</td>\n    <td>\n        ')
        # SOURCE LINE 26
        __M_writer(escape(h.text('contact')))
        __M_writer(u'\n    </td>\n</tr></table>\n\n')
        # SOURCE LINE 30
        __M_writer(escape(h.submit('submit', 'Submit')))
        __M_writer(u'\n\n')
        # SOURCE LINE 32
        __M_writer(escape(h.end_form()))
        return ''
    finally:
        context.caller_stack._pop_frame()


