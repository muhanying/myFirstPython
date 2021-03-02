from test_frame.App_page import AppPage


class TestCaseFrame:
    def setup(self):
        self.app = AppPage()

    def teardown(self):
        self.app.close()

    def test_black(self):
        self.app.start().goto_main().goto_search_page().goto_market_page()