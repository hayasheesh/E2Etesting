import keyword
import os
import time
import pytest
import datetime
import allure
from src.uitestsuite.pageobject.fileinitialization_po import FileInitializationPage
from src.uitestsuite.driversetup.create_driver import InitDriver
from assertpy import assert_that, soft_assertions
from src.util.common import getTimestamp
from src.util.file_operations import get_file_operations_by_os

class TestProjectAttrExtraction():
    @allure.feature("Project Attribute Feature")
    @allure.title("To Test Project Attribute Extraction List")
    @pytest.mark.dependency(name="TestProjectAttrExtraction::test_project_attr_ext_list",depends=["TestFileUpload::test_file_upload_validate"], scope="session")
    def test_attr_ext_list(self):
        proj_att = TestProjectAttrExtraction(InitDriver.init_driver().get_web_driver())
        proj_att.click_on_settings()
        uploaded_files = file_lnit.get_list_of_file_init()
        print(f"Prject attribute list page : {uploaded_files}")
    
    