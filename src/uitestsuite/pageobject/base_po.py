from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import allure
import pytest
import time
import logging
from src.uitestsuite.driversetup.create_driver import InitDriver


# Setup logging
import pytest
import allure
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup logging
logging.basicConfig(
    filename="test_log.txt",
    level=logging.DEBUG,  # Change to DEBUG to capture all logs
    format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()


class BasePage:
    def __init__(self, driver=None):
        if driver is None:
            self.driver = InitDriver.init_driver().get_web_driver()
        else:
            self.driver = driver

    def open(self, url):
        with allure.step(f"Open the URL: {url}"):
            self.driver.get(url)

    def find_element(self, locator):
        with allure.step(f"Find the element: {locator}"):
            return self.driver.find_element(*locator)

    def find_elements(self, locator):
        with allure.step(f"Find the elements: {locator}"):
            return self.driver.find_elements(*locator)

    def click(self,locator):
        with allure.step(f"Click the element: {locator}"):
            self.find_element(locator).click()

    def enabled(self,locator):
        with allure.step(f"Is the element enabled: {locator}"):
            return self.find_element(locator).is_displayed()

    def send_keys(self, locator, text):
        with allure.step(f"Send the text: {text} to the element: {locator}"):
            self.find_element(locator).send_keys(text)

    def get_text(self, locator):
        with allure.step(f"Get the text of the element: {locator}"):
            return self.find_element(locator).text

    def get_title(self):
        with allure.step("Get the title of the page"):
            return self.driver.title

    def get_current_url(self):
        with allure.step("Get the current URL of the page"):
            return self.driver.current_url
    
    def select_dropdown_by_visible_text(self, locator, text):
        with allure.step(f"Select the dropdown by visible text: {text}"):
            select = Select(self.find_element(locator))
            select.select_by_visible_text(text)

    def wait_for_element(self, locator, timeout=10):
        with allure.step(f"Wait for the element: {locator}"):
            WebDriverWait(self.driver, timeout).until(
               EC.visibility_of_element_located(locator)
        )
    def click_element(self, locator):
        with allure.step(f"click with java script: {locator}"):
            element = self.find_element(locator)
            actions = ActionChains(self.driver)
            actions.move_to_element(element)
            actions.click(element)
            actions.perform()

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        with allure.step(f"Wait for the element to be clickable: {locator}"):  
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
        )
            
    def wait_for_60sec(self,timeout=60):
        with allure.step(f"Wait for the 60 sec implicitly"):  
            WebDriverWait(self.driver, timeout)

    def wait_for_pageload(self):
        with allure.step("Wait for the page to load"):
            self.driver.implicitly_wait(15)

    def wait_for_title(self, title, timeout=10):
        with allure.step(f"Wait for the title: {title}"):
            WebDriverWait(self.driver, timeout).until(
               EC.title_is(title)
        )

    def wait_for_url(self, url, timeout=10):
        with allure.step(f"Wait for the URL: {url}"):
            WebDriverWait(self.driver, timeout).until(
              EC.url_to_be(url)
        )

    def wait_for_alert(self, timeout=10):
        with allure.step("Wait for the alert"):
            WebDriverWait(self.driver, timeout).until(
               EC.alert_is_present()
        )

    def accept_alert(self):
        with allure.step("Accept the alert"):
            WebDriverWait(self.driver, 3).until(
                EC.alert_is_present(),'Timed out waiting and confirmation popup to appear.'
                )
            self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        with allure.step("Dismiss the alert"):
            self.driver.switch_to.alert.dismiss()

    def get_alert_text(self):
        with allure.step("Get the alert text"):
            return self.driver.switch_to.alert.text

    def switch_to_frame(self, locator):
        with allure.step(f"Switch to the frame: {locator}"):
            self.driver.switch_to.frame(locator)
     
    def wait_for_15sec(self, timeout=15):
            time.sleep(timeout)

    def switch_to_default_content(self):
        with allure.step("Switch to the default content"):
            self.driver.switch_to.default_content()

    def get_current_window_handle(self):
        with allure.step("Get the current window handle"):
            return self.driver.current_window_handle

    def get_window_handles(self):
        with allure.step("Get the window handles"):
            return self.driver.window_handles

    def switch_to_window(self, handle):
        with allure.step(f"Switch to the window: {handle}"):
            self.driver.switch_to.window(handle)

    def close_window(self):
        with allure.step("Close the window"):
            self.driver.close()

    def quit(self):
        with allure.step("Quit the browser"):
            self.driver.quit()

    def take_screenshot(self, filename):
        with allure.step("Take the screenshot"):
            self.driver.save_screenshot(filename)

    def scroll_to_element(self, locator):
        with allure.step(f"Scroll to the element: {locator}"):
            element = self.find_element(locator)
            self.driver.execute_script("arguments[0].scrollIntoView()")
            
    def maximize_window(self):
        with allure.step("Maximize the window"):
            self.driver.maximize_window()

    def clear(self, locator):
        with allure.step(f"Clear the text in: {locator}"):
            self.find_element(locator).clear()

    def hard_assert(self, actual, expected, message="Hard assertion failed"):
        """Logs assertion failure and stops execution."""
        with allure.step(f"Hard assert: {actual} == {expected}"):
            if actual != expected:
                logger.error(f"{message}: Expected '{expected}', but got '{actual}'")  # Logs the failure
            assert actual == expected, f"{message}: Expected '{expected}', but got '{actual}'"

    def soft_assert(self, actual, expected, message="Soft assertion failed"):
        """Logs assertion failure but continues execution."""
        with allure.step(f"Soft assert: {actual} == {expected}"):
            if actual != expected:
                logger.warning(f"{message}: Expected '{expected}', but got '{actual}'")  # Logs the failure
                allure.attach(f"{message}: Expected '{expected}', but got '{actual}'", name="Soft Assertion", attachment_type=allure.attachment_type.TEXT)
         


   