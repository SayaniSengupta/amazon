from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utilities.BasePage import BasePage


class Home(BasePage):
    result = (By.TAG_NAME, "h2")
    SEARCH_BAR = (By.XPATH, "//input[@id = 'twotabsearchtextbox']")
    # PRODUCT_LIST = (By.XPATH, "//div[@class='a-section a-spacing-small a-spacing-top-small']/div/h2/a")
    item4 = (By.XPATH, "(//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style "
                       "a-text-normal'])[2]")

    def __init__(self, driver):
        self.driver = driver

    def is_search_box_present(self):
        """
         method to check search box is present or not
        """
        search_box = self.driver.find_elements(*Home.SEARCH_BAR)
        present = False
        if len(search_box) >= 1:
            present = True
        return present

    def homePage(self, param):
        """
         method to pass the element to search
         and enter
        """
        self.driver.find_element(*Home.SEARCH_BAR).send_keys(param['search_item'])
        self.driver.find_element(*Home.SEARCH_BAR).send_keys(Keys.ENTER)

    def get_result(self):
        """
         method to get all list of item after searching done
        """
        all_result = self.driver.find_elements(*Home.result)
        return all_result

    def click_item(self):
        """
         method to click on the 4th item of this item's list
        """
        return self.driver.find_element(*Home.item4).click()

    def scroll(self):
        """
         method to perform scroll down
        """
        self.driver.execute_script("window.scrollTo(0,700);")
