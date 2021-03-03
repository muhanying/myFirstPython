from test_frame.market_page import MarketPage
from test_frame.search_page import SearchPage
from test_frame.base_page import BasePage


class MainPage(BasePage):

    def goto_search_page(self):
        self.to_steps("../test_frame/main_page.yaml", "goto_search_page")
        # self.find_and_click((By.ID, "com.xueqiu.android:id/tv_search"))
        return SearchPage(self._driver)

    def goto_market_page(self):
        self.to_steps("../test_frame/main_page.yaml", "goto_market_page")
        # self.find_and_click((By.XPATH, "//*[@text='行情']"))
        return MarketPage(self._driver)
