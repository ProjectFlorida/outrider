import tornado.httpserver
import tornado.web

from lib.base import BaseHandler

class HomeHandler(BaseHandler):
    def get(self):
        return self.db
