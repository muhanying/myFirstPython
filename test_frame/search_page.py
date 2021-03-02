from selenium.webdriver.common.by import By

from test_frame.base_page import BasePage


class SearchPage(BasePage):

    def goto_market_page(self):
        self.find_and_click((By.XPATH, "//*[@text='行情']"))
        pass
