import ConfigParser
import os
import yaml

class Database(object):
    """ Generic class for handling database-related tasks. """
    def load_config(self):
        """ Pull the configuration off disk and parse the yml. Returns a dict
        containing a subset of the yml from the 'database' section. """
        try:
            config = open("%s/config/cmdb.yml" %
                os.path.join(os.path.dirname(__file__), '..'))
            return yaml.load(config)['database']
        except LoadError:
            print "Ensure config/cmdb.yml exists"
            return None
