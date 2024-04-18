import unittest

class ApiTestCase(unittest.TestCase):
    def test_one(self):
        self.assertTrue(True)

    def test_api_exists(self):
        api = '/api/card-scheme/verify/'
        
        response = self.app.get(api)

        self.assertEqual(200, response.status_code)

if __name__ == '__main__':
    unittest.main()