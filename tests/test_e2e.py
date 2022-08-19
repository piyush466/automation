import time


from selenium.webdriver.common.by import By
from utilities.BaseClass import Baseclass

# @pytest.mark.usefixtures("setup")
class Testone(Baseclass):
    def test_e2e(self):

        self.driver.find_element(By.LINK_TEXT, "Shop").click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, 500)")

        products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        time.sleep(2)

        self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        time.sleep(2)
        # driver.close()
