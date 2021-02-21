from appium_test.commons.base import BasePage
from appium.webdriver.common.mobileby import MobileBy


class ManualMemberPage(BasePage):

    """
    手动录入成员信息界面，录入信息后保存，进入到添加成员界面
    """

    def add_member_info(self, name, username, gender, phone):
        from appium_test.page.add_member_page import AddMemberPage
        self.find_and_sendkey((MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText"),
                              name)
        self.find_and_sendkey((MobileBy.XPATH, "//*[contains(@text,'帐号')]/../android.widget.EditText"),
                              username)
        self.find_and_click((MobileBy.ID, "com.tencent.wework:id/eso"))
        if gender == '女':
            self.find_and_click((MobileBy.XPATH, "//*[@text='女']"))
        else:
            self.find_and_click((MobileBy.XPATH, "//*[@text='男']"))
        self.find_and_sendkey((MobileBy.ID, "com.tencent.wework:id/fwi"), phone)
        self.find_and_click((MobileBy.ID, "com.tencent.wework:id/aj_"))
        return AddMemberPage(self._driver)
