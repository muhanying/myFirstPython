from selenium.webdriver.common.by import By

from test_frame.base_page import BasePage
from test_frame.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search_page(self):
        self.to_steps("../test_frame/market_page.yaml", "goto_search_page")
        # self.find_and_click((By.ID, "com.xueqiu.android:id/action_search"))
        return SearchPage(self._driver)
