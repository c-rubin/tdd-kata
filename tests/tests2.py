import unittest

import sys
sys.path.append('../datatellers/api')
from api import app

import json

import pickle

api = '/api/card-scheme/stats'

cardsCheckedFile = "./api/cardsChecked.pkl"

def writeFile(cardsChecked):
        with open(cardsCheckedFile, 'wb') as f:
            pickle.dump(cardsChecked, f)
            f.close()

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
        #first, create a mock file which shall be read by the api
        testPayload = {"45717360":2, "45717361":1, "45717362":1}
        writeFile(testPayload)
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
            self.assertEqual(responseJson["payload"], testPayload)


        #Lets try some more calls and test again
        self.app.get('/api/card-scheme/verify/'+"45717360")
        self.app.get('/api/card-scheme/verify/'+"45717361")
        self.app.get('/api/card-scheme/verify/'+"45717362")
        self.app.get('/api/card-scheme/verify/'+"45717363")
        #testPayload = {"45717360":2+1=3, "45717361":1+1=2, "45717362":1+1=2}
        testPayload = {"45717360":3, "45717361":2, "45717362":2}

        #now, check json again
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
            self.assertEqual(responseJson["payload"], testPayload)

        #finally, set mock to empty (thus its not mock anymore, but serves as real memory)
        writeFile({})


    def setUp(self):
        self.app = app.test_client(self)

if __name__ == '__main__':
    unittest.main()