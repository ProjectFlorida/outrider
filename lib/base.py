from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import tornado.web
import tornado.httpserver
from sqlalchemy import create_engine
from utils.database import Database

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
      config = self.load_db_config()
      return create_engine("postgresql://%s@%s/%s" %
          (config['username'], config['host'], config['database']))

    @property
    def load_db_config(self):
        return Database().load_config()
