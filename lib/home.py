import tornado.httpserver
import tornado.web

from lib.base import BaseRequestHandler

class HomeHandler(BaseRequestHandler):
    def get(self):
        return self.db()
