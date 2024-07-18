"""
1. Feladat: Keressük a téglalap kerületét

Készíts egy python applikációt (egy darab python file) ami selenium-ot használ.
Az ellenőrzésekhez pytest keretrendszert használj, valamint fontos az `assert` összehasonlítások használata is!

A program töltse be a téglalap kerülete app-ot. https://high-flyer.hu/hetihazi/feladat2_email.html

Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat a téglalap kerülete appban:

* Helyes kitöltés esete:
    * a: 74
    * b: 32
    * Eredmény: 212

* Nem számokkal történő kitöltés:
    * a: kiskutya
    * b: 32
    * Eredmény: NaN

* Üres kitöltés:
    * a: <üres>
    * b: <üres>
    * Eredmény: NaN
"""

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
