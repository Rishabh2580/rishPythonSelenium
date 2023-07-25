import time
from selenium.webdriver.common.by import By

from Config import config
from Pages import Register, Contactus, Login
from conftest import setUpAutomation
from unittest import TestCase

class email(TestCase):
    def setUp(self) -> None:
        self.obj = setUpAutomation()
        #self.obj.open_browser()
    def test_addNewAccountForUser(self):
        driver = self.obj.open_browser()


        driver.implicitly_wait(15)
        time.sleep(5)
        driver.find_element(By.XPATH, "//*[@id='loginPanel']/p[2]/a").click()
        actual_title = driver.title
        print(actual_title)
        driver.find_element(By.NAME, Login.Username).send_keys("Rishabh")
        driver.find_element(By.NAME, Login.Password).send_keys("1232")
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, Login.LoginButton).click()

        time.sleep(5)

        try:
            assert actual_title == config.expected_title_login
            print("The title of the login page is " + actual_title)
        except Exception as e:
            print(repr(e))
            print("the title of the page is not as expected")

    def tearDown(self) -> None:
        self.obj.closeBrowser()