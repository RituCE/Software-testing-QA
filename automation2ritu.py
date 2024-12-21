# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Testblankform():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_blankform(self):
        self.driver.get("https://testpages.eviltester.com/styled/")
        self.driver.set_window_size(550, 693)
        self.driver.find_element(By.CSS_SELECTOR, ".thumblinkdesc:nth-child(1) img").click()
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(31)").click()
        time.sleep(3)
        #sleeping time is for stay window

# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class TestFormAutomation:
    def setup_method(self, method):

        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.vars = {}

    def teardown_method(self, method):

        self.driver.quit()

    def test_form_submission(self):

        self.driver.get("https://testpages.eviltester.com/styled/validation/input-validation.html")


        self.driver.find_element(By.ID, "firstname").send_keys("James")
        self.driver.find_element(By.ID, "surname").send_keys("Johnjemesjohn")

        age_field = self.driver.find_element(By.ID, "age")
        age_field.clear()
        age_field.send_keys("23")

        country_dropdown = Select(self.driver.find_element(By.ID, "country"))
        country_dropdown.select_by_visible_text("Belgium")
        self.driver.find_element(By.ID, "notes").send_keys("abc")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        # sleeping time stay window
        time.sleep(2)











