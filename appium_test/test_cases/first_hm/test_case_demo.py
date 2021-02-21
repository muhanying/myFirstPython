from appium.webdriver.common.mobileby import MobileBy

from appium_test.commons.base import BasePage


class TestDemo:
    def setup(self):
        self.base = BasePage()

    def test_add_member(self):
        self.base.find_and_click((MobileBy.XPATH, "//*[@text='通讯录']"))
        self.base.find_and_click((MobileBy.ANDROID_UIAUTOMATOR,
                                  'new UiScrollable(new UiSelector().'
                                  'scrollable(true).instance(0)).'
                                  'scrollIntoView(new UiSelector().'
                                  'text("添加成员").instance(0));'))
        self.base.find_and_click((MobileBy.XPATH, "//*[@text='手动输入添加']"))
        self.base.find_and_sendkey((MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText"), "zhangqin2")
        self.base.find_and_sendkey((MobileBy.XPATH, "//*[contains(@text,'帐号')]/../android.widget.EditText"), "zhangqin2")
        self.base.find_and_click((MobileBy.ID, "com.tencent.wework:id/eso"))
        self.base.find_and_click((MobileBy.XPATH, "//*[@text='女']"))
        self.base.find_and_sendkey((MobileBy.ID, "com.tencent.wework:id/fwi"), "18721901111")
        self.base.find_and_click((MobileBy.ID, "com.tencent.wework:id/aj_"))
        toast = self.base.find_and_gettext((MobileBy.XPATH, "//*[@class='android.widget.Toast'']"))
        assert toast == '添加成功'

    def teardown(self):
        self.base.close()
