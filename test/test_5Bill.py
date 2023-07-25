import time

import time
from selenium.webdriver.common.by import By

from Config import config
from Pages import Register, Contactus, BillPay
from conftest import setUpAutomation
from unittest import TestCase

class Bill(TestCase):
    def setUp(self) -> None:
        self.obj = setUpAutomation()
        #self.obj.open_browser()
    def test_addNewAccountForUser(self):
        driver = self.obj.open_browser()

        driver.implicitly_wait(15)
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//*[@id='loginPanel']/p[2]/a").click()
        actual_title = driver.title
        print(actual_title)
        driver.find_element(By.ID, BillPay.Firstnamee).send_keys("Risaab")
        driver.implicitly_wait(5)
        driver.find_element(By.ID, BillPay.lastnamee).send_keys("sharma")
        driver.find_element(By.ID, BillPay.address_streett).send_keys("ShivjiStreet")
        driver.find_element(By.ID, BillPay.cityy).send_keys("Gwalior")
        driver.find_element(By.ID, BillPay.statee).send_keys("MP")
        driver.find_element(By.ID, BillPay.zipp).send_keys("474001")
        driver.implicitly_wait(5)
        driver.find_element(By.ID, BillPay.phonenoo).send_keys("859347")
        driver.find_element(By.ID, BillPay.customerssnn).send_keys("5874504")
        driver.find_element(By.ID, BillPay.customeruserr).send_keys("Rk")
        driver.find_element(By.ID, BillPay.customerpasss).send_keys("Rl")
        driver.implicitly_wait(15)
        driver.find_element(By.ID, BillPay.repeatedpasss).send_keys("Rl")
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, BillPay.customerformm).click()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, BillPay.Billpay).click()
        driver.implicitly_wait(10)
        driver.find_element(By.NAME,BillPay.PayeeName).send_keys("Ramesh")
        driver.find_element(By.NAME,BillPay.Address).send_keys("shivnagar")
        driver.find_element(By.NAME, BillPay.CityName).send_keys("Mumbai")
        driver.find_element(By.NAME, BillPay.State).send_keys("Mumbai")
        driver.find_element(By.NAME, BillPay.ZipCode).send_keys("1021")
        driver.find_element(By.NAME, BillPay.Phoneno).send_keys("394839")
        driver.find_element(By.NAME, BillPay.Account).send_keys("XYZ")
        driver.find_element(By.NAME, BillPay.verifyAccount).send_keys("1231")
        driver.find_element(By.NAME, BillPay.Amount).send_keys("50000")
        driver.find_element(By.XPATH, BillPay.Fromaccount).send_keys("12432")
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, BillPay.SendButton).click()
        driver.implicitly_wait(5)

