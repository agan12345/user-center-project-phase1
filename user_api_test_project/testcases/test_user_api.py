import unittest
from user_api_test_project.utils.request_util import RequestUtil


class TestUserAPI(unittest.TestCase):
    def setUp(self):
        self.req = RequestUtil()
        self.base_url = "https://jsonplaceholder.typicode.com"  # 模拟接口
        self.token = "模拟token123"

    def test_get_user(self):
        url = f"{self.base_url}/users/1"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = self.req.send_request("get", url, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn("username", response.text)

    def test_modify_user_nickname(self):
        url = f"{self.base_url}/posts/1"  # 模拟PUT接口
        payload = {"nickname": "新昵称"}
        headers = {"Authorization": f"Bearer {self.token}"}
        response = self.req.send_request("put", url, json=payload, headers=headers)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
