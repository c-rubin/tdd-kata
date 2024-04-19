import unittest

import sys
sys.path.append('../datatellers/api')
from api import app

api = '/api/card-scheme/stats'

class ApiTestCase(unittest.TestCase):
    def test_api_exists(self):
        response = self.app.get(api+"45717360")
        self.assertNotEqual(404, response.status_code)


    def test_api_success(self):
        response = self.app.get(api+"45717360")
        self.assertEqual(200, response.status_code)


    def setUp(self):
        self.app = app.test_client(self)

if __name__ == '__main__':
    unittest.main()