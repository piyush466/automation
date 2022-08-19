import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\selenium browser driver\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

def q():
    time.sleep(2)
name =  driver.find_element(By.CSS_SELECTOR, "#name")
name.send_keys("piy")
q()
confirm = driver.find_element(By.CSS_SELECTOR, "#confirmbtn")
confirm.click()
q()
aler =driver.switch_to.alert
alertt = aler.text
print(aler.text)
aler.dismiss()

assert alertt in "Hello piy, Are you sure you want to confirm?"
driver.close()



