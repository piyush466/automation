import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\selenium browser driver\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
check  = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for c in check:
    if c.get_attribute("value") == "option3":
        c.click()
        assert c.is_selected()

        

