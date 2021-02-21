from appium.webdriver.common.mobileby import MobileBy

from appium_test.commons.base import BasePage
from appium_test.page.contact_page import ContactPage


class MainPage(BasePage):
    """
      消息页，点击通讯录进入，通讯录界面
    """

    def goto_contact_page(self):
        self.find_and_click((MobileBy.XPATH, "//*[@text='通讯录']"))
        return ContactPage(self._driver)
