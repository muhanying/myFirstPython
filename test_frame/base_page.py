from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import yaml


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find_ele(self, by, locator=None):
        with open("./black_list.yaml") as f:
            black_list = yaml.load(f)
        # black_list = [(By.ID, "com.xueqiu.android:id/action_close")]
        try:
            if locator is None:
                result = self._driver.find_element(*by)
            else:
                result = self._driver.find_element(by, locator)
        except Exception as e:
            for loc in black_list:
                ele = self._driver.find_elements(*loc)
                if len(ele) > 0:
                    ele[0].click()
                    return self.find_ele(by)
                raise e
        return result

    def find_and_send_keys(self, by, text):
        self.find_ele(by).send_keys(text)

    def find_and_click(self, by):
        self.find_ele(by).click()

    def find_and_gettext(self, by):
        return self.find_ele(by).text

    def find_scroll_click(self, text):
        self.find_and_click((MobileBy.ANDROID_UIAUTOMATOR,
                             'new UiScrollable(new UiSelector().'
                             'scrollable(true).instance(0)).'
                             'scrollIntoView(new UiSelector().'
                             f'text("{text}").instance(0));'))

    def to_steps(self, t_path, option):
        with open(t_path, 'r', encoding="utf-8") as f:
            data = yaml.load(f)
        steps = data[option]

        for step in steps:
            if step["action"] == "find_and_click":
                self.find_and_click(step["locator"])
            elif step["action"] == "find_and_send_keys":
                self.find_and_send_keys(step["locator"], step["content"])

