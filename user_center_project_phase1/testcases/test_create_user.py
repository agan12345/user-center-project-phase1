import unittest

from user_center_project_phase1.config.settings import BASE_URL, headers
from user_center_project_phase1.utils.request_util import RequestHandler


class TestCreateUser(unittest.TestCase):
    name = "morpheus"
    job = "leader"
    def setUp(self):
        self.req = RequestHandler()
        self.url = f"{BASE_URL}/users"
        self.headers = headers

    def test_create_user_success(self):
        payload = {
            "name": self.name,
            "job": self.job
        }
        resp = self.req.send("post", self.url,headers=self.headers, json=payload)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.json().get("name"), 'morpheus',"键值对不匹配name:morpheus")
        self.assertEqual(resp.json().get("job"), "leader", "键值对不匹配job:leader")
        self.assertIn("createdAt",resp.json())


if __name__ == "__main__":
    unittest.main()