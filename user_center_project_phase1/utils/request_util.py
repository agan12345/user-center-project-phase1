import requests
from user_center_project_phase1.utils.log_util import logger  # ✅ 引入日志器

class RequestHandler:
    def __init__(self):
        self.session = requests.Session()

    def send(self, method, url, **kwargs):
        method = method.lower()

        # ✅ 打印请求日志
        logger.info(f"【请求方法】{method.upper()}")
        logger.info(f"【请求地址】{url}")
        logger.info(f"【请求参数】{kwargs}")

        if method == "get":
            resp = self.session.get(url, **kwargs)
        elif method == "post":
            resp = self.session.post(url, **kwargs)
        elif method == "put":
            resp = self.session.put(url, **kwargs)
        elif method == "delete":
            resp = self.session.delete(url, **kwargs)
        else:
            raise ValueError("Unsupported method")

        # ✅ 打印响应日志
        logger.info(f"【响应状态码】{resp.status_code}")
        logger.info(f"【响应内容】{resp.text}")
        logger.info("-" * 60)

        return resp
