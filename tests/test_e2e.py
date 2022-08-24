import time

from selenium.webdriver.common.by import By

from config.con import TestData
from pageobject.checkout import Checkout
from pageobject.homepage import Home
from utilities.BasePage import BasePage


class Test_e2e(BasePage):

    def test_home(self, param):
        # self.driver.implicit_wait(10)
        home = Home(self.driver)
        home.homePage(self.param)
        home.product()

    def test_sign(self, param):
        check = Checkout(self.driver)
        check.frame_switch()
        time.sleep(2)
        check.buy_product()
        check.email().send_keys(self.param['email'])
        check.continue_c()
        time.sleep(2)
        check.password().send_keys(self.param['password'])
        check.sigin()
        time.sleep(2)
        try:
            msg = check.message()
            if TestData.text1 in msg:
                # assert (TestConfig.text1 in message)
                self.message_logging(TestData.text1)
            elif TestData.text2 in msg:
                # assert (TestConfig.text2 in message)
                self.message_logging(TestData.text2)
        except Exception as e:
            raise e
        check.close_tab()
