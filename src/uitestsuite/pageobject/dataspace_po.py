from selenium.webdriver.common.by import By
from src.uitestsuite.pageobject.base_po import BasePage
from src.uitestsuite.pageobject.projectlist_po import ProjectListPage
import allure
class DataspacePage(BasePage):
    dataspace_select = (By.XPATH, "//*[text()='smoke-test']")
    @allure.title("Select the dataspace")
    def select_dataspace(self):
        self.click(self.dataspace_select)
        return ProjectListPage()
