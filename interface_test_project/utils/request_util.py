import requests

class RequestUtil:
    def send_request(self, method, url, params=None, data=None, json=None, headers=None):
        method = method.lower()
        if method == "get":
            response = requests.get(url, params=params, headers=headers)
        elif method == "post":
            response = requests.post(url, data=data, json=json, headers=headers)
        else:
            raise ValueError("Unsupported HTTP method")
        return response
