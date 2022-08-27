from selenium.webdriver.common.by import By

from utilities.BasePage import BasePage


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
        """
         method to switch the frame
        """
        windowsopene = self.driver.window_handles
        print(len(windowsopene))
        return self.driver.switch_to.window(windowsopene[1])

    def is_buy_button_present(self):
        """
        method to check buy now button is present or not
        """
        button = self.driver.find_elements(*Checkout.BUY_BUTTON)
        present = False
        if len(button) >= 1:
            present = True
        return present

    def buy_product(self):
        """
        method to click on buy_now button
        """
        self.driver.find_element(*Checkout.BUY_BUTTON).click()

    def email(self):
        """
        method to pass the email-id
        """
        return self.driver.find_element(*Checkout.EMAIL)

    def continue_c(self):
        """
        method to click on the continue button
        """
        return self.driver.find_element(*Checkout.CONTINUE).click()

    def password(self):
        """
        method to pass the password
        """
        return self.driver.find_element(*Checkout.PASSWORD)

    def sigin(self):
        """
        method to click on the sign-in button
        """
        self.driver.find_element(*Checkout.SIGN_IN).click()

    def message(self):
        """
        method to take the warning text after clicking on sign-in button
        """
        return self.driver.find_element(*Checkout.MESSAGE).text

    def close_tab(self):
        """
        method to close the extra window opened
        """
        windowsopen = self.driver.window_handles
        self.driver.close()
        self.driver.switch_to.window(windowsopen[0])
