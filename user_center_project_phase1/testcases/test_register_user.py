import unittest
from ddt import ddt,data
from user_center_project_phase1.config.settings import BASE_URL, headers, REGISTER_EXCEL_PATH
from user_center_project_phase1.utils.excel_util import read_excel_data
from user_center_project_phase1.utils.request_util import RequestHandler

test_data = read_excel_data(REGISTER_EXCEL_PATH)
print(test_data)

@ddt
class TestRegisterUser(unittest.TestCase):
    def setUp(self):
        self.req = RequestHandler()
        self.url = f"{BASE_URL}/register"
        self.headers = headers
    # @data(
    #     {"email": "eve.holt@reqres.in", "password": "pistol", "expected_status": 200, "expect_token": True},
    #     {"email": "eve.holt@reqres.in", "password": "", "expected_status": 400, "expect_token": False},
    #     {"email": "", "password": "pistol", "expected_status": 400, "expect_token": False},
    #     {"email": "invalid@example.com", "password": "123456", "expected_status": 400, "expect_token": False},
    # )

    @data(*test_data)
    def test_register_success(self, case):
        print("测试数据：%s" % case)
        payload = {
            "email": case['email'],
            "password": case['password']
        }
        resp = self.req.send("post", self.url,headers=self.headers, json=payload)

        self.assertEqual(resp.status_code, case["expected_status"], f"状态码错误，期望{case['expected_status']}，实际{resp.status_code}")
        if case["expect_token"]:
            self.assertIn("token", resp.json(), "期望存在token字段，但未找到")
        else:
            self.assertIn("error", resp.json(), "期望存在error字段，但未找到")

        self.assertLess(resp.elapsed.total_seconds(), 2,'接口响应时间超过2s')


if __name__ == "__main__":
    unittest.main()