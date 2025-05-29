from src.uitestsuite.driversetup.create_driver import InitDriver
from src.uitestsuite.pageobject.dataspace_po import DataspacePage
from src.uitestsuite.pageobject.org_po import OrgPage
import time
import pytest
import allure

class TestDataspace():
    @pytest.mark.dependency(name="TestDataspace::test_opendata",depends=["TestOrg::test_org"], scope="session")
    @allure.feature("Dataspace Feature")
    def test_opendata(self): 
        """
        Test case to verify dataspace functionality
        
        Steps:
        1. Launch the browser
        2. Enter the URL
        3. Click on the dataspace
        4. Verify the title of the page
        """
        data_page = DataspacePage(InitDriver.init_driver().get_web_driver())
        data_page.wait_for_element_to_be_clickable(data_page.dataspace_select )
        data_page.select_dataspace()
        print(data_page.get_title())