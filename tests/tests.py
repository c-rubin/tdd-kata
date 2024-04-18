import unittest

#import the api file
import sys
sys.path.append('../datatellers')
from api.api import app

class ApiTestCase(unittest.TestCase):
    def test_one(self):
        self.assertTrue(True)

    def test_api_exists(self):
        api = '/api/card-scheme/verify/'
        
        response = self.app.get(api)

        self.assertNotEqual(404, response.status_code)

    def setUp(self):
        self.app = app.test_client(self)

if __name__ == '__main__':
    unittest.main()