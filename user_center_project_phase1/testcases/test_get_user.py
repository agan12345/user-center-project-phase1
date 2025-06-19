import unittest

from user_center_project_phase1.config.settings import BASE_URL, headers
from user_center_project_phase1.utils.request_util import RequestHandler


class TestGetUserInfo(unittest.TestCase):
    def setUp(self):
        self.req = RequestHandler()
        self.url = f"{BASE_URL}/users/2"
        self.headers = headers

    def test_get_userinfo(self):
        resp = self.req.send("get", self.url,headers=self.headers)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["data"]["id"], 2,f"响应码异常：{resp.status_code}")
        self.assertEqual(resp.json()["data"]["email"], "janet.weaver@reqres.in", "用户id不匹配")


if __name__ == "__main__":
    unittest.main()