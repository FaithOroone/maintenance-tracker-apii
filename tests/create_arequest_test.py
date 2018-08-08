from users.views import app
import unittest
import json
from unittest import TestCase

class Test(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.request_data ={
            "name":"faith",
            "request_id:"12345"
            "category":"chair",
            "request_type":"repair",
            "description":"replace a broken chair",
            "department":"it",
            "status":"approved"
        }

    def test_create_request(self):
        res = self.app.post('/api/v1/users/request',data = json.dumps(self.request_data),content_type = 'application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn("we have recieved your request. Thank you", str(res.data))

    if __name__ == '__main__':
        unittest.main()