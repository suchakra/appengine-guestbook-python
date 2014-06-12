import os
import webapp2

from google.appengine.api import users
from models import greeting as model

class Guestbook(webapp2.RequestHandler):
    def post(self):
        greeting_ = model.Greeting(parent=model.guestbook_key())

        if users.get_current_user():
            greeting_.author = users.get_current_user()

        greeting_.content = self.request.get('content')
        greeting_.put()
        self.redirect('/')