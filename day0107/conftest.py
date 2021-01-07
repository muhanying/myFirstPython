import pytest

# 可以把公共配置放到一个文件里  文件名 有且只能为conftest,且只能在用例所在包下
@pytest.fixture()
def login():
    print("登录")
    userName = "zq"
    pwd = "123"
    token = "12ddds"
    yield [userName, pwd, token]
    print("退出")


# scope:``"function (default), ``"class"``, ``"module"``, ``"package"`` or ``"session"``
@pytest.fixture(scope="class")
def conDb():
    print("连接")
    yield
    print("断开")
