import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\selenium browser driver\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/seleniumPractice/")
driver.maximize_window()


