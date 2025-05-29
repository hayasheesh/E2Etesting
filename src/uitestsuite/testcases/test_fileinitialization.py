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

class TestFileInitialization():
    @allure.feature("File Initialization Feature")
    @allure.title("To Test File Initialization List")
    @pytest.mark.dependency(name="TestFileInitialization::test_file_init_list",depends=["TestFileUpload::test_file_upload_validate"], scope="session")
    def test_file_init_list(self):
        file_lnit = FileInitializationPage(InitDriver.init_driver().get_web_driver())
        time.sleep(5)
        file_lnit.click_on_settings()
        uploaded_files = file_lnit.get_list_of_file_init()
        print(f"Files in Initialization : {uploaded_files}")
    
    @pytest.mark.dependency(name="TestFileInitialization::test_file_init_filter_user",depends=["TestFileInitialization::test_file_init_list"], scope="session")
    @allure.title("To Test File Initialization List filter by user")
    def test_file_init_filter_user(self):
        file_lnit = FileInitializationPage(InitDriver.init_driver().get_web_driver())
        time.sleep(5)
        file_lnit.select_filter_by_user()   
        listed_files = file_lnit.get_list_of_file_init()
        print(f"Files in Initialization by user: {listed_files}")
    
    @allure.title("To Test File List filter by Status as file initialization started")
    @pytest.mark.dependency(name="TestFileInitialization::test_file_init_started",depends=["TestFileInitialization::test_file_init_filter_user"], scope="session")
    def test_file_init_started(self):
        file_lnit = FileInitializationPage(InitDriver.init_driver().get_web_driver())
        time.sleep(5)
        file_lnit.filter_by_file_init_started()   
        listed_files = file_lnit.get_list_of_file_init()
        #verification of files list is pending since its dynamic 
        print(f"Files in Initialization by user: {listed_files}")
        file_lnit.filter_by_file_init_started()   

    @allure.title("To Test File Initialization by queued status")
    @pytest.mark.dependency(name="TestFileInitialization::test_file_init_queued",depends=["TestFileInitialization::test_file_init_started"], scope="session")
    def test_file_init_queued(self):
        file_lnit = FileInitializationPage(InitDriver.init_driver().get_web_driver())
        time.sleep(5)
        file_lnit.filter_by_file_init_queued()
        uploaded_files = file_lnit.get_list_of_file_init()
        print(f"Files in Initialization : {uploaded_files}")
         #verification of files list is pending since its dynamic 
        file_lnit.filter_by_file_init_queued()

   
    @allure.title("To Test File Initialization by Failed status")
    @pytest.mark.dependency(name="TestFileInitialization::test_file_init_failed",depends=["TestFileInitialization::test_file_init_queued"], scope="session")
    def test_file_init_failed(self):
        file_lnit = FileInitializationPage(InitDriver.init_driver().get_web_driver())
        time.sleep(5)
        file_lnit.filter_by_file_init_failed()
        uploaded_files = file_lnit.get_list_of_file_init()
        print(f"Files in Initialization : {uploaded_files}")
        #verification of files list is pending since its dynamic
        file_lnit.filter_by_file_init_failed()
 
    
    @allure.title("To Test File Initialization by Completed status")
    @pytest.mark.dependency(name="TestFileInitialization::test_file_init_completed",depends=["TestFileInitialization::test_file_init_failed"], scope="session")
    def test_file_init_completed(self):
        file_lnit = FileInitializationPage(InitDriver.init_driver().get_web_driver())
        time.sleep(5)
        file_lnit.filter_by_file_init_completed()
        uploaded_files = file_lnit.get_list_of_file_init()
        print(f"Files in Initialization : {uploaded_files}")
        
        #verification of files list is pending since its dynamic
        time.sleep(5)
        file_lnit.filter_by_file_init_completed()
 

    @allure.title("To Test File Initialization retry for Failed filed")
    @pytest.mark.dependency(name="TestFileInitialization::test_file_init_retry",depends=["TestFileInitialization::test_file_init_completed"], scope="session")
    def test_file_init_retry(self):
        file_lnit = FileInitializationPage(InitDriver.init_driver().get_web_driver())
        time.sleep(5)
        file_lnit.filter_by_file_init_failed()
        file_lnit.retry_failed_files()
        uploaded_files = file_lnit.get_list_of_file_init()
        new_name = "tif.tif"
        print(f"Files in Initialization : {uploaded_files}")
        with soft_assertions():
             assert_that(file_lnit.verify_file_retry(), f"{new_name} File name was not deleted ").is_true()
    
    @allure.title("To Test download for Failed files")
    @pytest.mark.dependency(name="TestFileInitialization::test_file_init_download",depends=["TestFileInitialization::test_file_init_retry"], scope="session")
    def test_file_init_download(self):
        file_lnit = FileInitializationPage(InitDriver.init_driver().get_web_driver())
        file_ops = get_file_operations_by_os()
        downloads_dir = file_ops.get_download_dir()
        files = os.listdir(downloads_dir)
        #file_lnit.refresh_webpage()
        keyword = "tif"
        Targetfilecount1 = sum(1 for file in files if keyword in file)
        time.sleep(5)
        file_lnit.download_failed_files()
        time.sleep(5)
        files = os.listdir(downloads_dir)
        Targetfilecount2 = sum(1 for file in files if keyword in file)
        with soft_assertions():
            assert_that(Targetfilecount1 + 1).is_equal_to(Targetfilecount2)
    
    @allure.title("To Test delete for failed files")
    @pytest.mark.dependency(name="TestFileInitialization::test_file_init_delete",depends=["TestFileInitialization::test_file_init_download"], scope="session")
    def test_file_init_delete(self):
        file_lnit = FileInitializationPage(InitDriver.init_driver().get_web_driver())
        time.sleep(5)
        file_lnit.delete_failed_files()
        time.sleep(5)
        file_lnit.accept_deleting_alert()
        new_name = "tif.tif"
        first_uploaded_files = file_lnit.get_first_uploaded_files()
        print(f"First Uploaded files: {first_uploaded_files}")
        with soft_assertions():
             assert_that(file_lnit.verify_file_deleted(), f"{new_name} File name was not deleted ").is_true()

    @allure.title("To Test Preview for Completed files")
    @pytest.mark.dependency(name="TestFileInitialization::test_file_init_preview",depends=["TestFileInitialization::test_file_init_delete"], scope="session")
    def test_file_init_preview(self):
        file_lnit = FileInitializationPage(InitDriver.init_driver().get_web_driver())
        time.sleep(5)
        file_lnit.preview_files_in_file_init()
        with soft_assertions():
            assert_that(file_lnit.verify_preview(), "preview is not displayed").is_true()
        file_lnit.wait_for_element_to_be_clickable(file_lnit.exit_preview_button)
        file_lnit.click_exit_preview_button()
                