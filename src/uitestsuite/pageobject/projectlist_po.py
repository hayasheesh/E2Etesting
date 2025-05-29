from selenium.webdriver.common.by import By
from src.uitestsuite.pageobject.base_po import BasePage
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.uitestsuite.pageobject.projectattribute_po import ProjectAttributePage
from src.uitestsuite.pageobject.filelist_po import FileListPage


class ProjectListPage(BasePage):
    #test_Tc_001,002
    create_project_button = (By.XPATH, "//span[text()='New project']")
    project_name_text = (By.ID, "project_name")
    project_ok_button = (By.XPATH, "//input[@value='Create Project']")
    create_sucess_message = (By.XPATH, "//div[@class='pt-1']")
    created_folder= (By.XPATH, "//div[@class='nav-tabs border-b-tabs']")
    #test_Tc_003
    setting_button = (By.XPATH, "//div[1]/ul[1]/li[2]/a[1]")
    project_newname_text = (By.XPATH, "//input[@id='project_name']")
    update_project_button = (By.XPATH, "//input[@value='Update Project']")
    updated_sucess_message = (By.XPATH, "//div[@class='pt-1']")
    rename_folder= (By.XPATH, "//div[@class='nav-tabs border-b-tabs']")
    #test_Tc_004
    delete_project_button = (By.XPATH, "//a[normalize-space()='Delete']")
    removed_sucess_message = (By.XPATH, "//div[@class='pt-1']")
    all_projectlist= (By.XPATH, "//table[@class='w-full']")

    @allure.step("capture screenshot")
    def take_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(),name="screenshot",attachment_type=allure.attachment_type.PNG)

    #new project button
    def check_new_project_button(self):
        project_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.create_project_button))
        project_button=project_button.is_enabled()
        print("New Project button is enabled")

    # Create a project
    def new_project_button(self):
        project_button=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.create_project_button))
        project_button.click()
    def create_project(self, name):
        create_project = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.project_name_text))
        create_project.send_keys(name)
    def submit_project(self):
        submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.project_ok_button))
        submit_button.click()

    # Rename a project
    def rename_project(self, new_name):
        setting = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.setting_button))
        setting.click()
        rename_project_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.project_newname_text))
        rename_project_field.clear()
        rename_project_field.send_keys(new_name)
        
    def update_project(self):
        update_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.update_project_button))
        update_button.click()
    
    # Delete a project
    def delete_project(self):
        setting = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.setting_button))
        setting.click()
        delete_project=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.delete_project_button))
        delete_project.click()
        #Dismiss the alert
        alert_text = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        print(alert_text.text)
        alert_text.dismiss()
        print("Alert text: cancel", alert_text)
        delete_project=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.delete_project_button))
        delete_project.click()
        #Accept the alert
        alert_text = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        print(alert_text.text)
        alert_text.accept()
        print("Alert text: ok", alert_text)

        return FileListPage()