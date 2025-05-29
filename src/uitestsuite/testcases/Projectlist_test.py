
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import time
from src.uitestsuite.driversetup.create_driver import InitDriver
from src.uitestsuite.pageobject.projectlist_po import ProjectListPage
from src.util.readCSV import read_test_data_from_csv
from datetime import datetime
from src.uitestsuite.pageobject.base_po import logger
from src.util.timestamp import get_timestamp

class TestProjectList:
    @allure.title("To Test + New Project button enabled on right side of page")
    @pytest.mark.dependency(name="test_TC_001")
    def test_TC_001(self):
        project_list = ProjectListPage(InitDriver.init_driver().get_web_driver())
        with allure.step("Verify the New Project button is enabled"):
            project_button = WebDriverWait(project_list.driver, 10).until(EC.element_to_be_clickable(project_list.create_project_button))
            project_list.hard_assert(project_button.is_enabled(), True, "New Project button should be enabled")
            logger.info("New Project button is enabled")

    @allure.title("To test new project is created successfully")
    @pytest.mark.dependency(name="test_TC_002", depends=["test_TC_001"])
    @pytest.mark.parametrize("test_data", read_test_data_from_csv())
    def test_TC_002(self, test_data):
        project_name = test_data['project_name'] + get_timestamp()
        print("Project name:", project_name)
        expected_message = test_data['expected_success_message'].strip()
        project_list = ProjectListPage(InitDriver.init_driver().get_web_driver())
        project_button = WebDriverWait(project_list.driver, 10).until(EC.element_to_be_clickable(project_list.create_project_button))
        project_button.click()
        create_project = WebDriverWait(project_list.driver, 10).until(EC.element_to_be_clickable(project_list.project_name_text))
        create_project.send_keys(project_name)
        submit_button = WebDriverWait(project_list.driver, 10).until(EC.element_to_be_clickable(project_list.project_ok_button))
        submit_button.click()

        with allure.step("Verify successful project creation"):
            success_message = WebDriverWait(project_list.driver, 10).until(EC.visibility_of_element_located(project_list.create_sucess_message)).text
            project_list.soft_assert(success_message, expected_message, "Project creation failed")
            print("Project Created successfully")
        with allure.step("Verify the project is created"):
            created_folder_element = WebDriverWait(project_list.driver, 10).until(EC.visibility_of_element_located(project_list.created_folder))
            created_folder_name = created_folder_element.text.strip().split("\n")[0]
            project_list.soft_assert(created_folder_name, project_name.strip(), "Project not created")
            print("Project created successfully")
        with allure.step("Capture Screenshot"):
            allure.attach(project_list.driver.get_screenshot_as_png(), name="Project_Creation", attachment_type=allure.attachment_type.PNG)

    @allure.title("To test project is renamed successfully")
    @pytest.mark.dependency(name="test_TC_003", depends=["test_TC_002"])
    @pytest.mark.parametrize("test_data", read_test_data_from_csv())
    def test_TC_003(self, test_data):
        project_list = ProjectListPage(InitDriver.init_driver().get_web_driver())
        setting = WebDriverWait(project_list.driver, 10).until(EC.element_to_be_clickable(project_list.setting_button))
        setting.click()
        rename_project_field = WebDriverWait(project_list.driver, 10).until(EC.element_to_be_clickable(project_list.project_newname_text))
        rename_project_field.clear()
        rename_project_name = test_data['Rename_project'] + get_timestamp()
        print("Rename project name:", rename_project_name)
        rename_project = WebDriverWait(project_list.driver, 10).until(EC.element_to_be_clickable(project_list.project_newname_text))
        rename_project.send_keys(rename_project_name)
        update_button = WebDriverWait(project_list.driver, 10).until(EC.element_to_be_clickable(project_list.update_project_button))
        update_button.click()

        with allure.step("Verify successful project rename"):
            updated_message = WebDriverWait(project_list.driver, 10).until(EC.visibility_of_element_located(project_list.updated_sucess_message)).text
            project_list.soft_assert(updated_message, "Project updated.", "Project rename failed")
            print("Project updated successfully")
        with allure.step("Verify the project is renamed"):
            updated_folder = WebDriverWait(project_list.driver, 10).until(EC.visibility_of_element_located(project_list.rename_folder))
            updated_folder_name = updated_folder.text.strip().split("\n")[0]
            project_list.soft_assert(updated_folder_name, rename_project_name.strip(), "Project not renamed")
            print("Project renamed successfully")
        with allure.step("Capture Screenshot"):   
            allure.attach(project_list.driver.get_screenshot_as_png(), name="Project_Rename", attachment_type=allure.attachment_type.PNG)
 
    # @allure.title("To test project is removed successfully")
    # @pytest.mark.dependency(name="test_TC_004", depends=["test_TC_003"])
    # def test_TC_004(self):
    #     project_list = ProjectListPage(InitDriver.init_driver().get_web_driver())
    #     setting = WebDriverWait(project_list.driver, 10).until(EC.element_to_be_clickable(project_list.setting_button))
    #     setting.click()
    #     delete_project = WebDriverWait(project_list.driver, 10).until(EC.element_to_be_clickable(project_list.delete_project_button))
    #     delete_project.click()
    #     # Dismiss the alert
    #     alert_text = WebDriverWait(project_list.driver, 10).until(EC.alert_is_present())
    #     print(project_list.get_alert_text())
    #     project_list.dismiss_alert()
    #     print("Alert text: cancel", alert_text)
    #     delete_project = WebDriverWait(project_list.driver, 10).until(EC.element_to_be_clickable(project_list.delete_project_button))
    #     delete_project.click()
    #     # Accept the alert
    #     alert_text = WebDriverWait(project_list.driver, 10).until(EC.alert_is_present())
    #     print(project_list.get_alert_text())
    #     project_list.accept_alert()
    #     print("Alert text: ok", alert_text)
    #     with allure.step("Successfully removed project"):
    #         removed_message = WebDriverWait(project_list.driver, 10).until(EC.visibility_of_element_located(project_list.removed_sucess_message)).text
    #         project_list.soft_assert(removed_message, "Project removed.", "Project removal failed")
    #         print("Project removed successfully")
    #     with allure.step("Capture Screenshot"):
    #         allure.attach(project_list.driver.get_screenshot_as_png(), name="Project_Removal", attachment_type=allure.attachment_type.PNG)
