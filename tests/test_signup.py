import unittest
import json
from users.views import app
from unittest import TestCase

class signupTest(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.user_data = {
            "first_name":"keren",
            "last_name":"agemo",
            "user_id":"12345",
            "email":"agemo@gmail",
            "password":"12345678",
            "confirm_password":"12345678"
        }

    def test_user_signup(self):
        res = self.app.post('/api/v1/auth/signup',data = json.dumps(self.user_data),content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn("you have successfully signed in.", str(res.data))

    if __name__ == '__main__':
        unittest.main()
