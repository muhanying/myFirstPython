import requests


class TestApiFirst:

    def setup(self):
        self.corpid = "xxx"
        self.corpsecret = "xxxx"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.corpid}&corpsecret={self.corpsecret}"
        r = requests.get(url)
        self.token = r.json()["access_token"]

    def test_member_api(self):
        self.user_id = "zhangqin7"
        create_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        query_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={self.user_id}"
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        delete_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={self.user_id}"

        create_body = {
            "userid": f"{self.user_id}",
            "name": "张三",
            "alias": "zhangqin",
            "mobile": "+86 13800000007",
            "department": [1]
        }
        # 创建成员
        r = requests.post(create_url, json=create_body)
        assert r.json()['errmsg'] == "created"
        # 查询成员
        get_r = requests.get(query_url)
        assert get_r.json()['name'] == "张三"

        update_body = {
            "userid": f"{self.user_id}",
            "name": "张三update",
            "alias": "zhangqin",
            "mobile": "+86 13800000007",
            "department": [1],
        }

        # 更新成员
        r = requests.post(update_url, json=update_body)
        assert r.json()['errmsg'] == "updated"
        # 查询成员
        get_update_r = requests.get(query_url)
        assert get_update_r.json()['errmsg'] == "张三update"

        # 删除成员
        requests.get(delete_url)
        # 查询成员
        get_delete_r = requests.get(query_url)
        assert get_delete_r.json()['errmsg'].find("userid not found") == 0
