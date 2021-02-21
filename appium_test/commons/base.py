from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver = None):
        if driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"
            caps['settings[waitForIdleTimeout]'] = 1

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver

    def find_ele(self, by, locator=None):
        if locator is None:
            result = self._driver.find_element(*by)
        else:
            result = self._driver.find_element(by, locator)

        return result

    def find_and_sendkey(self, by, text):
        self.find_ele(by).send_keys(text)

    def find_and_click(self, by):
        self.find_ele(by).click()

    def find_and_gettext(self, by):
        self.find_ele(by).text

    def close(self):
        self._driver.quit()

