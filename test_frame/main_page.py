from selenium.webdriver.common.by import By

from test_frame.search_page import SearchPage
from test_frame.base_page import BasePage


class MainPage(BasePage):

    def goto_search_page(self):
        self.find_and_click((By.ID, "com.xueqiu.android:id/tv_search"))
        return SearchPage(self._driver)
