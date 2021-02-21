from appium_test.commons.base import BasePage
from appium.webdriver.common.mobileby import MobileBy

from appium_test.page.manual_add_member_page import ManualMemberPage


class AddMemberPage(BasePage):

    """
    添加成员界面，点击手动输入添加，进入手动输入界面
    """

    def goto_manual_add_member_page(self):
        self.find_and_click((MobileBy.XPATH, "//*[@text='手动输入添加']"))
        return ManualMemberPage(self._driver)

    def get_toast_text(self):
        return self.find_and_gettext((MobileBy.XPATH, '//*[@class="android.widget.Toast"]'))
