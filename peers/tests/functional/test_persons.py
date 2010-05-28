from peers.tests import *

class TestPersonsController(TestController):

    def test_index(self):
        response = self.app.get(url('persons'))
        # Test response...

    def test_index_as_xml(self):
        response = self.app.get(url('formatted_persons', format='xml'))

    def test_create(self):
        response = self.app.post(url('persons'))

    def test_new(self):
        response = self.app.get(url('new_person'))

    def test_new_as_xml(self):
        response = self.app.get(url('formatted_new_person', format='xml'))

    def test_update(self):
        response = self.app.put(url('person', id=1))

    def test_update_browser_fakeout(self):
        response = self.app.post(url('person', id=1), params=dict(_method='put'))

    def test_delete(self):
        response = self.app.delete(url('person', id=1))

    def test_delete_browser_fakeout(self):
        response = self.app.post(url('person', id=1), params=dict(_method='delete'))

    def test_show(self):
        response = self.app.get(url('person', id=1))

    def test_show_as_xml(self):
        response = self.app.get(url('formatted_person', id=1, format='xml'))

    def test_edit(self):
        response = self.app.get(url('edit_person', id=1))

    def test_edit_as_xml(self):
        response = self.app.get(url('formatted_edit_person', id=1, format='xml'))
