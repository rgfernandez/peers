import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from peers.lib.base import BaseController, render

from peers.lib import helpers as h

log = logging.getLogger(__name__)

class PersonsController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py
    # file has a resource setup:
    #     map.resource('person', 'persons')

    def index(self, format='html'):
        """GET /persons: All items in the collection"""
        # url('persons')
        #return '<br>'.join([i for i in dir(m.meta.Session.query(m.e.Person))])
        #redirect_to(controller='persons',action='create')
        session['test'] = 'testing'
        session.save()
        return '<a href="persons/create">hi</a>'

    def create(self):
        """POST /persons: Create a new item"""
        # url('persons')
        return '<br>'.join(['%s: %r' % (key, value) for (key,value) in request.environ.items()])
        #return '<br>'.join(['%s: %r' % (elem,item) for (elem,item) in request.headers.items()])
        #return session['test']

    def new(self, format='html'):
        """GET /persons/new: Form to create a new item"""
        # url('new_person')
        return render('/person.mako')

    def update(self, id):
        """PUT /persons/id: Update an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(url('person', id=ID),
        #           method='put')
        # url('person', id=ID)

    def delete(self, id):
        """DELETE /persons/id: Delete an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(url('person', id=ID),
        #           method='delete')
        # url('person', id=ID)

    def show(self, id, format='html'):
        """GET /persons/id: Show a specific item"""
        # url('person', id=ID)

    def edit(self, id, format='html'):
        """GET /persons/id/edit: Form to edit an existing item"""
        # url('edit_person', id=ID)
