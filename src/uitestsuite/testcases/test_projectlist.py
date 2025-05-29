
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from assertpy import soft_assertions, assert_that
from src.uitestsuite.driversetup.create_driver import InitDriver
from src.uitestsuite.pageobject.projectlist_po import ProjectListPage
from src.util.readCSV import read_test_data_from_csv
from src.uitestsuite.pageobject.base_po import logger
from src.util.timestamp import get_timestamp

class TestProjectList:
    """
    Test suite for verifying elements and actions on the Project List page.
    """

    @allure.feature("Create project")
    @allure.title("To Test + New Project button enabled")
    @pytest.mark.dependency(name="check_new_project_button")
    def test_check_new_project_button(self):
        """
        Test to verify that the '+ New Project' button is enabled on the Project List page.

        Steps:
        1. Initialize the web driver and navigate to the Project List page.
        2. Check if the '+ New Project' button is enabled.
        3. Take a screenshot of the current UI state.

        Assertions:
        This test passes if the button is interactable (enabled).

        Reports:
        A screenshot is saved for visual confirmation.

        Dependencies:
        This test is marked for dependency as 'check_new_project_button' using pytest.
        """
        # Initialize the driver
        project_list = ProjectListPage(InitDriver.init_driver().get_web_driver())

        # Perform UI actions
        project_list.check_new_project_button()
        project_list.take_screenshot()

    
    @allure.title("To test new project is created successfully")
    @pytest.mark.dependency(name="create_project", depends=["check_new_project_button"])
    @pytest.mark.parametrize("test_data", read_test_data_from_csv())
    def test_create_project(self, test_data):
        """
        Test to verify that a new project can be created successfully.
        
        Steps:
        1. Extract test data from the CSV file.
        2. Initialize the web driver and navigate to the Project List page.
        3. Click on the '+ New Project' button.
        4. Create a new project with a unique name.
        5. Submit the project creation form.
        6. Verify the success message displayed in the toast notification.
        7. Take a screenshot of the current UI state.
            
        Assertions:
        This test passes if the success message matches the expected message.
        
        Reports:
        A screenshot is saved for visual confirmation.
        
        Dependencies:
        This test is marked for dependency as 'create_project' using pytest.
        """
        # Extract test data
        project_name = test_data['project_name'] + get_timestamp()
        expected_message = test_data['expected_success_message'].strip()
        # Initialize the driver
        project_list = ProjectListPage(InitDriver.init_driver().get_web_driver())
        # perform UI actions
        project_list.new_project_button()
        project_list.create_project(project_name)
        project_list.submit_project()
        with allure.step("Verify soft assertion for toast message"):
            with soft_assertions():
                success_message = WebDriverWait(project_list.driver, 10).until(EC.visibility_of_element_located(project_list.create_sucess_message)).text
                assert_that(success_message, "Project creation failed").is_equal_to(expected_message)
                print("Toast message:",success_message)
        project_list.take_screenshot()

    @allure.title("To test Created project is listed")
    @pytest.mark.dependency(name="project_present", depends=["create_project"])
    def test_project_present(self):
        """
        Test to verify that the created project is listed on the Project List page.
        
        Steps:
        1. Verify that the created project is listed.
        2. Take a screenshot of the current UI state.
        
        Assertions:
        This test passes if the created project is listed on the page.
            
        Reports:
        A screenshot is saved for visual confirmation.
            
        Dependencies:
        This test is marked for dependency as 'project_present' using pytest.
        """     
        # Initialize the driver
        project_list = ProjectListPage(InitDriver.init_driver().get_web_driver())
        with allure.step("Verify the project is created"):
            with soft_assertions():
                created_folder_element = WebDriverWait(project_list.driver, 10).until(EC.visibility_of_element_located(project_list.created_folder))
                created_folder_name = created_folder_element.text.strip().split("\n")[0]
                assert_that(created_folder_name).is_not_empty()
                print(created_folder_name)
                print("Created project lisied.")
        project_list.take_screenshot()
        
    @allure.title("To test project is renamed successfully")
    @pytest.mark.dependency(name="rename_project", depends=["project_present"])
    @pytest.mark.parametrize("test_data", read_test_data_from_csv())
    def test_rename_project(self,test_data):
        """
        Test to verify that a project can be renamed successfully.
        
        Steps:
        1. Extract test data from the CSV file.
        2. Rename the project with a unique name.
        3. Update the project name.
        4. Verify the success message displayed in the toast notification.
        5. Take a screenshot of the current UI state.
        
        Assertions:
        This test passes if the success message matches the expected message.
        
        Reports:
        A screenshot is saved for visual confirmation.
        
        Dependencies:
        This test is marked for dependency as 'rename_project' using pytest.
        """
        # Extract test data
        rename_project_name = test_data['Rename_project'] + get_timestamp()
        expected_message = test_data['expected_updated_message'].strip()
        # Initialize the driver
        project_list = ProjectListPage(InitDriver.init_driver().get_web_driver())
        # perform UI actions
        project_list.rename_project(rename_project_name)
        project_list.update_project()
        with allure.step("Verify toast message for project rename"):
             with soft_assertions():
                updated_message = WebDriverWait(project_list.driver, 10).until(EC.visibility_of_element_located(project_list.updated_sucess_message)).text
                assert_that(updated_message, "Project rename failed").is_equal_to(expected_message)
                print("Toast message:",updated_message)
        project_list.take_screenshot()

    @allure.title("To test renamed project listed.")
    @pytest.mark.dependency(name="updated_project", depends=["rename_project"])       
    def test_updated_project(self):
        """
        Test to verify that the renamed project is listed on the Project List page.
        
        Steps:
        1. Verify that the renamed project is listed.
        2. Take a screenshot of the current UI state.
        
        Assertions:
        This test passes if the renamed project is listed on the page.
        
        Reports:
        A screenshot is saved for visual confirmation.

        Dependencies:
        This test is marked for dependency as 'updated_project' using pytest.
        """
        # Initialize the driver
        project_list = ProjectListPage(InitDriver.init_driver().get_web_driver())
        with allure.step("Verify the project is renamed"):
            with soft_assertions():
                updated_folder = WebDriverWait(project_list.driver, 10).until(EC.visibility_of_element_located(project_list.rename_folder))
                updated_folder_name = updated_folder.text.strip().split("\n")[0]
                assert_that(updated_folder_name).is_not_empty()
                print(updated_folder_name)
                print("Project renamed & Updated successfully")
        project_list.take_screenshot()
                              
    @allure.title("To test project is removed successfully")
    @pytest.mark.dependency(name="delete_project", depends=["updated_project"])
    def test_delete_project(self):
        """
        Test to verify that a project can be removed successfully.
        
        Steps:
        1. Remove the project.
        2. Verify the success message displayed in the toast notification.
        3. Take a screenshot of the current UI state.
        
        Assertions:
        This test passes if the success message matches the expected message.
        
        Reports:
        A screenshot is saved for visual confirmation.
        
        Dependencies:
        This test is marked for dependency as 'delete_project' using pytest.
        """
        # Initialize the driver
        project_list = ProjectListPage(InitDriver.init_driver().get_web_driver())
        # perform UI actions
        project_list.delete_project()
        with allure.step("Verify successful project removal"):
            with soft_assertions():
                removed_message = WebDriverWait(project_list.driver, 10).until(EC.visibility_of_element_located(project_list.removed_sucess_message)).text
                project_list.soft_assert(removed_message, "Project removed.", "Project removal failed")
                print("Project removed successfully")
        project_list.take_screenshot()

    @allure.title("To test new project is created successfully")
    @pytest.mark.dependency(name="create_newproject")
    @pytest.mark.parametrize("test_data", read_test_data_from_csv())
    def test_create_newproject(self, test_data):
        """
        Test to verify that a new project can be created successfully.
        
        Steps:
        1. Extract test data from the CSV file.
        2. Click on the '+ New Project' button.
        3. Create a new project with a unique name.
        4. Submit the project creation form.
        5. Verify the success message displayed in the toast notification.
        6. Take a screenshot of the current UI state.
            
        Assertions:
        This test passes if the success message matches the expected message.
        
        Reports:
        A screenshot is saved for visual confirmation.
        
        Dependencies:
        This test is marked for dependency as 'create_newproject' using pytest.
        """
        # Extract test data
        project_name = test_data['project_name'] + get_timestamp()
        expected_message = test_data['expected_success_message'].strip()
        # Initialize the driver
        project_list = ProjectListPage(InitDriver.init_driver().get_web_driver())
        # perform UI actions
        project_list.new_project_button()
        project_list.create_project(project_name)
        project_list.submit_project()
        with allure.step("Verify soft assertion for toast message"):
            success_message = WebDriverWait(project_list.driver, 10).until(EC.visibility_of_element_located(project_list.create_sucess_message)).text
            assert_that(success_message, "Project creation failed").is_equal_to(expected_message)
            print("Toast message:",success_message)
        project_list.take_screenshot()
