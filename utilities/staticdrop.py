import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\selenium browser driver\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(10)
drop = Select(driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1"))
drop.select_by_visible_text("Female")
time.sleep(1)
drop.select_by_index(0)
time.sleep(2)


