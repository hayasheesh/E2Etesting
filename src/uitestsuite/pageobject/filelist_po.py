from selenium.webdriver.common.by import By
from src.uitestsuite.pageobject.base_po import BasePage
from src.util.file_operations import get_file_operations_by_os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import os
class FileListPage(BasePage):
    #locaters
    #1 for folder creating
    add_folder_button = (By.ID, "addNewFolderButton")
    folder_name_input = (By.ID, "input_file_name")
    create_folder_button = (By.XPATH, "//input[@value='Create Folder']")
    folder_names = (By.XPATH, "//div[contains(@class, 'flex') and not(contains(text(),'Previous'))]")
    qa_folder = (By.XPATH, "//a[contains(@href, 'input_files') and contains(., 'QA_Folder')]")
    #2 for file uploading (success and fail)
    upload_button = (By.XPATH, "//button[@data-tw-target='#upload-file-modal']")
    file_upload_input = (By.XPATH, "//input[@type='file']")
    progress_bar = (By.XPATH, "//span[@class='inner-progress bg-success' and @data-file-upload-section-target='progressBar']")
    progress_text = (By.XPATH, "//span[@data-file-upload-section-target='overallProgressText']")
    close_button = (By.XPATH, "//button[@data-file-upload-section-target='modalDialogCloseButton']")
    uploaded_file = (By.XPATH, "//div[@class='flex max-h-[65px] break-words overflow-scroll no-scrollbar']")
    before_upload = (By.XPATH, "//td[@class='p-10 text-gray-200 text-center']")

    #3 for file viewing
    
    
    list_view_button = (By.XPATH, "//a[contains(@href, 'list_mode=list')]")
    #list_view_button = (By.CSS_SELECTOR, "//a[data-turbo='true'][href*='list_mode=list']")
    grid_view_button = (By.CSS_SELECTOR,"a[data-turbo='true'][href*='list_mode=grid']")
    preview_button = By.CSS_SELECTOR, "button[data-input-files-preview-modal-opener='true']"
    #grid_view_button  = (By.XPATH, "//i[@class='bx bx-list-ul relative']")
    #list_view_button = (By.XPATH, "//i[@class='bx bx-grid-alt relative']")
    grid_block1 = (By.XPATH, "//a[contains(text(),'jpg.jpg')]")
    grid_block2 = (By.XPATH, "//a[contains(text(),'tif.tif')]")
    grid_block3 = (By.XPATH, "//a[contains(text(),'xlsx.xlsx')]")
    grid_block4 = (By.XPATH, "//a[contains(text(),'pdf.pdf')]")
    #grid_block1 = (By.XPATH, "//div[@class='card-body py-3']//div[text()='jpg.jpg']")
    #grid_block2 = (By.XPATH, "//div[@class='card-body py-3']//div[text()='tif.tif']")
    #grid_block3 = (By.XPATH, "//div[@class='card-body py-3']//div[text()='xlsx.xlsx']")
    #grid_block4 = (By.XPATH, "//div[@class='card-body py-3']//div[text()='pdf.pdf']")
    preview_1 = (By.XPATH, "//img[@alt='jpg.jpg']")
    preview_2 = (By.XPATH, "//img[@alt='tif.tif']")
    preview_3 = (By.XPATH, "//div[text()='xlsx']")
    preview_4 = (By.XPATH, "//img[@alt='pdf.pdf']")
    exit_preview_button = (By.XPATH, "//*[@id='inputFilesPreviewModal']//button[contains(@class, 'close-btn')]")
    #4 for file renaming
    file_settings_button_1 = (By.XPATH, "//button[@id='file-setting-btn']")
    file_settings_button_3 = (By.XPATH, "(//button[@id='file-setting-btn'])[3]")
    
    # file_settings_button_1 = (By.XPATH, "(//button[@data-test-id='file-setting-btn'])[1]")
        ##this file setting button_2 is for the in-folder page but the file setting button_1 is for the file list page.
    file_select_button = (By.XPATH, "input[data-multifiles-manager-file-name-param='jpg.jpg']")
    file_select1_button = (By.XPATH, "input[data-multifiles-manager-file-name-param='pdf.pdf']")
   
    #rename_button = (By.XPATH, "/html/body/div[8]/div/div/turbo-frame/div[1]/table/tbody/tr[1]/td[2]/div/div/ul/li[1]/button")
    rename_button = (By.XPATH, "//span[text()='Rename']")
    file_name_input = (By.XPATH, "//input[@id='input_file_file_name']")
    update_button = (By.XPATH, "//input[@value='Update']")
    success_msg= (By.XPATH, "//div[@class='pt-1']")
    updated_name = (By.XPATH, "//div[@class='flex max-h-[65px] break-words overflow-scroll no-scrollbar' and text()='jpg1.jpg']")
    project_home =(By.XPATH, "//i[@class='bx bx-building-house ltr:mr-2 align-middle mb-[2px]']")
    #5 for file moving  
    file_move_button = (By.XPATH, "//span[text()='Move']")
    folder_select_dropdown = (By.ID, "input_file_parent_id")
    folder_select_dropdown_2 = (By.ID, "input_file_record_id")
    confirm_move_button = (By.XPATH, "//input[@type='submit' and @value='Move']")
    move_target_folder_confirm_1= (By.XPATH, "//*[contains(., 'Automation_folder')]")
    move_target_folder_confirm = (By.XPATH, "//*[contains(., 'QA_Folder_move')]")
    
    move_target_project_confirm = (By.XPATH, "//span[text()='QA_Upload2']")

    #6 for file downloading
    download_button = (By.XPATH, "//span[text()='Download']")
    #7 for file deleting
    file_settings_button_2 = (By.XPATH, "/html/body/div[6]/div/div/div[2]/div[2]/table/tbody/tr[1]/td[2]/div/div/button")
    deleting_button = (By.XPATH, "//span[text()='Delete']")
    delete_button = (By.XPATH, "//span[text()='Delete']")
    #8 for folder multi selecting
    root_project_button = (By.XPATH, "/html/body/div[8]/div/div/div[2]/nav/ol/li[1]/div/a")
    multiselect_all_folder_button = (By.XPATH, "//input[@data-action='change->multifiles-manager#selectAll']")
    multiselect_download_button = (By.XPATH, "/html/body/div[7]/div/div/div[2]/div/div/div[1]/div[2]")
    confirm_multi_download_button = (By.XPATH, "//span[contains(text(), 'Download Files')]")
    multiselect_folder_button = (By.XPATH, "//input[@type='checkbox' and @data-multifiles-manager-file-name-param='QA_Folder']")
    multiselect_folder_button1 = (By.XPATH, "//input[@type='checkbox' and @data-multifiles-manager-file-name-param='QA_Folder1']")
    multiselect_folder_button2 = (By.XPATH, "//input[@type='checkbox' and @data-multifiles-manager-file-name-param='QA_Folder2']")
    multiselect_folder_button3 = (By.XPATH, "//input[@type='checkbox' and @data-multifiles-manager-file-name-param='QA_Folder3']")
    multiselect_folder_button4 = (By.XPATH, "//input[@type='checkbox' and @data-multifiles-manager-file-name-param='QA_Folder4']")
    multiselect_delete_button = (By.XPATH, "/html/body/div[7]/div/div/div[2]/div/div/div[1]/form/button")
    multiselect_move_button = (By.XPATH, "/html/body/div[7]/div/div/div[2]/div/div/div[1]/div[1]")
    #9 for folder moving
    folder_settings_button_1 = (By.XPATH, "//table/tbody/tr[4]//button[@id='file-setting-btn']")
    folder_settings_button_2 = (By.XPATH, "/html/body/div[7]/div/div/turbo-frame/div[1]/div/table/tbody/tr/td[2]/div/div/button")
    move_folder_button = (By.XPATH, "/html/body/div[7]/div/div/turbo-frame/div[1]/div/table/tbody/tr/td[2]/div/div/ul/li[2]/button")
    project_select_dropdown = (By.ID, "input_file_record_id")
    Tektome_button = (By.XPATH, "//*[@id='top-page-link']")
    QA2_project_button = (By.XPATH, "//div[text()='QA_Upload2']")
    confirm_move_button = (By.XPATH, "//input[@type='submit' and @value='Move']")
    confirm_move_button_2 = (By.XPATH, "//div[@data-action='click->multifiles-manager#bulkMove' and contains(text(), 'Move')]")
    #10 for multi file selecting 
    multiselect_move_button_2 = (By.XPATH,"/html/body/div[8]/div/div/div[2]/div/div/div[1]/div[1]")
    multiselect_file_button1 = (By.XPATH, "//input[@type='checkbox' and @data-multifiles-manager-file-name-param='pdf.pdf']")
    multiselect_file_button2 = (By.XPATH, "//input[@type='checkbox' and @data-multifiles-manager-file-name-param='xlsx.xlsx']")

    #folder creating
    @allure.step("Create folder with name: {folder_name}")
    def create_folder(self, folder_name):
        self.click(self.add_folder_button)
        self.send_keys(self.folder_name_input, folder_name)
        self.click(self.create_folder_button)
        self.refresh_page

    @allure.step("Get all folder names")
    def get_all_folders(self):
        elements = self.find_elements(self.folder_names)
        return [element.text.strip() for element in elements if element.text.strip() and element.text.strip() != "Previous\n1\nNext"]

    @allure.step("Navigate to folder: {folder_name}")
    def navigate_to_folder(self, folder_name):
        folder_locator = (By.XPATH, f"//div[normalize-space(text())='{folder_name}']")
        self.wait_for_element_to_be_clickable(folder_locator )
        self.click(folder_locator)

    @allure.step("Confirm navigation to QA folder")
    def confirm_navigate_folder(self):
        self.wait_for_element(self.qa_folder)
        return True
    
#upload
    @allure.step("Click upload button")
    def click_upload_button(self):
        upload = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.upload_button))
        upload.click()
    
       # self.wait_for_element(self.upload_button)
       # self.click(self.upload_button)

    @allure.step("folder path to upload: {file_paths}")
    def add_filepath_to_upload(self, file_paths):
        try:
            os.path.abspath(os.path.join(os.path.dirname(__file__),
            file_paths)
        )
        except Exception as e:
            print(f"Error uploading files: {e}")


    @allure.step("Upload multiple files: {file_paths}")
    def upload_multiple_files(self, file_paths):
        try:
            self.send_keys(self.file_upload_input, "\n".join(file_paths))
        except Exception as e:
            print(f"Error uploading files: {e}")
    
    @allure.step("Upload multiple files: {file_paths}")
    def upload_multiple_files_withfailure(self, file_paths):
        try:
            self.send_keys(self.file_upload_input, "\n".join(file_paths))
            self.click(self.close_button)            
        except Exception as e:
            print(f"Error uploading files: {e}")

    @allure.step("Get uploaded files")
    def get_uploaded_files_in_failure(self):
        elements = self.find_elements(self.before_upload)
        return [element.text.strip() for element in elements if element.text.strip()]
    
    @allure.step("Get uploaded files")
    def get_uploaded_files(self):
        self.wait_for_element(self.uploaded_file)
        elements = self.find_elements(self.uploaded_file)
        return [element.text.strip() for element in elements if element.text.strip()]
    
    @allure.step("Get first uploaded files")
    def get_first_uploaded_files(self):
        self.wait_for_element(self.uploaded_file)
        element = self.find_element(self.uploaded_file)
        return [element.text.strip()]

    @allure.step("Click close button on upload modal")
    def click_close_button(self):
        self.wait_for_element_to_be_clickable(self.close_button)
        self.click(self.close_button)

#view test 
    @allure.step("Click grid view button")
    def click_grid_view_button(self):
        self.wait_for_element_to_be_clickable(self.grid_view_button)
        self.click(self.grid_view_button)

    @allure.step("Verify grid view is displayed")
    def verify_grid_view(self):
        self.wait_for_element(self.grid_block1)
        self.wait_for_element(self.grid_block2)
        self.wait_for_element(self.grid_block3)
        self.wait_for_element(self.grid_block4)
        return True
    @allure.step("Verify grid view is displayed for three files")
    def verify_grid_view_3_file(self):
        self.wait_for_element(self.grid_block1)
        self.wait_for_element(self.grid_block3)
        self.wait_for_element(self.grid_block4)
        return True
    
    @allure.step("Click preview button")
    def click_preview_button(self):
        self.wait_for_element_to_be_clickable(self.preview_button)
        self.click(self.preview_button)

    @allure.step("Verify file preview is displayed")
    def verify_preview(self):
        if self.enabled(self.preview_1) or self.enabled(self.preview_3) or self.enabled(self.preview_4):
          return True
        else:
         return False

    @allure.step("Exit file preview")
    def click_exit_preview_button(self):
        self.wait_for_element_to_be_clickable(self.exit_preview_button)
        self.click(self.exit_preview_button)

    @allure.step("Switch to list view")
    def click_list_view_button(self):
        self.wait_for_element_to_be_clickable(self.list_view_button)
        self.click(self.list_view_button)
        print("Switched to list view",self.enabled(self.list_view_button))

#rename test
    @allure.step("Get updated file element with name: {name}")
    def updated_file(self, name):
        return (By.XPATH, f"//div[@class='flex max-h-[65px] break-words overflow-scroll no-scrollbar' and text()='{name}']")

    @allure.step("Refresh the page")
    def refresh_page(self):
        self.driver.execute_script("location.reload()")

    @allure.step("Click on home button")
    def click_on_home_button(self):
        try:
            self.wait_for_element_to_be_clickable(self.project_home)
            self.click(self.project_home)
        except Exception as e:
            print(f"Error clicking home button: {e}")
    
    
    @allure.step("Click file settings button for rename")
    def click_file_settings_button_filelist_page(self):
        try:
            self.wait_for_element_to_be_clickable(self.file_settings_button_1)
            self.click(self.file_settings_button_1)
        except Exception as e:
            print(f"Error clicking file settings button: {e}")
    
    @allure.step("Click file settings button for move")
    def click_file_settings_button_move_filelist_page(self):
        try:
            self.wait_for_element_to_be_clickable(self.file_settings_button_3)
            self.click(self.file_settings_button_3)

        except Exception as e:
            print(f"Error clicking file settings button: {e}")


    @allure.step("Click rename button")
    def click_rename_button(self):
        self.wait_for_element(self.rename_button)
        self.click(self.rename_button)

    @allure.step("Rename file to: {new_name}")
    def rename_file(self, new_name):
        self.wait_for_element(self.file_name_input)
        input_element = self.find_element(self.file_name_input)
        input_element.clear()
        input_element.send_keys(new_name)
        self.click(self.update_button)
        print(self.success_msg)
    
    @allure.step("Verify success message")
    def verify_success_msg(self,act_msg):
        if self.get_text(self.success_msg) == act_msg:
            return True
        else:
            return False   

    @allure.step("Verify file name updated successfully")
    def verify_file_name_updated(self):
        self.wait_for_element(self.updated_name)
        return True

#move test
    @allure.step("Click move file button")
    def click_move_button(self):
        self.click(self.file_move_button)    

    @allure.step("Select folder for move")
    def click_folder_select_dropdown(self):
        move_target_folder = "  - QA_Folder_move"
        self.select_dropdown_by_visible_text(self.folder_select_dropdown,move_target_folder)

    @allure.step("Confirm move operation")
    def confirm_move(self):
        self.click(self.confirm_move_button)

    @allure.step("Check if move operation succeeded")
    def check_move_success(self):
        self.wait_for_element(self.move_target_folder_confirm)
        return True
    
    @allure.step("Check if move operation succeeded in file list")
    def check_move_success_in_filelist(self):
        self.wait_for_element(self.move_target_folder_confirm_1)
        return True
#download test
    @allure.step("Click file settings button for download")
    def click_file_settings_button(self):
        self.wait_for_element_to_be_clickable(self.file_settings_button_2 )
        self.click(self.file_settings_button_2)

    @allure.step("Click download button")
    def click_download_button(self):
        self.wait_for_element(self.download_button)
        self.click(self.download_button)

    @allure.step("Click delete button for file")
    def click_deleting_button(self):
        self.wait_for_element(self.delete_button)
        self.click(self.delete_button)  

    #delete test
    @allure.step("Dismiss delete confirmation alert")
    def dismiss_deleting_alert(self):
        print("Dismissing alert")
        self.driver.switch_to.alert.dismiss()

    @allure.step("Accept delete confirmation alert")
    def accept_deleting_alert(self):
        print("Accepting alert")
        self.accept_alert()

    @allure.step("Verify file is deleted")
    def verify_file_deleted(self):
        try:
            self.find_element(self.updated_name)
            return False  
        except Exception:  
            return True  

#multi select test
    @allure.step("Click root project button")
    def click_root_project_button(self):
        self.click(self.root_project_button)

    @allure.step("Click folder settings button 1")
    def click_folder_settings_button_1(self):
        self.wait_for_element(self.folder_settings_button_1)
        self.click(self.folder_settings_button_1)
    
    @allure.step("Click folder settings button 2")
    def click_folder_settings_button_2(self):
        self.wait_for_element(self.folder_settings_button_2)
        self.click(self.folder_settings_button_2)

    @allure.step("Click move folder button")
    def click_move_folder_button(self):
        self.wait_for_element(self.move_folder_button)
        self.click(self.move_folder_button)

    @allure.step("Select folder for move from dropdown")
    def click_folder_select_dropdown(self):
        move_target_folder = "  - QA_Folder_move"
        self.select_dropdown_by_visible_text(self.folder_select_dropdown,move_target_folder)

    @allure.step("Select folder for move from second dropdown")
    def click_folder_select_dropdown_2(self):
        move_target_folder = "  - Automation_folder"
        self.select_dropdown_by_visible_text(self.folder_select_dropdown_2,move_target_folder)
    
    @allure.step("Select project for move")
    def click_project_select_dropdown(self):
        move_target_project = "QA_Upload2"
        self.select_dropdown_by_visible_text(self.project_select_dropdown,move_target_project)
            
    @allure.step("Confirm move operation")
    def confirm_move(self):
        self.wait_for_element(self.confirm_move_button)
        self.click(self.confirm_move_button)

    @allure.step("Check if move operation succeeded")
    def check_move_success(self):
        self.wait_for_element(self.move_target_folder_confirm)
        return True

    @allure.step("Click multiselect all folder button")
    def click_multiselect_all_folder_button(self):
        self.click(self.multiselect_all_folder_button)
    
    @allure.step("Click multiselect download button")
    def click_multiselect_download_button(self):
        self.click(self.multiselect_download_button)

    @allure.step("Confirm multi-download operation")
    def confirm_multi_download(self):
        self.click(self.confirm_multi_download_button)

    @allure.step("Select folder button 1 for multiselect")
    def click_multiselect_folder_button1(self):
        self.click(self.multiselect_folder_button1)

    @allure.step("Select folder button 2 for multiselect")
    def click_multiselect_folder_button2(self):
        self.click(self.multiselect_folder_button2)

    @allure.step("Click delete button for multiselect folders")
    def click_multiselect_delete_button(self):
        self.click(self.multiselect_delete_button)

    @allure.step("Verify selected folders are deleted")
    def verify_folder_deleted(self):
        all_folders = self.get_all_folders()
        return "QA_Folder1" not in all_folders and "QA_Folder2" not in all_folders

#folder move test   
    @allure.step("Select folder button 3 for multiselect")
    def click_multiselect_folder_button3(self):
        self.click(self.multiselect_folder_button3)

    @allure.step("Select folder button for multiselect")
    def click_multiselect_folder_button(self):
        self.click(self.multiselect_folder_button)    
    
    @allure.step("Select folder button 4 for multiselect")
    def click_multiselect_folder_button4(self):
        self.click(self.multiselect_folder_button4)

    @allure.step("Click move button for multiselect folders")
    def click_multiselect_move_button(self):
        self.click(self.multiselect_move_button)

    @allure.step("Click Tektome button to get project list")
    def click_tektome(self):
        self.click(self.Tektome_button)
        
    def click_QA2_project_button(self):
        self.click(self.QA2_project_button)

    @allure.step("Check if folder multi-move operation succeeded")
    def check_multi_move_success(self):
        all_folders = self.get_all_folders()
        expected_items = { "QA_Folder", "QA_Folder3", "QA_Folder4","jpg1.jpg"}
        return expected_items.issubset(set(all_folders))
    
    @allure.step("Check if file multi-move operation succeeded")
    def check_file_multi_move_success(self):
        all_folders = self.get_all_folders()
        expected_items = { "QA_Folder_move", "pdf.pdf", "xlsx.xlsx","tif.tif"}
        return expected_items.issubset(set(all_folders))
    
    @allure.step("Confirm second move operation")
    def confirm_move_2(self):
        self.click(self.confirm_move_button_2)

    @allure.step("Check if move operation succeeded")
    def check_project_move_success(self):
        self.wait_for_element(self.move_target_project_confirm)
        return True

#multi file select test
    @allure.step("Select file button 1 for multiselect")
    def click_multiselect_file_button1(self):
        self.click(self.multiselect_file_button1)

    @allure.step("Click move button for multiselect folders2")
    def click_multiselect_move_button_2(self):
        self.click(self.multiselect_move_button_2)

    @allure.step("Select file button 2 for multiselect")
    def click_multiselect_file_button2(self):
        self.click(self.multiselect_file_button2)

    @allure.step("Verify files are selected")
    def verify_file_selected(self):
        return True

    @allure.step("Verify selected files are deleted")
    def verify_files_deleted(self):
        all_files = self.get_all_folders()
        return "pdf.pdf" not in all_files and "xlsx.xlsx" not in all_files
