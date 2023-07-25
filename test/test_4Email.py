import time
from selenium.webdriver.common.by import By

from Config import config
from Pages import Register, Contactus
from conftest import setUpAutomation
from unittest import TestCase

class email(TestCase):
    def setUp(self) -> None:
        self.obj = setUpAutomation()
        #self.obj.open_browser()
    def test_addNewAccountForUser(self):
        driver = self.obj.open_browser()


        driver.implicitly_wait(15)

        driver.find_element(By.XPATH, "//*[@id='loginPanel']/p[2]/a").click()
        actual_title = driver.title
        print(actual_title)
        driver.find_element(By.XPATH, Contactus.contactus).click()
        driver.implicitly_wait(5)
        driver.find_element(By.NAME, Contactus.name).send_keys("rishabh")
        driver.find_element(By.NAME, Contactus.email).send_keys("rishabh121@gmail.com")
        driver.find_element(By.NAME, Contactus.phone).send_keys("12232")
        driver.find_element(By.NAME,Contactus.Message).send_keys("How ARE YOU")
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, Contactus.send).click()
