import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\selenium browser driver\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/client/")
time.sleep(2)

driver.find_element(By.LINK_TEXT, "Forgot password?").click()
time.sleep(1)
# usernamr by XpATH
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("piyush@gmail.com")
time.sleep(1)
#password by CSS selector
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("pi@123")
time.sleep(1)
# confirm password is only use when id #confirmPassword

driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("pi@123")
time.sleep(1)

driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()

time.sleep(1)

