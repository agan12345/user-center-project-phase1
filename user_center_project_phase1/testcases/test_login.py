import unittest
from user_center_project_phase1.config.settings import BASE_URL, headers
from user_center_project_phase1.utils.request_util import RequestHandler


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.req = RequestHandler()
        self.url = f"{BASE_URL}/login"
        self.headers = headers

    def test_login_success(self):
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        resp = self.req.send("post", self.url, json=payload, headers=self.headers)
        self.assertEqual(resp.status_code, 200)
        self.assertIn("token", resp.json())

    def test_login_fail(self):
        payload = {
            "email": "peter@klaven"
        }
        resp = self.req.send("post", self.url, json=payload, headers=self.headers)
        self.assertEqual(resp.status_code, 400)
        self.assertIn("error", resp.json())

if __name__ == "__main__":
    unittest.main()