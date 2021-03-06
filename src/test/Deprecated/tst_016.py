# -*- coding: utf-8 -*-
'''
Created on 11 oct. 2019

@author: Luisa

video 31 keys

'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




class Test_015(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        # INGRESO A LA APP
        self.driver.get("https://www.google.com.ar/")

    def test_015(self):

        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys("Curso de Selenium en Udemy")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys(Keys.ARROW_DOWN)
        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys(Keys.ENTER)
        time.sleep(6)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()