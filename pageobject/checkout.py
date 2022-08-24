from selenium.webdriver.common.by import By

from config.con import TestData


class Checkout:
    BUY_BUTTON = (By.XPATH, "//input[@id='buy-now-button']")
    EMAIL = (By.XPATH, "//input[@id='ap_email']")
    PASSWORD = (By.XPATH, "//input[@id='ap_password']")
    SIGN_IN = (By.XPATH, "//input[@id='signInSubmit']")
    MESSAGE = (By.XPATH, "//span[@class='a-list-item']")
    CONTINUE = (By.XPATH, "//input[@id='continue']")
    excpt = (By.XPATH, "//span[@class='a-list-item']")

    def __init__(self, driver):
        self.driver = driver

    def frame_switch(self):
        windowsopened = self.driver.window_handles
        print(len(windowsopened))
        return self.driver.switch_to.window(windowsopened[1])

    def buy_product(self):
        return self.driver.find_element(*Checkout.BUY_BUTTON).click()

    def email(self):
        return self.driver.find_element(*Checkout.EMAIL)


    def continue_c(self):
        return self.driver.find_element(*Checkout.CONTINUE).click()

    def password(self):
        return self.driver.find_element(*Checkout.PASSWORD)


    def sigin(self):
        self.driver.find_element(*Checkout.SIGN_IN).click()

    def message(self):
            return self.driver.find_element(*Checkout.MESSAGE).text


    def close_tab(self):
        windowsopen = self.driver.window_handles
        self.driver.close()
        self.driver.switch_to.window(windowsopen[0])
