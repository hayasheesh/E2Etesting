from src.uitestsuite.driversetup.create_driver import InitDriver
from src.uitestsuite.pageobject.login_po import LoginPage
from src.uitestsuite.testcases.test_base import TestBase
import time
import pytest
import allure


class TestLogin(TestBase):
    @pytest.mark.usefixtures("setup_method")
    @pytest.mark.dependency(name="TestLogin::test_login", scope="session")
    @allure.feature("Login Feature")
    def test_login(self):
        """
        Test case to verify login functionality
        
        Steps:
        1. Launch the browser
        2. Enter the URL
        3. Enter the username
        4. Enter the password
        5. Click on the login button
        6. Verify the title of the page
        """
        print("TestLogin")
        login_page = LoginPage(InitDriver.init_driver().get_web_driver())
        org_page = login_page.login("", "")
        print(org_page.get_title())  
