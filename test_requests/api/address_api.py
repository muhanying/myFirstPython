from test_requests.api.base_api import Base


class Address(Base):
    def create_member(self, userid, username, alisa, mobile, department):
        create_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        create_body = {
            "userid": f"{userid}",
            "name": f"{username}",
            "alias": f"{alisa}",
            "mobile": f"{mobile}",
            "department": [department]
        }
        return self.send_rq("post", url=create_url, json=create_body)

    def query_member(self, userid):
        query_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}"
        return self.send_rq("get", url=query_url)

    def update_member(self, userid, username, alisa, mobile, department):
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        create_body = {
            "userid": f"{userid}",
            "name": f"{username}",
            "alias": f"{alisa}",
            "mobile": f"{mobile}",
            "department": [{department}]
        }
        return self.send_rq("post", url=update_url, json=create_body)

    def delete_member(self, userid):
        delete_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}"
        return self.send_rq("get", delete_url)
