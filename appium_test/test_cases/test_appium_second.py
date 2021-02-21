from appium_test.page.main_page import MainPage


class TestAppiumSecond:

    def setup(self):
        self.main = MainPage()

    def test_add_member(self):
        name = "zhangqin5"
        username = "zhangqin5"
        gender = '女'
        phone = '18723123455'
        toast = self.main.goto_contact_page().goto_add_member_page().goto_manual_add_member_page().\
            add_member_info(name, username, gender, phone).get_toast_text()
        assert toast == '添加成功'

    def teardown(self):
        self.main.close()
