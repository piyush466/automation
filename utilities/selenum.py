import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\selenium browser driver\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/angularpractice/")
time.sleep(2)
print(driver.title)

driver.find_element(By.NAME, "name").send_keys("piyush dravyakar")
time.sleep(1)

driver.find_element(By.NAME, "email").send_keys("piyush@gmail.com")
time.sleep(1)

driver.find_element(By.ID, "exampleInputPassword1").send_keys("piyush@123")
time.sleep(1)

driver.find_element(By.ID,"exampleCheck1").click()
time.sleep(1)
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(1)
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("pp")

time.sleep(3)
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

mas = driver.find_element(By.CLASS_NAME, "alert-dismissible").text
print(mas)
time.sleep(1)

assert "Success! The Form has been submitted successfully!." in mas
# driver.quit()
