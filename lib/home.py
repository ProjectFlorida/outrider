from lib.base import BaseRequestHandler


class HomeHandler(BaseRequestHandler):
    """ Just return some dummy info for now. """
    def get(self):
        return self.db()
