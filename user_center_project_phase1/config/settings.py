import os

# 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Excel 数据路径
REGISTER_EXCEL_PATH = os.path.join(BASE_DIR, "data", "register_data.xlsx")


BASE_URL = "https://reqres.in/api"
headers = {
            "x-api-key": "reqres-free-v1",
            "Content-Type": "application/json",
        }