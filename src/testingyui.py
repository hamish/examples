#!/usr/bin/env python
import cgi
import os

import wsgiref.handlers

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext import db

class Thing(db.Model):
    name = db.StringProperty()
    description = db.TextProperty()

class ListHandler(webapp.RequestHandler):
  def get(self):
    editor = self.request.get('editor', 'simple')
    things=db.GqlQuery("SELECT * FROM Thing ORDER BY name")
    values = {
              'things' : things,
              'editor' : editor,
              }
    path = os.path.join(os.path.dirname(__file__),'', 'testingyui_list.html')
    self.response.out.write(template.render(path, values))

class EditHandler(webapp.RequestHandler):
  def get(self):
    editor = self.request.get('editor', 'simple')
    key_name = self.request.get('key')
    thing = {}
    if (key_name):
        thing= db.get(db.Key(key_name))
    values = {
              'thing' : thing,
              'editor' : editor,
              }

    path = os.path.join(os.path.dirname(__file__),'', 'testingyui_edit.html')
    html = template.render(path, values)
    
    self.response.out.write(html)

class ViewHandler(webapp.RequestHandler):
  def get(self):
    editor = self.request.get('editor', 'simple')
    key_name = self.request.get('key')
    thing = {}
    if (key_name):
        thing= db.get(db.Key(key_name))
    values = {
              'thing' : thing,
              'editor' : editor,
              }

    path = os.path.join(os.path.dirname(__file__),'', 'testingyui_view.html')
    html = template.render(path, values)
    
    self.response.out.write(html)

class SaveHandler(webapp.RequestHandler):
  def post(self):
    editor = self.request.get('editor', 'simple')
    key_name = self.request.get('key')
    thing=Thing()
    if (key_name):
        thing= db.get(db.Key(key_name))
    thing.name = self.request.get('name')
    thing.description = self.request.get('description')
    thing.put()
    self.redirect('../?editor='+editor)

def main():
  application = webapp.WSGIApplication([('/testingyui/', ListHandler),
                                        ('/testingyui/edit/', EditHandler),
                                        ('/testingyui/view/', ViewHandler),
                                        ('/testingyui/save/', SaveHandler),
                                        ])
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()