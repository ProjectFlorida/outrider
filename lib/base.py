from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import tornado.web
import tornado.httpserver
from sqlalchemy import create_engine
from utils.database import Database

class BaseHandler(object):
    @property
    def db(self):
	config = Database().load_config()
        return create_engine("postgresql://%s@%s/%s" %
			(config['username'], config['host'], config['database']))

    @property
    def load_db_config(self):
        """ Call the Database class to load and parse the configuration from
        yml on disk. Returns a dict. """
        return Database().load_config()

class BaseRequestHandler(BaseHandler, tornado.web.RequestHandler):
    """ This class is the base for all the other handlers. You should always
    inherit from this class when initiating a class which is a handler to which
    the application will direct requests. """
    pass
