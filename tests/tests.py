import unittest

#import the api file
import sys
sys.path.append('../datatellers/api')
from api import app

import json

api = '/api/card-scheme/verify/'
cardNum = '45717360'

def isJson(string):
        try:
            json.loads(string)
            return True
        except ValueError: return False

class ApiTestCase(unittest.TestCase):
    def test_one(self):
        self.assertTrue(True)


    def test_api_exists(self):
        response = self.app.get(api+cardNum)
        self.assertNotEqual(404, response.status_code)


    def test_api_success(self):
        response = self.app.get(api+cardNum)
        self.assertEqual(200, response.status_code)


    def test_response_json(self):
        response = self.app.get(api+cardNum) 
        self.assertTrue(isJson(response.text))


    def test_response_json(self):
        response = self.app.get(api+cardNum)
        responseJson = json.loads(response.text)

        self.assertTrue(isinstance(responseJson["success"], bool))

        if responseJson["success"]:
            responseJson = responseJson["payload"]

            #testing data according to binlist.net
            self.assertEqual("visa", responseJson["scheme"])
            self.assertEqual("debit", responseJson["type"])
            self.assertEqual("Jyske Bank A/S", responseJson["bank"])


    def setUp(self):
        self.app = app.test_client(self)

if __name__ == '__main__':
    unittest.main()