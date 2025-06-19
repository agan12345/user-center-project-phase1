import requests

class RequestUtil:
    def send_request(self, method, url, **kwargs):
        method = method.lower()
        if method == "get":
            return requests.get(url, **kwargs)
        elif method == "post":
            return requests.post(url, **kwargs)
        elif method == "put":
            return requests.put(url, **kwargs)
        else:
            raise ValueError("暂不支持的请求方式")
