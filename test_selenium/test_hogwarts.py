from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHogwarts:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com/")
        # todo: 隐式等待
        self.driver.implicitly_wait(10)      # 隐式等待

    def test_hogwarts(self):
        self.driver.find_element(By.LINK_TEXT, '社团').click()

        # todo: 显式等待
        element = (By.PARTIAL_LINK_TEXT, '霍格沃兹测试学院')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()
        # self.driver.find_element(By.CSS_SELECTOR, '[data-name=霍格沃兹测试学院]').click()

        self.driver.find_element(By.CSS_SELECTOR, '.topic:nth-child(1) .title a').click()

    def teardown_method(self):
        sleep(3)
        self.driver.quit()