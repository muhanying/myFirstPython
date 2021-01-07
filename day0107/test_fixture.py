import pytest

def test_one(login):
    print("one")
    print(f"登录用户信息 userName,pwd,token，{login}")


def test_two():
    print("不需要登录")


@pytest.mark.usefixtures("login")
def test_three():
    print("通过注解传入")


class TestFixture:
    def test_select(self, conDb):
        print("测试scope")
