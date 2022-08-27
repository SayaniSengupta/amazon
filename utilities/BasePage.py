import inspect
import logging

import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup", "param")
class BasePage:
    def wait_presence(self, path):
        """
           This wait is WebDriverWait along with expected condition where
           this wait used to wait for whether all elements of given locator
           presence or not.If not then raise exception.The locator pass
           through from different page objects
        """
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(path))

    def wait_clickable(self, path):
        """

            This wait is WebDriverWait along with expected condition where
            this wait used to wait for whether element of given locator
            is clickable or not.If not then raise exception.The locator pass
            through from different page objects

        """
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable(path))

    def message_logging(self, message):
        """
         to create the log file
        """
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler("logfile.log")
        logger.addHandler(filehandler)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.setLevel(logging.INFO)
        logger.info(message)
