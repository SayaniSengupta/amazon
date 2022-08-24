from selenium.webdriver.common.by import By


class Checkout:
    BUY_BUTTON = (By.XPATH, "//input[@id='buy-now-button']")
    EMAIL = (By.XPATH,"//input[@id='ap_email']")
    PASSWORD =(By.XPATH,"//input[@id='ap_password']")
    SIGN_IN = (By.XPATH,"//input[@id='signInSubmit']")
    MESSAGE = (By.XPATH,"//span[@class='a-list-item']")
    CONTINUE = (By.XPATH,"//input[@id='continue']")

    def __init__(self, driver, email, password):
        self.driver = driver
        self.email = email
        self.password = password

    def frame_switch(self):
        windowsopened = self.driver.window_handles
        print(len(windowsopened))
        return self.driver.switch_to.window(windowsopened[1])


    def buy_product(self):
        return self.driver.find_element(*Checkout.BUY_BUTTON).click()

    def email(self):
        return self.driver.find_element(*Checkout.EMAIL).send_keys(self.email)

    def continue_c(self):
        return self.driver.find_element(*Checkout.CONTINUE).click()

    def password(self):
        return self.driver.find_element(*Checkout.PASSWORD).send_keys(self.password)

    def sigin(self):
        self.driver.find_element(By.XPATH(*Checkout.SIGN_IN))

    def message(self):
        return self.driver.find_element(*Checkout.MESSAGE)

    def close_tab(self):
        windowsopen = self.driver.window_handles
        self.driver.close()
        self.driver.switch_to.window(windowsopen[0])
