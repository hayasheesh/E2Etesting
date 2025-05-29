from assertpy import assert_that, soft_assertions
from src.uitestsuite.driversetup.create_driver import InitDriver
import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.uitestsuite.pageobject.fileattribute_po import FileAttributePage
from src.util.readCSV import read_test_data_from_csv
from src.util.timestamp import get_timestamp

class TestProjectAttribute:
    @allure.feature("Project Attribute")
    @allure.title("To test Project Attribute is clickable")
    @pytest.mark.dependency(name="Click_on_setting_button")
    def test_Click_on_setting_button(self):
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        file_attribute.select_setting()
        file_attribute.select_project_attribute_setting()     
        file_attribute.take_screenshot()

    @allure.title("Delete the exsiting attribute")
    @pytest.mark.dependency(name="Delete_existing_attribute", depends=["Click_on_setting_button"])
    def test_Delete_existing_attribute(self):
        project_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        project_attribute.exsiting_attribute_delete()
        project_attribute.take_screenshot()
        print("Existing attribute is deleted")

    @allure.title("To test the New attribute functionality")
    @pytest.mark.dependency(name="Click_New_attribute_button", depends=["Delete_existing_attribute"])
    def test_Click_New_attribute_button(self):
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        file_attribute.new_attribute_button()
        with soft_assertions():
            button = WebDriverWait(file_attribute.driver, 10).until(EC.element_to_be_clickable(FileAttributePage.New_attribute_button))
            assert_that(button).is_not_none()
        file_attribute.take_screenshot()
        print("New attribute button is clickable")

    @allure.title("To test the File filter-data type functionality")
    @pytest.mark.dependency(name="Click_File_filter_button", depends=["Click_New_attribute_button"])
    @pytest.mark.parametrize("test_data", read_test_data_from_csv())
    def test_Click_File_filter_button(self, test_data):
        attributename = test_data['attribute_name'] + get_timestamp()
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        file_attribute.enter_attribute_name(attributename)
        file_attribute.click_file_filter()
        file_attribute.select_data_type()
        with soft_assertions():
            data_type_dropdown = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(FileAttributePage.data_type_dropdown))
            assert_that(data_type_dropdown).is_not_none()
        file_attribute.take_screenshot()
        print("File filter-data type functionality is clickable")

    @allure.title("To test the image File search in extraction functionality")
    @pytest.mark.dependency(name="select_only_image", depends=["Click_File_filter_button"])
    def test_select_only_image(self):
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        file_attribute.deselect_pdf_checkbox()
        file_attribute.click_test_button()
        file_attribute.download_files()
        with soft_assertions():
             download_links = WebDriverWait(file_attribute.driver, 10).until(EC.presence_of_all_elements_located(FileAttributePage.download_file))
             assert_that(download_links).is_not_empty()
        file_attribute.take_screenshot()
        print("Image file is searchable")

    @allure.title("To test the pdf File search in extraction functionality")
    @pytest.mark.dependency(name="select_only_pdf", depends=["select_only_image"])
    def test_select_only_pdf(self):
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        file_attribute.deselect_image_checkbox()
        file_attribute.select_pdf_checkbox()
        file_attribute.click_test_button()
        file_attribute.download_files()
        with soft_assertions():
            download_links = WebDriverWait(file_attribute.driver, 10).until(EC.presence_of_all_elements_located(FileAttributePage.download_file))
            assert_that(download_links).is_not_empty()
        file_attribute.take_screenshot()
        print("Pdf file is searchable")

    @allure.title("To test the image&pdf by deselecting in File extraction functionality")
    @pytest.mark.dependency(name="deselect_image_pdf", depends=["select_only_pdf"])
    def test_deselect_image_pdf(self):
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        file_attribute.deselect_pdf_checkbox()
        file_attribute.click_test_button()
        file_attribute.no_record_text()
        with soft_assertions():
            no_record = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(FileAttributePage.norecord_text))
            assert_that(no_record.text.lower()).contains("no record")
        file_attribute.take_screenshot()
        print("Image&pdf by deselecting is not searchable")

    @allure.title("To test the image&pdf by selecting in File extraction functionality")
    @pytest.mark.dependency(name="select_image_pdf", depends=["deselect_image_pdf"])
    def test_select_image_pdf(self):
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        file_attribute.select_image_checkbox()
        file_attribute.select_pdf_checkbox()
        file_attribute.click_test_button()
        file_attribute.download_files()
        with soft_assertions():
            download_links = WebDriverWait(file_attribute.driver, 10).until(EC.presence_of_all_elements_located(FileAttributePage.download_file))
            assert_that(download_links).is_not_empty()
        file_attribute.take_screenshot()
        print("Image&pdf is searchable")

    @allure.title("To test the download file button functionality in file filter")
    @pytest.mark.dependency(name="download_files", depends=["select_image_pdf"])
    def test_download_files(self):
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        file_attribute.download_files()
        with soft_assertions():
            download_links = WebDriverWait(file_attribute.driver, 10).until(EC.presence_of_all_elements_located(FileAttributePage.download_file))
            assert_that(download_links).is_not_empty()
        file_attribute.take_screenshot()
        print("Download file button is clickable")

    @allure.title("To test history button functionality in file extraction ")
    @pytest.mark.dependency(name="history_button1", depends=["download_files"])
    def test_history_button1(self):
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        file_attribute.click_history_button1()
        file_attribute.history_page_text1()
        file_attribute.take_screenshot()
        file_attribute.history_file_filter1()
        with soft_assertions():
            history_filter = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(FileAttributePage.history_file_choose1))
            assert_that(history_filter).is_not_none()
        print("History button is clickable")

    @allure.title("To test the multipage pdf-sematicsearch in extraction functionality")
    @pytest.mark.dependency(name="multipage_pdf_sematicsearch", depends=["history_button1"])
    @pytest.mark.parametrize("test_data", read_test_data_from_csv())
    def test_multipage_pdf_sematicsearch(self, test_data):
        # Extract test data
        semantic_search = test_data['multipage_text']
        prompt_text = test_data['prompt_text']
        # Initialize the Project Attribute Page
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        # Perform UI actions
        file_attribute.click_extraction_filter()
        file_attribute.click_multipage_pdf()
        file_attribute.enter_semantic_search_text(semantic_search)
        file_attribute.enter_prompt_text(prompt_text)
        file_attribute.click_test_button2()
        file_attribute.click_load_more()
        file_attribute.verify_extract_attribute_button()
        with soft_assertions():
            extract_attribute = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(FileAttributePage.extract_attribute_button))
            assert_that(extract_attribute).is_not_none()
        file_attribute.take_screenshot()

    @allure.title("To test the multipage pdf-Exactsearch in extraction functionality")
    @pytest.mark.dependency(name="exact_search", depends=["multipage_pdf_sematicsearch"])
    @pytest.mark.parametrize("test_data", read_test_data_from_csv())
    def test_exact_search(self, test_data):
        # Extract test data
        exact_search = test_data['multipage_text']
        prompt_text = test_data['prompt_text']
        # Initialize the Project Attribute Page
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        # Perform UI actions
        file_attribute.enter_exact_search_text(exact_search)
        file_attribute.enter_prompt_text(prompt_text)
        file_attribute.click_test_button2()
        file_attribute.verify_extract_attribute_button()
        with soft_assertions():
            extract_attribute = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(FileAttributePage.extract_attribute_button))
            assert_that(extract_attribute).is_not_none()
        file_attribute.take_screenshot()
        print("Exact search is working")

    @allure.title("To test the content filter functionality")
    @pytest.mark.dependency(name="content_filter", depends=["exact_search"])
    def test_content_filter(self):
        # Initialize the driver
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        # peroform UI actions
        file_attribute.click_content_filter()
        file_attribute.click_position_filter()
        file_attribute.click_zoom_level()
        with soft_assertions():
            zoom_level = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(FileAttributePage.Zoom_level))
            assert_that(zoom_level).is_not_none()
        file_attribute.take_screenshot()
        print("Content filter is clickable")

    @allure.title("To test the model 4trurbo filter functionality")
    @pytest.mark.dependency(name="model_filter_4turbo", depends=["content_filter"])
    @pytest.mark.parametrize("test_data", read_test_data_from_csv())
    def test_model_filter_4turbo(self, test_data):
        # Extract test data
        prompt_text = test_data['prompt_string']
        # Initialize the driver
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        # peroform UI actions
        file_attribute.click_extraction_filter()
        file_attribute.click_prompt_button()
        file_attribute.click_model()
        file_attribute.select_model_dropdown()
        file_attribute.select_model_name_4trurbo()
        file_attribute.enter_prompt_text(prompt_text)
        file_attribute.click_test_button2()
        file_attribute.click_load_more()
        file_attribute.verify_extract_attribute_button()
        with soft_assertions():
            extract_attribute = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(FileAttributePage.extract_attribute_button))
            assert_that(extract_attribute).is_not_none()
        file_attribute.take_screenshot() 
        print("Model 4trurbo search is working")

    @allure.title("To test the model 4omni filter functionality")
    @pytest.mark.dependency(name="model_filter_4omni", depends=["model_filter_4turbo"])
    @pytest.mark.parametrize("test_data", read_test_data_from_csv())
    def test_model_filter_4omni(self, test_data):
        # Extract test data
        prompt_text = test_data['prompt_string']
        # Initialize the driver
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        file_attribute.click_extraction_filter()
        file_attribute.click_prompt_button()
        file_attribute.click_model()
        file_attribute.select_model_dropdown()
        file_attribute.select_model_name_4omini()
        file_attribute.enter_prompt_text(prompt_text)
        file_attribute.click_test_button2()
        file_attribute.click_load_more()
        file_attribute.verify_extract_attribute_button()
        with soft_assertions():
            extract_attribute = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(FileAttributePage.extract_attribute_button))
            assert_that(extract_attribute).is_not_none
        file_attribute.take_screenshot()
        print("Model 4omni search is working")

    @allure.title("To test the model 3.5turbo filter functionality")
    @pytest.mark.dependency(name="model_filter_3.5turbo", depends=["model_filter_4omni"])
    @pytest.mark.parametrize("test_data", read_test_data_from_csv())
    def test_model_filter_3_5turbo(self, test_data):
        # Extract test data
        prompt_text = test_data['prompt_string']
        # Initialize the driver
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        # peroform UI actions
        file_attribute.click_extraction_filter()
        file_attribute.click_prompt_button()
        file_attribute.click_model()
        file_attribute.select_model_dropdown()
        file_attribute.select_model_name_35turbo()
        file_attribute.enter_prompt_text(prompt_text)
        file_attribute.click_test_button2()
        file_attribute.click_load_more()
        file_attribute.verify_extract_attribute_button()
        with soft_assertions():
            extract_attribute = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(FileAttributePage.extract_attribute_button))
            assert_that(extract_attribute).is_not_none()
        file_attribute.take_screenshot()
        print("Model 3.5turbo search is working")

    @allure.title("To test the model visionnaive filter functionality")
    @pytest.mark.dependency(name="model_filter_visionnaive", depends=["model_filter_3.5turbo"])
    @pytest.mark.parametrize("test_data", read_test_data_from_csv())
    def test_model_filter_visionnaive(self, test_data):
        # Extract test data
        prompt_text = test_data['prompt_naive']
        # Initialize the driver
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        # peroform UI actions
        file_attribute.click_extraction_filter()
        file_attribute.click_prompt_button()
        file_attribute.click_model()
        file_attribute.select_model_dropdown()
        file_attribute.select_model_name_visionnaive()
        file_attribute.enter_prompt_text(prompt_text)
        file_attribute.click_test_button2()
        file_attribute.click_load_more()
        file_attribute.verify_extract_attribute_button()
        with soft_assertions():
            extract_attribute = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(FileAttributePage.extract_attribute_button))
            assert_that(extract_attribute).is_not_none()
        file_attribute.take_screenshot()
        print("Model visionnaive search is working")

    @allure.title("To test All model listing in model filter functionality")
    @pytest.mark.dependency(name="model_filter_all", depends=["model_filter_visionnaive"])
    def test_model_filter_all(self):
        # Initialize the driver
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        # peroform UI actions
        file_attribute.click_extraction_filter()
        file_attribute.click_prompt_button()
        file_attribute.click_model()
        file_attribute.available_model()
        file_attribute.take_screenshot()
        print("All model listing is working")

    @allure.title("To test history button functionality in file extraction ")
    @pytest.mark.dependency(name="history_button2", depends=["model_filter_all"])
    def test_history_button2(self):
        # Initialize driver
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        # peroform UI actions
        file_attribute.click_history_button2()
        file_attribute.history_page_text2()
        file_attribute.take_screenshot()
        file_attribute.history_file_filter2()
        with soft_assertions():
            history_butn = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(FileAttributePage.history_button2))
            assert_that(history_butn).is_not_none()
        print("History button is clickable")

    @allure.title("To test the save as drop down box for string functionality")
    @pytest.mark.dependency(name="save_as_string", depends=["history_button2"])
    @pytest.mark.parametrize("test_data", read_test_data_from_csv())
    def test_save_as_string(self, test_data):
        # Extract test data
        attributename=test_data['attribute_string']
        prompt_text = test_data['prompt_string']
        expected_message = test_data['toast_attribute'].strip()
        # Initialize the driver
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        # peroform UI actions
        file_attribute.enter_attribute_name(attributename)
        file_attribute.click_extraction_filter()
        file_attribute.click_save_as_button()
        file_attribute.select_save_as_dropdown()
        file_attribute.select_save_as_string()
        file_attribute.enter_prompt_text(prompt_text)
        file_attribute.click_test_button2()
        file_attribute.click_load_more()
        file_attribute.verify_extract_attribute_button()
        file_attribute.click_save_button()
        file_attribute.get_toast_msg()
        with allure.step("Verify soft assertion for toast message"):
            with soft_assertions():
                success_message = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(file_attribute.toast_msg)).text
                assert_that(success_message, "Project creation failed").is_equal_to(expected_message)
                print("Toast message:",success_message)
        file_attribute.take_screenshot()
        file_attribute.click_back_button()
        file_attribute.select_setting()
        file_attribute.select_project_attribute_setting()
        file_attribute.new_attribute_button()
        with soft_assertions():
            new_attribute = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(FileAttributePage.New_attribute_button))
            assert_that(new_attribute).is_not_none()
        print("New attribute added for string functionality")

    @allure.title("To test the save as drop down box for int functionality")
    @pytest.mark.dependency(name="save_as_int", depends=["save_as_string"])
    @pytest.mark.parametrize("test_data", read_test_data_from_csv())
    def test_save_as_int(self, test_data):
        # Extract test data
        attributename=test_data['attribute_int']
        prompt_text = test_data['prompt_int']
        expected_message = test_data['toast_attribute'].strip()
        # Initialize the driver
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        # peroform UI actions
        file_attribute.enter_attribute_name(attributename)
        file_attribute.click_extraction_filter()
        file_attribute.click_save_as_button()
        file_attribute.select_save_as_dropdown()
        file_attribute.select_save_as_int()
        file_attribute.enter_prompt_text(prompt_text)
        file_attribute.click_test_button2()
        file_attribute.click_load_more()
        file_attribute.verify_extract_attribute_button()
        file_attribute.click_save_button()
        file_attribute.get_toast_msg()
        with allure.step("Verify soft assertion for toast message"):
            with soft_assertions():
                success_message = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(file_attribute.toast_msg)).text
                assert_that(success_message, "Project creation failed").is_equal_to(expected_message)
                print("Toast message:",success_message)
        file_attribute.take_screenshot()
        file_attribute.click_back_button()
        file_attribute.select_setting()
        file_attribute.select_project_attribute_setting()
        file_attribute.new_attribute_button()
        with soft_assertions():
            new_attribute = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(FileAttributePage.New_attribute_button))
            assert_that(new_attribute).is_not_none()
        print("New attribute added for Integer functionality")

    @allure.title("To test the save as drop down box for float functionality")
    @pytest.mark.dependency(name="save_as_float", depends=["save_as_int"])
    @pytest.mark.parametrize("test_data", read_test_data_from_csv())
    def test_save_as_float(self, test_data):
        # Extract test data
        attributename=test_data['attribute_float']
        prompt_text = test_data['prompt_float']
        expected_message = test_data['toast_attribute'].strip()
        # Initialize the driver
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        # peroform UI actions
        file_attribute.enter_attribute_name(attributename)
        file_attribute.click_extraction_filter()
        file_attribute.click_save_as_button()
        file_attribute.select_save_as_dropdown()
        file_attribute.select_save_as_float()
        file_attribute.enter_prompt_text(prompt_text)
        file_attribute.click_test_button2()
        file_attribute.click_load_more()
        file_attribute.verify_extract_attribute_button()
        file_attribute.click_save_button()
        file_attribute.get_toast_msg()
        with allure.step("Verify soft assertion for toast message"):
            with soft_assertions():
                success_message = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(file_attribute.toast_msg)).text
                assert_that(success_message, "Project creation failed").is_equal_to(expected_message)
                print("Toast message:",success_message)
        file_attribute.take_screenshot()
        file_attribute.click_back_button()
        file_attribute.select_setting()
        file_attribute.select_project_attribute_setting()
        file_attribute.new_attribute_button()
        with soft_assertions():
            new_attribute = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(FileAttributePage.New_attribute_button))
            assert_that(new_attribute).is_not_none()
        print("New attribute added for Float functionality")

    @allure.title("To test the save as drop down box for date functionality")
    @pytest.mark.dependency(name="save_as_date", depends=["save_as_float"])
    @pytest.mark.parametrize("test_data", read_test_data_from_csv())
    def test_save_as_date(self, test_data):
        # Extract test data
        attributename=test_data['attribute_date']
        prompt_text = test_data['prompt_date']
        expected_message = test_data['toast_attribute'].strip()
        # Initialize the driver
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        # peroform UI actions
        file_attribute.enter_attribute_name(attributename)
        file_attribute.click_extraction_filter()
        file_attribute.click_save_as_button()
        file_attribute.select_save_as_dropdown()
        file_attribute.select_save_as_date()
        file_attribute.enter_prompt_text(prompt_text)
        file_attribute.click_test_button2()
        file_attribute.click_load_more()
        file_attribute.verify_extract_attribute_button()
        file_attribute.click_save_button()
        file_attribute.get_toast_msg()
        with allure.step("Verify soft assertion for toast message"):
            with soft_assertions():
                success_message = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(file_attribute.toast_msg)).text
                assert_that(success_message, "Project creation failed").is_equal_to(expected_message)
                print("Toast message:",success_message)
        file_attribute.take_screenshot()
        file_attribute.click_back_button()
        file_attribute.select_setting()
        file_attribute.select_project_attribute_setting()
        file_attribute.new_attribute_button()
        with soft_assertions():
            new_attribute = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(FileAttributePage.New_attribute_button))
            assert_that(new_attribute).is_not_none()
        print("New attribute added for date functionality")

    @allure.title("To test the save as drop down box for boolean functionality")
    @pytest.mark.dependency(name="save_as_boolean", depends=["save_as_date"])
    @pytest.mark.parametrize("test_data", read_test_data_from_csv())
    def test_save_as_boolean(self, test_data):
        # Extract test data
        attributename=test_data['attribute_boolean']
        prompt_text = test_data['prompt_boolean']
        expected_message = test_data['toast_attribute'].strip()
        # Initialize the driver
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        # peroform UI actions
        file_attribute.enter_attribute_name(attributename)
        file_attribute.click_extraction_filter()
        file_attribute.click_save_as_button()
        file_attribute.select_save_as_dropdown()
        file_attribute.select_save_as_boolean()
        file_attribute.enter_prompt_text(prompt_text)
        file_attribute.click_test_button2()
        file_attribute.click_load_more()
        file_attribute.verify_extract_attribute_button()
        file_attribute.click_save_button()
        with allure.step("Verify soft assertion for toast message"):
            with soft_assertions():
                success_message = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(file_attribute.toast_msg)).text
                assert_that(success_message, "Project creation failed").is_equal_to(expected_message)
                print("Toast message:",success_message)
        file_attribute.take_screenshot()
        file_attribute.click_back_button()
        file_attribute.select_setting()
        file_attribute.select_project_attribute_setting()
        file_attribute.new_attribute_button()
        with soft_assertions():
            new_attribute = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(FileAttributePage.New_attribute_button))
            assert_that(new_attribute).is_not_none()
        print("New attribute added for boolean functionality")

    @allure.title("To test the save as drop down box for datetime functionality")
    @pytest.mark.dependency(name="save_as_datetime", depends=["save_as_boolean"])
    @pytest.mark.parametrize("test_data", read_test_data_from_csv())
    def test_save_as_datetime(self, test_data):
        # Extract test data
        attributename=test_data['attribute_datetime']
        prompt_text = test_data['prompt_datetime']
        expected_message = test_data['toast_attribute'].strip()
        # Initialize the driver
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        # peroform UI actions
        file_attribute.enter_attribute_name(attributename)
        file_attribute.click_extraction_filter()
        file_attribute.click_save_as_button()
        file_attribute.select_save_as_dropdown()
        file_attribute.select_save_as_datetime()
        file_attribute.enter_prompt_text(prompt_text)
        file_attribute.click_test_button2()
        file_attribute.click_load_more()
        file_attribute.verify_extract_attribute_button()
        file_attribute.click_save_button()
        with allure.step("Verify soft assertion for toast message"):
            with soft_assertions():
                success_message = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(file_attribute.toast_msg)).text
                assert_that(success_message, "Project creation failed").is_equal_to(expected_message)
                print("Toast message:",success_message)
        file_attribute.take_screenshot()
        file_attribute.click_back_button()
        file_attribute.select_setting()
        file_attribute.select_project_attribute_setting()
        file_attribute.new_attribute_button()
        with soft_assertions():
            new_attribute = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(FileAttributePage.New_attribute_button))
            assert_that(new_attribute).is_not_none()
        print("New attribute added for datetime functionality")

    @allure.title("To test the save as drop down box for time functionality")
    @pytest.mark.dependency(name="save_as_time", depends=["save_as_datetime"])
    @pytest.mark.parametrize("test_data", read_test_data_from_csv())
    def test_save_as_time(self, test_data):
        # Extract test data
        attributename=test_data['attribute_time']
        prompt_text = test_data['prompt_time']
        expected_message = test_data['toast_attribute'].strip()
        # Initialize the driver
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        # peroform UI actions
        file_attribute.enter_attribute_name(attributename)
        file_attribute.click_extraction_filter()
        file_attribute.click_save_as_button()
        file_attribute.select_save_as_dropdown()
        file_attribute.select_save_as_time()
        file_attribute.enter_prompt_text(prompt_text)
        file_attribute.click_test_button2()
        file_attribute.click_load_more()
        file_attribute.verify_extract_attribute_button()
        file_attribute.click_save_button()
        with allure.step("Verify soft assertion for toast message"):
            with soft_assertions():
                success_message = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(file_attribute.toast_msg)).text
                assert_that(success_message, "Project creation failed").is_equal_to(expected_message)
                print("Toast message:",success_message)
        file_attribute.take_screenshot()
        file_attribute.click_back_button()
        file_attribute.select_setting()
        file_attribute.select_project_attribute_setting()
        file_attribute.new_attribute_button()
        with soft_assertions():
            new_attribute = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(FileAttributePage.New_attribute_button))
            assert_that(new_attribute).is_not_none()
        print("New attribute added for time functionality")
    
    @allure.title("To test the save as drop down box for json functionality")
    @pytest.mark.dependency(name="save_as_json", depends=["save_as_time"])
    @pytest.mark.parametrize("test_data", read_test_data_from_csv())
    def test_save_as_json(self, test_data):
        # Extract test data
        attributename=test_data['attribute_json']
        prompt_text = test_data['prompt_json']
        expected_message = test_data['toast_attribute'].strip()
        # Initialize the driver
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        # peroform UI actions
        file_attribute.enter_attribute_name(attributename)
        file_attribute.click_extraction_filter()
        file_attribute.click_save_as_button()
        file_attribute.select_save_as_dropdown()
        file_attribute.select_save_as_json()
        file_attribute.enter_prompt_text(prompt_text)
        file_attribute.click_test_button2()
        file_attribute.click_load_more()
        file_attribute.verify_extract_attribute_button()
        file_attribute.click_save_button()
        with allure.step("Verify soft assertion for toast message"):
            with soft_assertions():
                success_message = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(file_attribute.toast_msg)).text
                assert_that(success_message, "Project creation failed").is_equal_to(expected_message)
                print("Toast message:",success_message)
        file_attribute.take_screenshot()
        file_attribute.click_back_button()
        file_attribute.select_setting()
        file_attribute.select_project_attribute_setting()
        file_attribute.new_attribute_button()
        with soft_assertions():
            new_attribute = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(FileAttributePage.New_attribute_button))
            assert_that(new_attribute).is_not_none()
        print("New attribute added for json functionality")

    @allure.title("To test the save as drop down box for table functionality")
    @pytest.mark.dependency(name="save_as_table", depends=["save_as_json"])
    @pytest.mark.parametrize("test_data", read_test_data_from_csv())
    def test_save_as_table(self, test_data):
        # Extract test data
        attributename=test_data['attribute_table']
        keycolumn1_text=test_data['key_coumn_name1']
        keycolumn2_text1=test_data['key_coumn_name2']
        prompt_text = test_data['prompt_table']
        expected_message = test_data['toast_attribute'].strip()
        # Initialize the driver
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        # peroform UI actions
        file_attribute.click_extraction_filter()
        file_attribute.enter_attribute_name(attributename)
        file_attribute.click_save_as_button()
        file_attribute.select_save_as_dropdown()
        file_attribute.select_save_as_table()
        file_attribute.enter_key_column1_name(keycolumn1_text)
        file_attribute.select_key_column1_type()
        file_attribute.click_add_column()
        file_attribute.enter_key_column2_name(keycolumn2_text1)
        file_attribute.select_key_column2_type()
        file_attribute.select_key_type_int()
        file_attribute.enter_prompt_text(prompt_text)
        file_attribute.click_test_button2()
        file_attribute.click_load_more()
        file_attribute.verify_extract_attribute_button()
        file_attribute.click_save_button()
        with allure.step("Verify soft assertion for toast message"):
            with soft_assertions():
                success_message = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(file_attribute.toast_msg)).text
                assert_that(success_message, "Project creation failed").is_equal_to(expected_message)
                print("Toast message:",success_message)
        file_attribute.take_screenshot()
        file_attribute.click_back_button()
        print("New attribute added for table functionality")
    
    @allure.title("To test the added attribute is in the list")
    @pytest.mark.dependency(name="attribute_list", depends=["save_as_table"])
    def test_attribute_list(self):
        # Initialize the driver
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        # peroform UI actions
        file_attribute.check_attribute_name()
        file_attribute.take_screenshot()
        print("Attribute is added in the list")

    @allure.title("To test the edit setting functionality")
    @pytest.mark.dependency(name="edit_setting", depends=["attribute_list"])
    def test_edit_setting(self):
        # Initialize the driver
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        # peroform UI actions
        file_attribute.click_edit_setting()
        with soft_assertions():
            edit_setting = WebDriverWait(file_attribute.driver, 10).until(EC.visibility_of_element_located(FileAttributePage.edit_setting))
            assert_that(edit_setting).is_not_none()
        file_attribute.take_screenshot()
        print("Edit setting is working")

    @allure.title("To test the delete setting functionality")
    @pytest.mark.dependency(name="delete_setting", depends=["edit_setting"])
    def test_delete_setting(self):
        # Initialize the driver
        file_attribute = FileAttributePage(InitDriver.init_driver().get_web_driver())
        # peroform UI actions
        file_attribute.click_delete_attribute()
        file_attribute.accept_alert()
        file_attribute.take_screenshot()
        print("Delete setting is working")
