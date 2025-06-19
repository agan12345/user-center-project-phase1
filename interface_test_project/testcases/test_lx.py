import unittest
from interface_test_project.utils.request_util import RequestUtil


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.req = RequestUtil()
        self.base_url = "https://jsonplaceholder.typicode.com"

    def test_get_post(self):
        url = f"{self.base_url}/posts/2"
        resp = self.req.send_request("get", url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], 1)
        print(resp.text)

    def test_create_post(self):
        url = f"{self.base_url}/posts"
        payload = {
            "title": "Test123",
            "body": "This is a test",
            "userId": 1
        }
        resp = self.req.send_request("post", url, json=payload)
        print(resp.json()["id"])
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.json()["title"], "Test123")
    def test_get_post2(self):
        params = {
            "userId": 1
        }
        url = f"{self.base_url}/posts/2"
        resp = self.req.send_request("get", url, params=params)
        self.assertEqual(resp.status_code, 200)
        print(resp.text)

if __name__ == "__main__":
    unittest.main()
