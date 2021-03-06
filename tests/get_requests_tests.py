import unittest
from users.views import app
from unittest import TestCase
import json

class RequestsTest(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.request_data ={
            "name":"faith",
            "category":"laptop",
            "request_type":"repair",
            "description":"install new software",
            "department":"it",
            "request_id":"dsoius",
            "status":"approved"
        }
    def testfetchrequests(self):
        res = self.app.post('api/v1/users/requests', data = json.dumps(self.request_data),content_type = 'application/json' )
        res = self.app.get('/api/v1/user/requests', data = json.dumps(self.request_data),content_type = 'application/json')
        self.assertEqual(res.status_code, 302)
        self.assertIn('you have successfully fetched requests', str(res.data))

if __name__ == '__main__':
        unittest.main()