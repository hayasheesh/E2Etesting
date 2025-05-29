from selenium.webdriver.common.by import By
from src.uitestsuite.pageobject.base_po import BasePage
import allure
from src.uitestsuite.pageobject.org_po import OrgPage

class LoginPage(BasePage):
    username_text = (By.XPATH, "//input[@id='user_email']")
    password_text = (By.XPATH, "//input[@id='user_password']")
    login_button = (By.XPATH, "//input[@name='commit']")
    login_message = (By.XPATH, "//div[@class='pt-1']")
    
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Enter the user name: {user_name}")
    def enter_user_name(self, user_name):
        self.send_keys(self.username_text, user_name)

    @allure.step("Enter the password: {password}")
    def enter_password(self, password):
        self.send_keys(self.password_text, password)
    
    @allure.step("Click the login button")
    def click_login_button(self):
        self.click(self.login_button)

    @allure.step("Get the login message")
    def get_login_message(self):
        return self.find_element(self.login_message).text
    
    def login(self, username, password):
        self.enter_user_name(username)
        self.enter_password(password)
        self.click_login_button()
        return OrgPage()





