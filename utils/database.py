import ConfigParser
import os
import yaml

class Database(object):
    def load_config(self):
        try:
            config = open("%s/config/cmdb.yml" %
                os.path.join(os.path.dirname(__file__), '..'))
            return yaml.load(config)['database']
        except LoadError:
            print "Ensure config/cmdb.yml exists"
            return None
