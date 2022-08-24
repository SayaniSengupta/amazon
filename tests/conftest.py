import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from config.con import TestData


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption("--email", action="store", help="abcd@test.com")
    parser.addoption("--password", action="store", help="12345678")
    parser.addoption("--search_item", action="store", help="mobile")
global driver

@pytest.fixture(scope="class")
def setup(request):
    driver = None
    browser_name = request.config.getoption("browser_name")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-error')
    if browser_name == "chrome":
        service_obj = Service(TestData.chrome_executablepath)
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)

    driver.get(TestData.baseUrl)
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()
@pytest.fixture
def param(request):
    param = {'email': request.config.getoption('--email'),
              'password': request.config.getoption('--password'),
              'search_item': request.config.getoption('--search_item')}

    if param['email'] is None and param['password'] is None:
        pytest.skip()
    request.cls.param = param
    return







