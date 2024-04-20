import unittest

import sys
sys.path.append('../datatellers/api')
from api import app

import json

api = '/api/card-scheme/stats'

def isJson(string):
    try:
        json.loads(string)
        return True
    except ValueError: return False


class Api2TestCase(unittest.TestCase):
    def test_api_exists(self):
        response = self.app.get(api)
        self.assertNotEqual(404, response.status_code)


    def test_api_success(self):
        response = self.app.get(api)
        self.assertEqual(200, response.status_code)


    def test_response_json(self):
        response = self.app.get(api)
        self.assertTrue(isJson(response.text))

    def test_json_attributes(self):
        #first, simulate request
        self.app.get('/api/card-scheme/verify/'+"45717360")

        #now, check json
        start = 1
        limit = 1
        
        response = self.app.get(api+f'?start={start}&limit={limit}')
        responseJson = json.loads(response.text)

        self.assertTrue(isinstance(responseJson["success"], bool))

        if responseJson["success"]:
            self.assertEqual(start, responseJson["start"])
            self.assertEqual(limit, responseJson["limit"])

            #I will test the payload size later

            self.assertTrue(isinstance(responseJson["payload"], dict))
            self.assertEqual(responseJson["payload"], {"45717360":1})#theres only 1 card tested so far


    def test_multiple_calls(self):
        #first, simulate request
        self.app.get('/api/card-scheme/verify/'+"45717360")
        self.app.get('/api/card-scheme/verify/'+"45717361")
        self.app.get('/api/card-scheme/verify/'+"45717362")
        self.app.get('/api/card-scheme/verify/'+"45717363")

        #now, check json
        start = 1
        limit = 3
        
        response = self.app.get(api+f'?start={start}&limit={limit}')
        responseJson = json.loads(response.text)

        self.assertTrue(isinstance(responseJson["success"], bool))

        if responseJson["success"]:
            self.assertEqual(start, responseJson["start"])
            self.assertEqual(limit, responseJson["limit"])

            #I will test the payload size later

            self.assertTrue(isinstance(responseJson["payload"], dict))
            testPayload = {"45717360":2, "45717361":1, "45717362":1}
            self.assertEqual(responseJson["payload"], testPayload)#Note that the first call was called 1 more time before


    def test_payload_size(self):
        #there are already multiple requests made, so I'll call the api directly
        start = 1
        limit = 3
        
        response = self.app.get(api+f'?start={start}&limit={limit}')
        responseJson = json.loads(response.text)

        self.assertTrue(isinstance(responseJson["success"], bool))

        if responseJson["success"]:
            self.assertEqual(start, responseJson["start"])
            self.assertEqual(limit, responseJson["limit"])

            #according to a site I checked, this payload {'45717360': 2, '45717361': 1, '45717362': 1}
            #must have a size of 45B

            self.assertEqual(45,responseJson["size"])


    #named aaa so that it runs first
    def test_aaa_serialization(self):
        #now, check json
        start = 1
        limit = 3
        
        response = self.app.get(api+f'?start={start}&limit={limit}')
        responseJson = json.loads(response.text)

        self.assertTrue(isinstance(responseJson["success"], bool))

        if responseJson["success"]:
            self.assertEqual(start, responseJson["start"])
            self.assertEqual(limit, responseJson["limit"])
            self.assertEqual(45,responseJson["size"])
            self.assertTrue(isinstance(responseJson["payload"], dict))
            testPayload = {"45717360":2, "45717361":1, "45717362":1}
            self.assertEqual(responseJson["payload"], testPayload)


    def setUp(self):
        self.app = app.test_client(self)

if __name__ == '__main__':
    unittest.main()