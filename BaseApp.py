from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    """Base Object"""

    def __init__(self, driver):
        self.driver = driver
        print(self.driver)
        self.url = "https://mail.google.com"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator), message=f"No element: {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f"No elements: {locator}")

    def go_to_site(self):
        return self.driver.get(self.url)
