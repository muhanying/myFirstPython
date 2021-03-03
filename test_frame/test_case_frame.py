import yaml
from selenium.webdriver.common.by import By

from test_frame.App_page import AppPage


class TestCaseFrame:
    def setup(self):
        self.app = AppPage()

    def teardown(self):
        self.app.close()

    def test_black(self):
        self.app.start().goto_main().goto_search_page().goto_market_page()

    def test_second_homework(self):
        self.app.start().goto_main().goto_market_page().goto_search_page().search_text()

    def test_demo(self):
        with open("./black_list.yaml") as f:
            black_list = yaml.load(f)
            for li in black_list:
                print(li)
        black_list1 = [(By.ID, "com.xueqiu.android:id/action_close")]
        for li2 in black_list1:
            print(li2)
