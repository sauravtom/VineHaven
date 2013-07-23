#!/usr/bin/env python

import jinja2
import os
import webapp2
from scraper import *

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

class MainPage(webapp2.RequestHandler):
    def get(self):
        x = 'hi'
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(x=x))
    def post(self):
    	pass    

class Viner(webapp2.RequestHandler):
    def get(self):
    	pass
    def post(self):
        word = self.request.get('content')
        arr = scrape_for_vine(word)
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(arr=arr))
        #self.redirect('/')


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/vines',Viner)
], debug=True)


'''
todos
+ and play button to video player
+ sleek design
+ google analytics
+ Add search FAQs
'''