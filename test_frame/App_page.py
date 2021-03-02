from appium import webdriver

from test_frame.base_page import BasePage
from test_frame.main_page import MainPage


class AppPage(BasePage):
    def start(self):
        if self._driver is None:
            caps = dict()
            # com.tencent.wework/.launch.LaunchSplashActivity  com.xueqiu.android/.common.MainActivity
            caps["platformName"] = "android"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".common.MainActivity"
            # 不清除缓存
            caps["noReset"] = "true"
            caps['settings[waitForIdleTimeout]'] = 1

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            # 隐式等待
            self._driver.implicitly_wait(5)
        else:
            self._driver.launch_app()
        return self

    def restart(self):
        self._driver.quit()
        self._driver.launch_app()
        return self

    def close(self):
        self._driver.quit()
        return self

    def goto_main(self):
        return MainPage(self._driver)





