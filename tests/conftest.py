
import time

import pytest

from selenium import webdriver

# from tests.test_e2e import Testone
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path='C:\Tool\chromedriver_win32 (1)\chromedriver.exe')
    elif browser_name =="firefox":
        driver = webdriver.Firefox(executable_path='C:\Automation\geckodriver-v0.31.0-win64 (1)\geckodriver.exe')

    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(122)
    time.sleep(2)
    request.cls.driver = driver
    yield
    driver.close()








