import os
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By


class TestRectangle():
    PATH = "https://high-flyer.hu/hetihazi/feladat1_teglalap.html"

    def setup_method(self):
        options = ChromeOptions()
        options.add_experimental_option('detach', True)
        self.browser = webdriver.Chrome(options=options)
        self.browser.get(TestRectangle.PATH)
        self.browser.maximize_window()

    def teardown_method(self):
        self.browser.quit()

    def test_fill_valid(self):
        input_a = self.browser.find_element(By.ID, 'a')
        input_a.send_keys('74')
        input_b = self.browser.find_element(By.ID, 'b')
        input_b.send_keys('32')
        button_calc = self.browser.find_element(By.ID, 'submit')
        button_calc.click()
        assert self.browser.find_element(By.ID, 'result').text == '212'

    def test_fill_invalid(self):
        input_a = self.browser.find_element(By.ID, 'a')
        input_a.send_keys('kiskutya')
        input_b = self.browser.find_element(By.ID, 'b')
        input_b.send_keys('32')
        button_calc = self.browser.find_element(By.ID, 'submit')
        button_calc.click()
        assert self.browser.find_element(By.ID, 'result').text == 'NaN'

    def test_no_fill(self):
        button_calc = self.browser.find_element(By.ID, 'submit')
        button_calc.click()
        assert self.browser.find_element(By.ID, 'result').text == 'NaN'
