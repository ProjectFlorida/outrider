import ConfigParser
import os

class Database(object):
    def load_config(self):
        parser = ConfigParser.ConfigParser()
        parser.read("%s/config/cmdb.cfg" % os.path.join(os.path.dirname(__file__), '..'))
        return parser
