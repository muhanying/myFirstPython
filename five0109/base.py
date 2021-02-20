from selenium.webdriver.android import webdriver


class BaseComm:
    def setup_class(self):
        chrome_driver = "E:\\driver\\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_driver)
        self.driver.maximize_window()

    def teardown_class(self):
        self.driver.quit()
