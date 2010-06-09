import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from peers.lib.base import BaseController, render

from peers.lib import helpers as h
from peers.lib import modules

log = logging.getLogger(__name__)

class MessagesController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py
    # file has a resource setup:
    #     map.resource('message', 'messages')

    def index(self, format='html'):
        """GET /messages: All items in the collection"""
        # url('messages')

    def create(self):
        """POST /messages: Create a new item"""
        # url('messages')
        ## no need to validate. this method is exposed to everyone
        if not modules.base.msghandler.create_message('http', request.params):
            abort(501, '')
        return ''

    def new(self, format='html'):
        """GET /messages/new: Form to create a new item"""
        # url('new_message')
        #if not modules.validated(request, url='messages/new'):
        #    abort(404, '')
        return render('/message.mako')

    def update(self, id):
        """PUT /messages/id: Update an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(url('message', id=ID),
        #           method='put')
        # url('message', id=ID)

    def delete(self, id):
        """DELETE /messages/id: Delete an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(url('message', id=ID),
        #           method='delete')
        # url('message', id=ID)

    def show(self, id, format='html'):
        """GET /messages/id: Show a specific item"""
        # url('message', id=ID)

    def edit(self, id, format='html'):
        """GET /messages/id/edit: Form to edit an existing item"""
        # url('edit_message', id=ID)
