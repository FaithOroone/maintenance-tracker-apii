import unittest
import json
from unittest import TestCase
from users.views import app


class loginTest(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.user_data = {
            "email":"agemo@gmail.com",
            "password":"password"
        }

    def test_user_login(self):
        res = self.app.post('api/v1/auth/login',data = json.dumps(self.user_data), content_type = 'application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn("you have successfully logged in.", str(res.data))