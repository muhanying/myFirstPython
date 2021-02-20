from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from five0109.base import BaseComm


class TestSelenium(BaseComm):

    def test_wait(self):
        print("测试等待")

        def wait(x):
            return len(self.driver.find_element_by_id("")) >= 1

        # 显式等待,自定义
        WebDriverWait(self.driver, 10).until(wait)

        # 使用Python提供的
        expected_conditions.element_to_be_clickable("")

    def setup_class(self):
        chrome_driver = "E:\\driver\\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_driver)
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    def test_one(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("pytest")
        self.driver.find_element_by_id("su").click()
        time.sleep(2)

    def test_script(self):
        self.driver.get("http://www.baidu.com")
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
