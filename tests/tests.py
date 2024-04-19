import unittest

#import the api file
import sys
sys.path.append('../datatellers')
from api.api import app

import json

api = '/api/card-scheme/verify/'

def isJson(string):
        try:
            json.loads(string)
            return True
        except ValueError: return False

class ApiTestCase(unittest.TestCase):
    def test_one(self):
        self.assertTrue(True)

    def test_api_exists(self):
        
        
        response = self.app.get(api)

        self.assertNotEqual(404, response.status_code)

    def test_api_success(self):
        
        response = self.app.get(api)

        self.assertEqual(200, response.status_code)

    def test_response_json(self):
        response = self.app.get(api) 

        self.assertTrue(isJson(response.text))

    def setUp(self):
        self.app = app.test_client(self)

if __name__ == '__main__':
    unittest.main()