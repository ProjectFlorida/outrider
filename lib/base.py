from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import tornado.web
import tornado.httpserver
from sqlalchemy import create_engine
from utils.database import Database


class BaseHandler(object):
    """ This class is a base class for any subsequent classes requiring a
    connection to the database. BaseRequestHandler inherits from This
    class. """

    @property
    def db(self):
        """ Fetch the database configuration for the environment, and
        create an Engine object with the retrieved information. """
        config = Database().load_config()
        return create_engine("%s://%s@%s/%s" %
                             (config['adapter'], config['username'],
                              config['host'], config['database']))

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
