import os
import time
import pytest
from assertpy import assert_that, soft_assertions
from src.uitestsuite.driversetup.create_driver import InitDriver
from src.uitestsuite.pageobject.filelist_po import FileListPage
from selenium.webdriver.common.by import By
from src.util.file_operations import get_file_operations_by_os
from selenium.webdriver.support.ui import WebDriverWait
import allure
from selenium.webdriver.support import expected_conditions as EC
from src.util.common import getTimestamp
random1=getTimestamp()
common_waittime = 5

class TestFileUpload():
    @allure.feature("Filelist Feature")   
    @allure.title("Test uploading invalid files and verifying no unexpected changes.")
    @pytest.mark.dependency(name="TestFileUpload::test_failed_file_upload", depends=["TestProjectList::create_new_project"], scope="session")
    def test_failed_file_upload(self):
        filelist_page = FileListPage(InitDriver.init_driver().get_web_driver())
        #failure_folder = filelist_page.add_filepath_to_upload("..", "inputs", "upload_testdata", "uploadfile_fail")
        failure_folder = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "..", "inputs", "upload_testdata", "uploadfile_fail"
            )
        )
        files_to_upload = [os.path.join(failure_folder, f) for f in os.listdir(failure_folder)]
        initial_uploaded_files = filelist_page.get_uploaded_files_in_failure()
        filelist_page.wait_for_element_to_be_clickable(filelist_page.upload_button )
        filelist_page.click_upload_button()
        filelist_page.wait_for_60sec()
        filelist_page.upload_multiple_files(files_to_upload)
        filelist_page.wait_for_60sec()
        filelist_page.wait_for_element_to_be_clickable(filelist_page.close_button )
        filelist_page.click_close_button()
        final_uploaded_files = filelist_page.get_uploaded_files_in_failure()
        with soft_assertions():
             assert_that(final_uploaded_files, "Uploaded file list changed after failed uploads.").is_equal_to(initial_uploaded_files)

    @allure.title("Test uploading Jpg valid files and verifying the uploaded files.")
    @pytest.mark.dependency(name="TestFileUpload::test_file_upload_validate_jpg", depends=["TestFileUpload::test_failed_file_upload"], scope="session")
    def test_file_upload_validate_jpg(self):
        filelist_page = FileListPage(InitDriver.init_driver().get_web_driver())
        success_folder = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "..", "inputs", "upload_testdata", "uploadfile_image"
            )
        )
        files_to_upload = [os.path.join(success_folder, f) for f in os.listdir(success_folder)]
        expected_uploaded_files = ["jpg.jpg"]
        filelist_page.click_upload_button()
        filelist_page.wait_for_60sec()
        filelist_page.upload_multiple_files(files_to_upload)
        filelist_page.wait_for_60sec()
        uploaded_files = filelist_page.get_uploaded_files()
        print(f"Image Uploaded files: {uploaded_files}")
        # can change to soft assertion if more success files to upload but at least 3 files are needed
        with soft_assertions():
             assert_that(set(uploaded_files), "Uploaded files do not match expected").is_equal_to(set(expected_uploaded_files))
        
    @allure.title("Test uploading PDF valid files and verifying the uploaded files.")
    @pytest.mark.dependency(name="TestFileUpload::test_file_upload_validate_pdf", depends=["TestFileUpload::test_file_upload_validate_jpg"], scope="session")
    def test_file_upload_validate_pdf(self):
        filelist_page = FileListPage(InitDriver.init_driver().get_web_driver())
        success_folder = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "..", "inputs", "upload_testdata", "uploadfile_pdf"
            )
        )
        files_to_upload = [os.path.join(success_folder, f) for f in os.listdir(success_folder)]
        expected_uploaded_files = ["jpg.jpg","pdf.pdf"]
        filelist_page.click_upload_button()
        filelist_page.wait_for_15sec()
        filelist_page.upload_multiple_files(files_to_upload)
        filelist_page.wait_for_15sec()
        uploaded_files = filelist_page.get_uploaded_files()
        print(f" PDF Uploaded files: {uploaded_files}")
        # can change to soft assertion if more success files to upload but at least 3 files are needed
        with soft_assertions():
             assert_that(set(uploaded_files), "Uploaded files do not match expected").is_equal_to(set(expected_uploaded_files))
        
    @allure.title("Test uploading XLXS valid files and verifying the uploaded files.")
    @pytest.mark.dependency(name="TestFileUpload::test_file_upload_validate_xlxs", depends=["TestFileUpload::test_file_upload_validate_pdf"], scope="session")
    def test_file_upload_validate_xlxs(self):
        filelist_page = FileListPage(InitDriver.init_driver().get_web_driver())
        success_folder = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..", "inputs", "upload_testdata", "uploadfile_xls"
        )
        )
        files_to_upload = [os.path.join(success_folder, f) for f in os.listdir(success_folder)]
        expected_uploaded_files = ["jpg.jpg","pdf.pdf","xlsx.xlsx"]
        filelist_page.click_upload_button()
        filelist_page.wait_for_15sec()
        filelist_page.upload_multiple_files(files_to_upload)
        filelist_page.wait_for_15sec()
        uploaded_files = filelist_page.get_uploaded_files()
        print(f"XLXS Uploaded files: {uploaded_files}")
        # can change to soft assertion if more success files to upload but at least 3 files are needed
        with soft_assertions():
             assert_that(set(uploaded_files), "Uploaded files do not match expected").is_equal_to(set(expected_uploaded_files)) 

    @allure.title("Test file list view and preview the uploaded files.")
    @pytest.mark.dependency(name="TestFileUpload::test_filelist_view", depends=["TestFileUpload::test_file_upload_validate_xlxs"], scope="session")
    def test_filelist_view(self):
            filelist_page = FileListPage(InitDriver.init_driver().get_web_driver())
            filelist_page.click_grid_view_button()
            with soft_assertions():
                assert_that(filelist_page.verify_grid_view_3_file(), "Grid view is not displayed").is_true()
            filelist_page.click_on_home_button()
            filelist_page.click_preview_button()
            filelist_page.wait_for_pageload()
            with soft_assertions():
                assert_that(filelist_page.verify_preview(), "preview is not displayed").is_true()
            filelist_page.click_exit_preview_button()
            filelist_page.wait_for_pageload()

            
    @allure.title("Test renaming the uploaded files.")
    @pytest.mark.dependency(name="TestFileUpload::test_rename_file", depends=["TestFileUpload::test_filelist_view"], scope="session")
    def test_rename_file(self):
        filelist_page = FileListPage(InitDriver.init_driver().get_web_driver())
        filelist_page.click_on_home_button()
        filelist_page.wait_for_pageload()
        filelist_page.click_file_settings_button_filelist_page()
        filelist_page.click_rename_button()
        filelist_page.wait_for_element(filelist_page.file_name_input)
        new_name = "jpg1.jpg"
        filelist_page.rename_file(new_name) 
        print(filelist_page.verify_success_msg("File updated."))
        with soft_assertions():
            assert_that(filelist_page.verify_success_msg("File updated."), f"Success message is not found{filelist_page.verify_success_msg("File updated.")}").is_true()
            filelist_page.click_on_home_button()
            assert_that(filelist_page.verify_file_name_updated(), f"File name was not updated to {new_name}").is_true()              


    @allure.title("Test downloading the uploaded files.")
    @pytest.mark.dependency(name="TestFileUpload::test_download_file",depends=["TestFileList::test_rename_file"], scope="session")
    def test_download_file(self):
        filelist_page = FileListPage(InitDriver.init_driver().get_web_driver())
        file_ops = get_file_operations_by_os()
        downloads_dir = file_ops.get_download_dir()
        files = os.listdir(downloads_dir)
        keyword = "jpg1"
        Targetfilecount1 = sum(1 for file in files if keyword in file)
        filelist_page.click_file_settings_button_filelist_page()
        filelist_page.wait_for_element_to_be_clickable(filelist_page.download_button )
        filelist_page.click_download_button()
        filelist_page.wait_for_pageload()
        files = os.listdir(downloads_dir)
        Targetfilecount2 = sum(1 for file in files if keyword in file)
        with soft_assertions():
             assert_that(Targetfilecount1 + 1).is_equal_to(Targetfilecount2)

    @allure.title("Test deleting the uploaded files.")
    @pytest.mark.dependency(name="TestFileUpload::test_delete_file", depends=["TestFileUpload::test_download_file"], scope="session")
    def test_delete_file(self):
        filelist_page = FileListPage(InitDriver.init_driver().get_web_driver())
        filelist_page.click_file_settings_button_filelist_page()
        filelist_page.wait_for_element_to_be_clickable(filelist_page.delete_button)
        new_name = "jpg1.jpg"
        filelist_page.click_deleting_button()
        filelist_page.accept_deleting_alert() 
        first_uploaded_files = filelist_page.get_first_uploaded_files()
        print(f"First Uploaded files: {first_uploaded_files} {filelist_page.verify_success_msg("File deleted.")}")
        with soft_assertions():
             assert_that(filelist_page.verify_success_msg("File deleted."), f"Success message is not found").is_true()
        with soft_assertions():
             assert_that(filelist_page.verify_file_deleted(), f"{new_name} File name was not deleted ").is_true()
    
    @allure.title("Test moving the uploaded files.")
    @pytest.mark.dependency(name="TestFileUpload::test_move_file",depends=["TestFileUpload::test_delete_file"], scope="session")
    def test_move_file(self):
        filelist_page = FileListPage(InitDriver.init_driver().get_web_driver())
        filelist_page.create_folder("Automation_folder")
        filelist_page.wait_for_pageload()
        filelist_page.click_file_settings_button_move_filelist_page()
        filelist_page.click_move_button()
        filelist_page.wait_for_element(filelist_page.folder_select_dropdown )
        filelist_page.click_folder_select_dropdown_2()
        filelist_page.wait_for_element_to_be_clickable(filelist_page.confirm_move_button)
        filelist_page.confirm_move()
        filelist_page.wait_for_pageload()
        filelist_page.wait_for_element(filelist_page.move_target_folder_confirm_1)
        with soft_assertions():
             assert_that(filelist_page.check_move_success_in_filelist(), "File move was not successful").is_true()

    @allure.title("Test uploading multiple files and verifying the uploaded files.")
    @pytest.mark.dependency(name="TestFileUpload::test_file_upload_validate", depends=["TestFileUpload::test_move_file"], scope="session")
    def test_file_upload_validate(self):
            filelist_page = FileListPage(InitDriver.init_driver().get_web_driver()) 
            folder_names = [
                "QA_Folder", "QA_Folder1", "QA_Folder2", "QA_Folder3", "QA_Folder4", "QA_Folder_move"
            ]

            for folder_name in folder_names:
                filelist_page.create_folder(folder_name)
                filelist_page.wait_for_element((By.XPATH, f"//div[contains(@class, 'flex') and normalize-space(text())='{folder_name}']") )
            filelist_page.wait_for_element((By.XPATH, f"//div[contains(@class, 'flex') and normalize-space(text())='QA_Folder_move']") )
            created_folders = filelist_page.get_all_folders()
            with soft_assertions():
                for folder_name in folder_names:
                    assert_that(created_folders, f"Folder '{folder_name}' was not created.").contains(folder_name)

            folder_to_test = "QA_Folder"
            filelist_page.navigate_to_folder(folder_to_test)
            filelist_page.wait_for_element(filelist_page.qa_folder )
            with soft_assertions():
                 assert_that(filelist_page.confirm_navigate_folder(), f"Failed to navigate to folder {folder_to_test}").is_true()
            success_folder = os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__),
                    "..", "inputs", "upload_testdata", "uploadfile_success"
                )
            )
            files_to_upload = [os.path.join(success_folder, f) for f in os.listdir(success_folder)]
            expected_uploaded_files = ["jpg.jpg", "tif.tif", "xlsx.xlsx", "pdf.pdf"]
            filelist_page.click_upload_button()
            time.sleep(20)
            filelist_page.upload_multiple_files_withfailure(files_to_upload)
            time.sleep(20)
            uploaded_files = filelist_page.get_uploaded_files()
            print(f"Uploaded files: {uploaded_files}")
            # can change to soft assertion if more success files to upload but at least 3 files are needed
            with soft_assertions():
                 assert_that(set(uploaded_files), "Uploaded files do not match expected").is_equal_to(set(expected_uploaded_files))
            failure_folder = os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__),
                    "..", "inputs", "upload_testdata", "uploadfile_fail"
                )
            )
            files_to_upload = [os.path.join(failure_folder, f) for f in os.listdir(failure_folder)]
            initial_uploaded_files = filelist_page.get_uploaded_files()
            filelist_page.wait_for_element_to_be_clickable(filelist_page.upload_button )
            filelist_page.click_upload_button()
            filelist_page.upload_multiple_files(files_to_upload)
            filelist_page.wait_for_element_to_be_clickable(filelist_page.close_button )
            filelist_page.click_close_button()
            final_uploaded_files = filelist_page.get_uploaded_files()
            with soft_assertions():
                 assert_that(final_uploaded_files, "Uploaded file list changed after failed uploads.").is_equal_to(initial_uploaded_files)
    