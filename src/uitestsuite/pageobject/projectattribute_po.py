from selenium.webdriver.common.by import By
from src.uitestsuite.pageobject.base_po import BasePage
import allure
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProjectAttributePage(BasePage):

    #test_Tc_001
    setting_button = (By.XPATH, "//div[1]/div[2]/a[1]/i[1]")
    project_attribute_setting = (By.XPATH, "//span[normalize-space()='Project Attribute Setting']")
    #test_Tc_002
    New_attribute_button = (By.XPATH, "//a[contains(@href,'entity_attributes/new')]")
    #test_Tc_003
    toggle_button = (By.XPATH, "//div[2]/label[1]/div[1]")
    attribute_name_text = (By.XPATH, "//input[@id='attribute-name']")
    file_filterbutton= (By.XPATH, "//p[normalize-space()='File filter']")
    data_type= (By.XPATH, "//h6[normalize-space()='Data type']")
    data_type_dropdown= (By.XPATH, "//div[@class='col-span-12']//select")
    #test_Tc_004,005,006,007,008
    file_image_checkbox= (By.XPATH, "//input[@value='Image']")
    file_pdf_checkbox= (By.XPATH, "//input[@value='PDF']")
    download_file= (By.XPATH, "//a[normalize-space()='Download Files']")
    norecord_text= (By.XPATH, "//div[contains(text(),'No record')][1]")
    test_button= (By.XPATH, "//div[2]/div[1][contains(text(),'Test')][1]")
    #test_Tc_009
    extraction_filterbutton= (By.XPATH, "//p[normalize-space()='Extraction']")
    mulpage_pdf= (By.XPATH, "//h6[normalize-space()='Page filter for multi-page PDF']")
    mulpage_dropdown= (By.XPATH, "//div[1]/div[2]/div[1]/select[1]")
    exactsearch= (By.XPATH, "(//option[normalize-space()='Exact search'])[2]")
    mulpage_textbox= (By.XPATH, "(//input[@placeholder='Input text'])[2]")
    prompt_text = (By.NAME, "prompt")
    test_button2= (By.XPATH, "(//div[contains(text(),'Test')])[2]")
    loadmore_button= (By.XPATH, "//div[normalize-space()='Load more']")
    extract_attribute_button= (By.XPATH, "(//div[contains(text(),'Extract attribute')])")

    #History_filefilter
    history_button1= (By.XPATH, "//div[2]/div[2]/div[1]/i[1]")
    history_page1= (By.XPATH, "//div[2]/div[1][@class='no-scrollbar overflow-scroll']")
    history_file_choose1= (By.XPATH, "//div[2]/div[1]/div[1]/div[2]/div[3]/div[2]")

    history_button2= (By.XPATH, "//div[3]/div[2]/div[1]/i[1]")
    history_page2= (By.XPATH, "//div[3]/div[1][@class='no-scrollbar overflow-scroll']")
    history_file_choose2= (By.XPATH, "//div[3]/div[1]/div[1]/div[2]/div[1]/div[2]")
    history_file_close= (By.XPATH, "(//i[@class='bx bx-x'])[1]")
    
    #test_Tc_010
    content_filter= (By.XPATH, "//h6[normalize-space()='Content filter']")   
    position_filter= (By.XPATH, "//p[normalize-space()='Position:']") 
    Zoom_level= (By.XPATH, "//p[normalize-space()='Zoom Level']")
    #test_Tc_011
    prompt_button= (By.XPATH, "//h6[normalize-space()='Prompt setting']")
    model= (By.XPATH, "//p[normalize-space()='Model:']")
    model_dropdown= (By.XPATH, "//div[3]/div[2]/div[1]/div[2]/select[1]")
    model_name_4trurbo= (By.XPATH, "//option[@value='openai-gpt-4-turbo']")
    model_name_4omini= (By.XPATH, "//option[@value='openai-gpt-4-omni']")
    model_name_35turbo= (By.XPATH, "//option[@value='openai-gpt-3.5-turbo-0125']")
    model_name_4omini= (By.XPATH, "//option[@value='openai-gpt-4-omni']")
    model_name_visionnaive= (By.XPATH, "//option[@value='openai-gpt-4-omni-vision-naive']")
    save_as_button= (By.XPATH, "//p[normalize-space()='Save as:']")
    #save_as_dropdown= (By.XPATH, "//div[3]/div[2]/div[2]/div[2]/select[1]")
    save_as_dropdown= (By.XPATH, "//select[@name='save-as']")
    save_as_string= (By.XPATH, "//option[normalize-space()='String']")
    save_as_int= (By.XPATH, "//option[normalize-space()='Int']")
    save_as_float= (By.XPATH, "//option[normalize-space()='Float']")
    save_as_date= (By.XPATH, "//option[normalize-space()='Date']")
    save_as_boolean= (By.XPATH, "//option[normalize-space()='Boolean']")
    save_as_datetime= (By.XPATH, "//option[normalize-space()='Datetime']")
    save_as_time= (By.XPATH, "//option[normalize-space()='Time']")
    save_as_json= (By.XPATH, "//option[normalize-space()='Json']")
    save_as_table= (By.XPATH, "//option[normalize-space()='Table']")

    #for table dropdown
    key_column1_name= (By.XPATH, "//input[@name='column-name-0']")
    key_column1_type= (By.XPATH, "//select[@name='column-type-0']")
    key_column2_name= (By.XPATH, "//input[@name='column-name-1']")
    key_column2_type= (By.XPATH, "//select[@name='column-type-1']")
    add_column= (By.XPATH, "//span[normalize-space()='Add Column']")

    #key colum type dropdowns
    key_type_string= (By.XPATH, "//select[@name='column-type-0']//option[normalize-space()='String']")
    key_type_int= (By.XPATH, "//select[@name='column-type-0']//option[normalize-space()='Int']")
    key_type_float= (By.XPATH, "//select[@name='column-type-0']//option[normalize-space()='Float']")
    key_type_date= (By.XPATH, "//select[@name='column-type-0']//option[normalize-space()='Date']")
    key_type_boolean= (By.XPATH, "//select[@name='column-type-0']//option[normalize-space()='Boolean']")
    key_type_datetime= (By.XPATH, "//select[@name='column-type-0']//option[normalize-space()='Datetime']")
    key_type_time= (By.XPATH, "//select[@name='column-type-0']//option[normalize-space()='Time']")
    key_type_json= (By.XPATH, "//select[@name='column-type-0']//option[normalize-space()='JSON']")

    #Attribute save & back
    save_button=(By.XPATH, "//div[contains(text(),'Save')]")
    back_button = (By.XPATH, "//div[@class='flex cursor-pointer items-center text-gray-100 hover:text-black']")

    project_attribute_list= (By.XPATH, "//div[@class='table-responsive overflow-scroll h-[calc(100vh-440px)]']")
    #toast_msg = (By.XPATH, "//div[@class='v-toast v-toast--bottom']")
    toast_msg = (By.XPATH, "//p[@class='v-toast__text']")

    edit_setting=(By.XPATH, "//tr[1]/td[6]/div[1]/a[1]")
    delete_attribute=(By.XPATH, "//span[normalize-space()='Delete']")

    #1
   # Comon method
    def select_setting(self):
            setting=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.setting_button))
            setting.click()
            print("Setting selected")
            return self
    def select_project_attribute_setting(self):
        with allure.step("Click on Project Attribute Setting"):
            pro_attribute=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.project_attribute_setting))
            pro_attribute.click()
            self.wait_for_5sec()
            print("Project Attribute Setting selected")
            return self
    def take_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(),name="screenshot",attachment_type=allure.attachment_type.PNG)
    #2
    def new_attribute_button(self):
        with allure.step("Click on New attribute button"):
            new_attribute=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.New_attribute_button))
            new_attribute.click()
            print("New attribute button selected")
            return self
    #3
    def enter_attribute_name(self, name):
        with allure.step("Enter attribute name"):
            attribute_name_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.attribute_name_text))
            attribute_name_field.clear()
            attribute_name_field.send_keys(name)
            print("Attribute name entered")
            return self
    # Filter option
    def click_file_filter(self):
        with allure.step("Click File filter button"):
            file_filter= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.file_filterbutton))
            file_filter.click()
            print("File filter selected")
            return self
    def click_extraction_filter(self):
        with allure.step("Click Extraction filter button"):
            extraction_filter=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.extraction_filterbutton))
            extraction_filter.click()
            print("Extraction filter selected")
            return self

    # File filter:Data type
    def select_data_type(self):
        with allure.step("Select Data type"):
            data_type_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.data_type))
            data_type_field.click()
            data_type_field=data_type_field.text
            print("Data type text:", data_type_field)
            data_type_dropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.data_type_dropdown))
            data_type_dropdown.click()
            return self

    # File filter:File extensions:Select & desekect image and pdf
    def deselect_pdf_checkbox(self):
        with allure.step("Deselect File PDF"):
            deselect_pdfcheckbox= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.file_pdf_checkbox))
            deselect_pdfcheckbox.click()
            print("PDF checkbox deselected")
            return self
    def deselect_image_checkbox(self):
        with allure.step("Deselect File Image"):
            deselect_imagecheckbox= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.file_image_checkbox))
            deselect_imagecheckbox.click()
            print("Image checkbox deselected")
            return self 
    def select_image_checkbox(self):
        with allure.step("Select File Image"):
            select_imagecheckbox=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.file_image_checkbox))
            select_imagecheckbox.click()
            print("Image checkbox selected")
            return self
    def select_pdf_checkbox(self):
        with allure.step("Select File PDF"):
            select_pdfcheckbox=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.file_pdf_checkbox))
            select_pdfcheckbox.click()
            print("PDF checkbox selected")
            return self
    def no_record_text(self):
        with allure.step("No record text"):
            no_record=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.norecord_text))
            print("No record text:", no_record.text)
            return self

    # Click History file filter
    def click_history_button1(self):
        with allure.step("Click on History file filter"):
            history_file_filter=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.history_button1))
            history_file_filter.click()
            print("History file filter selected")
            return self
    def history_page_text1(self):
        with allure.step("History page text"):
            history_page=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.history_page1))
            print("History page text:", history_page.text)
            return self
    def history_file_filter1(self):
        with allure.step("History file choose"):
            history_file_choose=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.history_file_choose1))
            history_file_choose.click()
            print("History file selected")
            return self

    def click_history_button2(self):
        with allure.step("Click on History file filter"):
            history_file_filter=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.history_button2))
            history_file_filter.click()
            print("History file filter selected")
            return self
    def history_page_text2(self):
        with allure.step("History page text"):
            history_page=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.history_page2))
            print("History page text:", history_page.text)
            return self
    def history_file_filter2(self):
        with allure.step("History file choose"):
            history_file_choose=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.history_file_choose2))
            history_file_choose.click()
            history_file_close=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.history_file_close))
            history_file_close.click()
            print("History file selected")
            return self

    # Click Test button:only for file filter
    def click_test_button(self):
        with allure.step("Click on Test button"):
            testbutton= WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.test_button))
            testbutton.click()
            self.wait_for_5sec()
            print("Test button selected")
            return self
    # Click Test button:only for extraction
    def click_test_button2(self):
        with allure.step("Click on Test button"):
            testbutton2= WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.test_button2))
            testbutton2.click()
            self.wait_for_5sec()
            print("Test button selected")
            return self
    
    # Download files
    def download_files(self):
        with allure.step("Downloaded files count"):
            try:
                download_files = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(self.download_file))
                print("Downloaded files count:", len(download_files))
            except TimeoutException:
                print("No download file found.")
                return self
    def download_files_click(self):
        try:
            download_files = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(self.download_file))
            if download_files:
                for file in download_files:
                    file.click()
                    self.wait_for_5sec()
                print("Downloaded files count:", len(download_files))
            else:
                print("No download file found")
        except TimeoutException:
            print("No download file found.") 
            return self

    # Extraction filter: Page filter for multi-page PDF:
    def click_multipage_pdf(self):
        with allure.step("Click on Multipage pdf"):
            multipage_pdf=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.mulpage_pdf))
            print("Multipage pdf text:", multipage_pdf.text)
            multipage_pdf.click()
            return self
    # Extraction filter: Page filter for multi-page PDF: All searches
    def enter_semantic_search_text(self, text):
        with allure.step("Enter semantic search text"):
            text_box=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.mulpage_textbox))
            text_box.clear()
            text_box.send_keys(text)
            print("Semantic search text entered")
            return self
    def enter_exact_search_text(self, text):
        with allure.step("Enter exact search text"):
            drop_down=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.mulpage_dropdown))
            drop_down.click()
            exact_search=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.exactsearch))
            exact_search.click()
            text_box=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.mulpage_textbox))
            text_box.clear()
            text_box.send_keys(text)
            print("Exact search text entered")
            return self

    # Search result load more
    def click_load_more(self):
        try:
                load_more = WebDriverWait(self.driver, 10).until( EC.element_to_be_clickable(self.loadmore_button))
                if load_more.is_displayed():
                    load_more.click()
                    self.wait_for_5sec()
                else:
                    print("No 'Load More' button found or no more items to load. Continuing test...")
        except TimeoutException:
            print("No 'Load More' button found or no more items to load. Continuing test...")
        return self
    
    # Search result extract attribute
    def verify_extract_attribute_button(self):
        try:
            extract_attributes = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(self.extract_attribute_button))
            if extract_attributes:
                print("Extract attribute button count:", len(extract_attributes))
                assert len(extract_attributes) > 0, "Extract Attribute button is not available"
            if len(extract_attributes) > 0:
                extract_attributes[1].click()
                self.wait_for_5sec()
        except TimeoutException:
            print("Extract Attribute button not found, continuing with the next test case.")

    # Extraction filter: Content filter
    def click_content_filter(self):
        with allure.step("Click on Content filter"):
            extraction_filter=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.extraction_filterbutton))
            extraction_filter.click()
            content_filter=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.content_filter))
            content_filter.click()
            print("Content filter text:", content_filter.text)
            return self
    def click_position_filter(self):
        with allure.step("Click on Position filter"):
            position_filter=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.position_filter))
            position_filter.click()
            print("Position filter text:", position_filter.text)
            return self
    def click_zoom_level(self):
        with allure.step("Click on Zoom level"):
            zoom_level=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.Zoom_level))
            zoom_level.click()
            print("Zoom level text:", zoom_level.text)
            return self

    # Extraction filter: Promt setting
    def click_prompt_button(self):
        with allure.step("Click on Prompt button"):
            prompt_button=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.prompt_button))
            print("Prompt button text:", prompt_button.text)
            return self
    def click_model(self):
        with allure.step("Click on Model"):
            model=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.model))
            model.click()
            print("Model text:", model.text)
            return self
    def select_model_dropdown(self):
        with allure.step("Select Model dropdown"):
            model_dropdown=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.model_dropdown))
            model_dropdown.click()
            return self
    def select_model_name_4trurbo(self):
        with allure.step("Select Model name 4trurbo"):
            model_name=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.model_name_4trurbo))
            model_name.click()
            print("Model name text:", model_name.text)
            return self
    def select_model_name_35turbo(self):
        with allure.step("Select Model name 3.5turbo"):
            model_name=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.model_name_35turbo))
            model_name.click()
            print("Model name text:", model_name.text)
            return self
    def select_model_name_4omini(self):
        with allure.step("Select Model name 4omini"):
            model_name=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.model_name_4omini))
            model_name.click()
            print("Model name text:", model_name.text)
            return self
    def select_model_name_visionnaive(self):
        with allure.step("Select Model name visionnaive"):
            model_name=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.model_name_visionnaive))
            model_name.click()
            print("Model name text:", model_name.text)
            return self
    def available_model(self):
        with allure.step("available model"):
            model_dropdown=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.model_dropdown))
            model_dropdown.click()
            print("Model dropdown text:", model_dropdown.text)
            return self
    def click_save_as_button(self):
        with allure.step("Click on Save as button"):
            save_as_button=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.save_as_button))
            save_as_button.click()
            print("Save as button text:", save_as_button.text)
            return self
    def select_save_as_dropdown(self):
        with allure.step("Select Save as dropdown"):
            save_as_dropdown=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.save_as_dropdown))
            save_as_dropdown.click()
            print("Save as dropdown text:", save_as_dropdown.text)
            return self
    def select_save_as_string(self):
        with allure.step("Select Save as string"):
            save_as_string=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.save_as_string))
            save_as_string.click()
            print("Save as string text:", save_as_string.text)
            return self
    def select_save_as_int(self):
        with allure.step("Select Save as int"):
            save_as_int=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.save_as_int))
            save_as_int.click()
            print("Save as int text:", save_as_int.text)
            return self
    def select_save_as_float(self):
        with allure.step("Select Save as float"):
            save_as_float=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.save_as_float))
            save_as_float.click()
            print("Save as float text:", save_as_float.text)
            return self
    def select_save_as_date(self):
        with allure.step("Select Save as date"):
            save_as_date=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.save_as_date))
            save_as_date.click()
            print("Save as date text:", save_as_date.text)
            return self
    def select_save_as_boolean(self):
        with allure.step("Select Save as boolean"):
            save_as_boolean=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.save_as_boolean))
            save_as_boolean.click()
            print("Save as boolean text:", save_as_boolean.text)
            return self
    def select_save_as_datetime(self):
        with allure.step("Select Save as datetime"):
            save_as_datetime=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.save_as_datetime))
            save_as_datetime.click()
            print("Save as datetime text:", save_as_datetime.text)
            return self
    def select_save_as_time(self):
        with allure.step("Select Save as time"):
            save_as_time=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.save_as_time))
            save_as_time.click()
            print("Save as time text:", save_as_time.text)
            return self
    def select_save_as_json(self):
        with allure.step("Select Save as json"):
            save_as_json=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.save_as_json))
            save_as_json.click()
            print("Save as json text:", save_as_json.text)
            return self
    def select_save_as_table(self):
        with allure.step("Select Save as table"):
            save_as_table=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.save_as_table))
            save_as_table.click()
            print("Save as table text:", save_as_table.text)
            return self
    def enter_key_column1_name(self, name):
        with allure.step("Enter key column1 name"):
            key_column1_name=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.key_column1_name))
            key_column1_name.clear()
            key_column1_name.send_keys(name)
            print("Key column1 name entered")
            return self
    def enter_key_column2_name(self, name):
        with allure.step("Enter key column2 name"):
            key_column2_name=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.key_column2_name))
            key_column2_name.clear()
            key_column2_name.send_keys(name)
            print("Key column2 name entered")
            return self
    def select_key_column1_type(self):
        with allure.step("Select key column1 type"):
            key_column1_type=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.key_column1_type))
            key_column1_type.click()
            print("Key column1 type selected")
            return self
    def select_key_column2_type(self):
        with allure.step("Select key column2 type"):
            key_column2_type=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.key_column2_type))
            key_column2_type.click()
            print("Key column2 type selected")
            return self
    def click_add_column(self):
        with allure.step("Click on Add column"):
            add_column=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_column))
            add_column.click()
            print("Add column selected")
            return self
    def select_key_type_string(self):
        with allure.step("Select key type string"):
            key_type_string=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.key_type_string))
            key_type_string.click()
            print("Key type string selected")
            return self
    def select_key_type_int(self):
        with allure.step("Select key type int"):
            key_type_int=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.key_type_int))
            key_type_int.click()
            print("Key type int selected")
            return self


    # Save button
    def click_save_button(self):
        with allure.step("Click on Save button"):
            save_button=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.save_button))
            save_button.click()
            print("Save button clicked")
            return self
    def get_toast_msg(self):
        with allure.step("Get toast message"):
            toast_msg=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.toast_msg))
            print("Toast message:", toast_msg.text)
            return self
    # Back button
    def click_back_button(self):
        with allure.step("Click on Back button"):
            back_button=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.back_button))
            back_button.click()
            self.wait_for_5sec()
            print("Back button clicked")
            return self
#Extraction filter: PROMPT
    def enter_prompt_text(self, text):
        with allure.step("Enter prompt text"):
            prompt=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.prompt_text))
            prompt.clear()
            prompt.send_keys(text)
            print("Prompt text entered")
            return self

# Main page Attributes
    def check_attribute_name(self):
        with allure.step("Check attribute name"):
            try:
                element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.project_attribute_list))
                text = element.text
                attrs = ["String-p", "Int-p", "Float-p", "Date-p", "Boolean-p", "Dateandtime-p", "Time-p", "Json-p", "Table-p"]
                present = []
                not_present = []
                for attr in attrs:
                    if attr in text:
                        present.append(attr)
                    else:
                        not_present.append(attr)

                print("Present: " + str(present))
                print("Not Present: " + str(not_present))

            except TimeoutException:
                print("Element not found")
             

    def click_edit_setting(self):
        with allure.step("Click on Edit setting"):
            edit_setting=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.edit_setting))
            edit_setting.click()
            print("Edit setting selected")
            return self
    def click_delete_attribute(self):
        with allure.step("Click on Delete attribute"):
            delete_attribute=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.delete_attribute))
            delete_attribute.click()
            print("Delete attribute selected")
            return self

    #Alert Handling
    def accept_alert(self):
        with allure.step("Accept alert"):
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print("Alert text:", alert_text)
            alert.accept()
            print("OK")
            return self
    def dismiss_alert(self):
        with allure.step("Dismiss alert"):
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print("Alert text:", alert_text)
            alert.dismiss()
            print("Cancel") 
            return self
        
    def exsiting_attribute_delete(self):
        with allure.step("Project attribute delete"):
            try:
                element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.project_attribute_list))
                text = element.text
                attrs = ["String-p", "Int-p", "Float-p", "Date-p", "Boolean-p", "Dateandtime-p", "Time-p", "Json-p", "Table-p"]
                for attr in attrs:
                    if attr in text:
                        print(f"Deleting attribute: {attr}")
                        self.click_edit_setting()
                        self.click_delete_attribute()
                        self.accept_alert()
                    else:
                        print(f"Attribute {attr} not found")
            except TimeoutException:
                print("Element not found")
            return self
