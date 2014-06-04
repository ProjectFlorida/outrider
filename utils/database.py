import ConfigParser
import os
import yaml

class Database(object):
    """ Generic class for handling database-related tasks. """

    def select_config_for_environment(self):
        """ Read the value of env variable and load the property
        database configuration based on the value of DB_ENV.

        Takes no input and returns a string like 'production' or 'testing'."""
        return os.getenv('DB_ENV', 'development')

    def load_config(self):
        """ Pull the configuration off disk and parse the yml. Returns a dict
        containing a subset of the yml from the 'database' section. """
        environment = self.select_config_for_environment()
        config_src = ("%s/config/settings.%s.yml" % (
            (os.path.join(os.path.dirname(__file__), '..')),
            environment))
        config = open(config_src)

        try:
            return yaml.load(config)['database']
        except IOError:
            print ("Ensure config/settings.%s.yml exists" % environment)
            return None
