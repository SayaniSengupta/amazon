from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Home:
    SEARCH_BAR = (By.XPATH, "//input[@id = 'twotabsearchtextbox']")
    select_fourth = (
    By.XPATH, "(//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'])[2]")

    def __init__(self, driver):
        self.driver = driver

    def homePage(self, param):
        self.driver.find_element(*Home.SEARCH_BAR).send_keys(param['search_item'])
        self.driver.find_element(*Home.SEARCH_BAR).send_keys(Keys.ENTER)

    def product(self):
        self.driver.find_element(*Home.select_fourth).click()
