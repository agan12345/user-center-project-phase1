import unittest
from interface_test_project.utils.request_util import RequestUtil


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.req = RequestUtil()
        self.base_url = "https://jsonplaceholder.typicode.com"

    def test_get_post(self):
        url = f"{self.base_url}/posts/1"
        resp = self.req.send_request("get", url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], 1)

    def test_create_post(self):
        url = f"{self.base_url}/posts"
        payload = {
            "title": "Test",
            "body": "This is a test",
            "userId": 1
        }
        resp = self.req.send_request("post", url, json=payload)
        print(resp.text)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.json()["title"], "Test")
        self.assertEqual(resp.json()["id"],101)

if __name__ == "__main__":
    unittest.main()
