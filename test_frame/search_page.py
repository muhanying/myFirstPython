from selenium.webdriver.common.by import By

from test_frame.base_page import BasePage


class SearchPage(BasePage):

    def goto_market_page(self):
        self.to_steps("../test_frame/search_page.yaml", "goto_market_page")
        # self.find_and_click((By.XPATH, "//*[@text='行情']"))
        pass

    def search_text(self):
        self.to_steps("../test_frame/search_page.yaml", "search_text")
        # self.find_and_send_keys((By.ID, "com.xueqiu.android:id/search_input_text"), "工商银行")
        # self.find_and_click((By.XPATH, "//*[@text='SH601398']"))
