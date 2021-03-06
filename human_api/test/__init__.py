import logging

import connexion
from flask_testing import TestCase

from human_api.encoder import JSONEncoder


class BaseTestCase(TestCase):
    def create_app(self):
        self.LOG = logging.getLogger('connexion.operation')
        self.LOG.setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../swagger/')
        app.app.json_encoder = JSONEncoder
        app.add_api('swagger.yaml', pythonic_params=True)
        return app.app
