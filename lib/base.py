import tornado.web
import tornado.httpserver
from sqlalchemy import create_engine
from utils.database import Database

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
      config = self.load_db_config()
      return create_engine("postgresql://%s@%s/%s" %
          (config.get('database', 'username'), config.get('database', 'host'),
            config.get('database', 'database')))

    @property
    def load_db_config(self):
        return Database().load_config
