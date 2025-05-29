from src.uitestsuite.driversetup.create_driver import InitDriver
from src.uitestsuite.pageobject.org_po import OrgPage
import time
import pytest
from src.uitestsuite.testcases.test_base import TestBase
import allure
class TestOrg():
    @pytest.mark.dependency(name="TestOrg::test_org", depends=["TestLogin::test_login"], scope="session")
    @allure.feature("Organization Feature")
    def test_org(self,request):
        """
        Test case to verify organization functionality
        
        Steps:
        1. Launch the browser
        2. Enter the URL
        3. Select the organization
        4. Verify the title of the page
        """
        org_page = OrgPage(InitDriver.init_driver().get_web_driver())
        org_page.wait_for_element_to_be_clickable(org_page.page_selection)
        org_page.select_page("200")
        org_page.wait_for_element_to_be_clickable(org_page.auotmation_org)
        org_page.select_org()
        print(org_page.get_title())