import logging
import time
from logging import exception

from config.con import TestData
from pageobject.checkout import Checkout
from pageobject.homepage import Home
from utilities.BasePage import BasePage


class Test_e2e(BasePage):

    def test_amazon_end_to_end(self, param):

        try:

            home = Home(self.driver)
            if home.is_search_box_present():

                home.homePage(param)
                self.message_logging("search is done")
            else:
                self.message_logging("search box is not present")

            results = home.get_result()
            for result in results:
                self.message_logging(result.text)

            # switch to the fourth searched items
            home.click_item()
            home.scroll()

            check = Checkout(self.driver)
            check.frame_switch()
            self.message_logging("change window")
            time.sleep(2)
            check.product_title()
            if check.is_buy_button_present():
                self.wait_clickable(Checkout.BUY_BUTTON)
                check.buy_product()
                self.message_logging("button is present")
                time.sleep(2)

                check = Checkout(self.driver)
                check.email().send_keys(param['email'])
                self.message_logging("send mail")
                self.wait_clickable(Checkout.CONTINUE)
                check.continue_c()
                self.message_logging("continue")
                time.sleep(2)
                check.password().send_keys(param['password'])
                self.message_logging("send password")
                self.wait_clickable(Checkout.SIGN_IN)
                check.sigin()
                self.message_logging("signin")
                time.sleep(2)

                msg = check.message()
                if TestData.text1 in msg:
                    # assert (TestConfig.text1 in message)
                    msg = self.message_logging(TestData.text1)
                    self.message_logging(f"send msg:.{msg}")

                elif TestData.text2 in msg:
                    # assert (TestConfig.text2 in message)
                    self.message_logging(TestData.text2)
                    self.message_logging(f"send msg:.{msg}")

            else:

                check.close_tab()

        except Exception as error:
            raise error
