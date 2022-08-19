import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\selenium browser driver\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
def t():
    print("piyushhhh")
    time.sleep(2)


driver.find_element(By.CSS_SELECTOR, "#name").send_keys("piyush")
t()
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
t()
alert =  driver.switch_to.alert
alert.accept()









