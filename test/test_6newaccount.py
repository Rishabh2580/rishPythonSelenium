import time
from selenium.webdriver.common.by import By

from Config import config
from Pages import Register, Contactus, Login, Opennewaccount
from conftest import setUpAutomation
from unittest import TestCase

class newaccountt(TestCase):
    def setUp(self) -> None:
        self.obj = setUpAutomation()
        #self.obj.open_browser()
    def test_addNewAccountForUser(self):
        driver = self.obj.open_browser()
        driver.find_element(By.XPATH, "//*[@id='loginPanel']/p[2]/a").click()
        actual_title = driver.title
        print(actual_title)
        driver.find_element(By.ID, Register.Firstname).send_keys("Risab")
        driver.implicitly_wait(5)
        driver.find_element(By.ID, Register.lastname).send_keys("sharma")
        driver.find_element(By.ID, Register.address_street).send_keys("ShivjiStreet")
        driver.find_element(By.ID, Register.city).send_keys("Gwalior")
        driver.find_element(By.ID, Register.state).send_keys("MP")
        driver.find_element(By.ID, Register.zip).send_keys("474001")
        driver.implicitly_wait(5)
        driver.find_element(By.ID, Register.phoneno).send_keys("859347")
        driver.find_element(By.ID, Register.customerssn).send_keys("5874504")
        driver.find_element(By.ID, Register.customeruser).send_keys("Rohan")
        driver.find_element(By.ID, Register.customerpass).send_keys("Riii")
        driver.implicitly_wait(10)
        driver.find_element(By.ID, Register.repeatedpass).send_keys("Riii")
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, Register.customerform).click()
        driver.implicitly_wait(15)
        driver.find_element(By.XPATH, Opennewaccount.openbutton).click()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, Opennewaccount.Account).click()
        driver.find_element(By.XPATH, Opennewaccount.Deposit).click()
        driver.find_element(By.CLASS_NAME, Opennewaccount.Button).click()

        try:
            assert actual_title == config.expected_title_login
            print("The title of the newaccountlogin page is " + actual_title)
        except Exception as e:
            print(repr(e))
            print("the title of the page is not as expected")

    def tearDown(self) -> None:
        self.obj.closeBrowser()
