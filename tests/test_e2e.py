import time

from selenium.webdriver.common.by import By

from config.con import TestData
from pageobject.checkout import Checkout
from pageobject.homepage import Home
from utilities.BasePage import BasePage


class Test_e2e(BasePage):

    def test_home(self):
        # self.driver.implicit_wait(10)
        home = Home(self.driver)
        home.homePage()
        home.product()

    def test_sign(self):
        check = Checkout(self.driver, self.email, self.password)
        check.frame_switch()
        check.buy_product()

        # +BasePage.wait_presence(self.driver.find_element(*Checkout.EMAIL))
        check.email()
        check.continue_c()
        time.sleep(2)
        check.password()
        check.sigin().click()
        time.sleep(2)
        msg = check.message().text
        assert msg == "Your password is incorrect"
        check.close_tab()
