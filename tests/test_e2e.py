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
        self.message_logging("search done")
        home.product()

    def test_sign(self, param):
        check = Checkout(self.driver)
        check.frame_switch()
        self.message_logging("change window")
        time.sleep(2)
        check.buy_product()
        self.message_logging("successfully click on buy now")
        check.email().send_keys(self.param['email'])
        self.message_logging("send mail")
        check.continue_c()
        self.message_logging("continue")

        time.sleep(2)
        check.password().send_keys(self.param['password'])
        self.message_logging("send password")

        check.sigin()
        self.message_logging("signin")

        time.sleep(2)
        try:
            msg = check.message()
            if TestData.text1 in msg:
                # assert (TestConfig.text1 in message)
                msg = self.message_logging(TestData.text1)
                self.message_logging(f"send msg:.{msg}")

            elif TestData.text2 in msg:
                # assert (TestConfig.text2 in message)
                self.message_logging(TestData.text2)
                self.message_logging(f"send msg:.{msg}")

        except Exception as e:
            raise e
        check.close_tab()
