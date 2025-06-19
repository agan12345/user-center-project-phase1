import unittest

from user_center_project_phase1.config.settings import BASE_URL, headers
from user_center_project_phase1.utils.request_util import RequestHandler


class TestUpdataUser(unittest.TestCase):
    name = "morpheus"
    job = "zion resident"
    def setUp(self):
        self.req = RequestHandler()
        self.url = f"{BASE_URL}/users/2"
        self.headers = headers

    def test_put_user_success(self):
        payload = {
            "name": self.name,
            "job": self.job
        }
        resp = self.req.send("put", self.url,headers=self.headers, json=payload)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json().get("name"), 'morpheus',"键值对不匹配name:morpheus")
        self.assertEqual(resp.json().get("job"), "zion resident", "键值对不匹配job:zion resident")
        self.assertIn("updatedAt",resp.json())
        self.assertLess(resp.elapsed.total_seconds(), 2,'接口响应时间超过2s')


if __name__ == "__main__":
    unittest.main()