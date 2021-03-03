import requests


class Base:
    def __init__(self):
        corpid = "wwc19a406113733049"
        corpsecret = "Sdqz3RKfTjlxjKJDfb1tbNhsxVVhdeF2GPr0XJf6o98"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url)
        token = r.json().get("access_token")
        self.s = requests.session()
        self.s.params = {"access_token": token}

    def send_rq(self, method, url, **kwargs):
        r = self.s.request(method, url, **kwargs)
        return r.json()
