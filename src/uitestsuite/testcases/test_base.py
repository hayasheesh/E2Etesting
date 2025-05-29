import time
import allure
import pytest
from src.uitestsuite.driversetup.create_driver import InitDriver

class TestBase:
    @allure.title("Initializing the driver and opening the website")
    @allure.description(
        "This method initializes the browser as specified by the user, "
        "creates the session for executing all the tests, and then closes the driver.")
    @pytest.fixture(scope='session', autouse=True)
    def setup_method(self, request):
        driver_manager = InitDriver.init_driver()

        self.driver = driver_manager.set_driver("chrome-headless")
        print("TestBase setup")
        
        self.driver.get("https://qa.tektome.dev/users/sign_in")
        self.driver.maximize_window()
        time.sleep(5)
        yield
        self.driver.quit()
