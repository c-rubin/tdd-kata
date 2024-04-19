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

    def test_response_json(self):
        cardNum = "45717360"

        response = self.app.get(api+cardNum)
        responseJson = json.loads(response.text)

        self.assertTrue(responseJson["success"])

        responseJson = responseJson["payload"]

        #testing data according to binlist.net
        self.assertEqual("Visa", responseJson["scheme"])
        self.assertEqual("Debit", responseJson["type"])
        self.assertEqual("Jyske Bank A/S", responseJson["bank"])

    def setUp(self):
        self.app = app.test_client(self)

if __name__ == '__main__':
    unittest.main()