from appium_test.commons.base import BasePage
from appium.webdriver.common.mobileby import MobileBy

from appium_test.page.add_member_page import AddMemberPage


class ContactPage(BasePage):

    """
       通讯录界面，点击添加人员，跳转到添加成员界面
    """

    def goto_add_member_page(self):
        self.find_and_click((MobileBy.ANDROID_UIAUTOMATOR,
                             'new UiScrollable(new UiSelector().'
                             'scrollable(true).instance(0)).'
                             'scrollIntoView(new UiSelector().'
                             'text("添加成员").instance(0));'))
        return AddMemberPage(self._driver)
