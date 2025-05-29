from selenium.webdriver.common.by import By
from src.uitestsuite.pageobject.base_po import BasePage
from src.uitestsuite.pageobject.dataspace_po import DataspacePage
import allure

class OrgPage(BasePage):
    page_selection = (By.XPATH, "(//select)[1]")
    auotmation_org = (By.XPATH, "//*[text()='tektome-test-automation']")

    @allure.step("Select the page")
    def select_page(self, page_no):
        self.select_dropdown_by_visible_text(self.page_selection, page_no)

    @allure.step("Select the organization")
    def select_org(self):
        self.click(self.auotmation_org)
        return DataspacePage()
    
