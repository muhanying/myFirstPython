import pytest
import yaml


def fun(x):
    return x + 1;


class TestPyTest:

    @pytest.mark.parametrize("a,excepted", [(3, 4), (4, 5)])
    def test_a(self, a, excepted):
        assert fun(a) == excepted

    @pytest.fixture()
    def login(self):
        userName = 'zq'
        return userName

    def test_b(self, login):
        print(f"tetb user= {login}")

    @pytest.mark.parametrize(("a", "b"), [("1", "2"), ("3", "4")])
    def test_c(self, a, b):
        print(a + b)

    @pytest.mark.parametrize(["a", "b"], yaml.safe_load(open("./data.yaml")))
    def test_yaml(self, a, b):
        print(a, b)

    @pytest.mark.parametrize(["env"], yaml.safe_load(open("./data2.yaml")))
    def test_yaml2(self, env):
        if "test" in env:
            print("this is ", env["test"])
        else:
            print("this is dev")

    @pytest.mark.demo
    def test_demo(self):
        print("测试标签 pytest -m 标签名")
