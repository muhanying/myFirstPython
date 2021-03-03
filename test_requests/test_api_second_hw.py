from test_requests.api.address_api import Address
import pytest


class TestSecondHW:
    def setup(self):
        self.address = Address()

    @pytest.mark.parametrize(("userid","username","alisa", "mobile", "department"),[("hello1","哈喽1","alisa", "13817772321", "1"),
                                                                                    ("hello2","哈喽2","alisa", "13817772322", "1"),
                                                                                    ("hello3","哈喽3","alisa", "13817772323", "1")])
    def test_create(self, userid, username, alisa, mobile, department):
        # 测试之前清理脏数据
        self.address.delete_member(userid)
        # 创建成员
        r = self.address.create_member(userid, username, alisa, mobile, department)
        assert r.get('errmsg', "创建成员失败") == "created"

