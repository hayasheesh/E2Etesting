from selenium.webdriver.common.by import By
from src.uitestsuite.pageobject.base_po import BasePage
import allure

class FileInitializationPage(BasePage):
     #4 for file renaming
    file_select_button_1 = (By.XPATH, "//i[@class='bx bx-dots-horizontal-rounded top-[1px]']")
    file_select_button_2 = (By.XPATH, "(//i[@class='bx bx-dots-horizontal-rounded top-[1px]'])[2]")

    #this file setting button_2 is for the in-folder page but the file setting button_1 is for the file list page.
    file_select_button = (By.XPATH, "input[data-multifiles-manager-file-name-param='jpg.jpg']")
    file_select1_button = (By.XPATH, "input[data-multifiles-manager-file-name-param='pdf.pdf']")
    retry_button = (By.XPATH, "//button[text()='Retry']")
    delete_button = (By.XPATH, "//button[text()='Delete']")
    download_button = (By.XPATH, "//span[text()='Download']")
    filter_user = (By.XPATH, "//input[@placeholder='Filter by Users']")
    select_user_name = (By.XPATH, "//span[text()='Banu Femina']")
    file_name_input= (By.XPATH, "//input[@id='input_file_file_name']")
    filter_started = (By.ID, "status_2")
    filter_queued = (By.ID, "status_1")
    filter_failed = (By.ID, "status_5")
    filter_completed = (By.ID, "status_6")
    file_name_input = (By.XPATH, "//input[@data-text='femina']")
    update_button = (By.XPATH, "//input[@value='Update']")
    updated_name = (By.XPATH, "//div[@class='td_inner max-h-[65px] break-words overflow-scroll no-scrollbar' and text()='tif.tif']")
    all_file_list = (By.XPATH, "//div[@class='td_inner max-h-[65px] break-words overflow-scroll no-scrollbar']")
    
    #5 for file moving  
    file_move_button = (By.XPATH, "//span[text()='Move']")
    processing_dashboard_link = (By.XPATH, "//span[text()='Processing Dashboard']")
    file_init_link = (By.XPATH, "//span[text()='File Initialization']")
    project_ok_button = (By.XPATH, "//input[@value='Create Project']")
    Tektome_button = (By.XPATH, "//*[@id='top-page-link']")
    processing_dashboard_button=(By.XPATH, "//span[text()='Processing Dashboard']")
    setting_button = (By.XPATH, "//a[@class='btn border-0 h-[70px] text-xl pr-6 px-4 dropdown-toggle dark:text-gray-100']")
    file_init_list = (By.XPATH, "//div[@class='td_inner max-h-[65px] break-words overflow-scroll no-scrollbar']")
    preview_button = By.CSS_SELECTOR, "button[data-input-files-preview-modal-opener='true']"
    preview_1 = (By.XPATH, "//img[contains(@src, 'jpg.jpg')]")
    preview_2 = (By.XPATH, "//img[contains(@src, 'tif.tif')]")
    preview_3 = (By.XPATH, "//div[text()='xlsx']")
    preview_4 = (By.XPATH, "//img[@alt='pdf.pdf']")
    preview_any = (By.XPATH, "//div[text()='pdf.pdf'] | //span[text()='xlsx.xlsx'] | //div[text()='jpg1.jpg'] | //div[text()='jpg.jpg'])]")
    exit_preview_button = (By.XPATH, "//*[@id='inputFilesPreviewModal']//button[contains(@class, 'close-btn')]")
    list_view_button = (By.CSS_SELECTOR, "a[data-turbo='true'][href*='list_mode=list']")
   
    @allure.step("Click on Setting Link")
    def click_on_settings(self):
        self.wait_for_element_to_be_clickable(self.setting_button)
        self.click(self.setting_button)
        self.wait_for_element_to_be_clickable(self.processing_dashboard_link)
        self.click(self.processing_dashboard_link)
        self.wait_for_element_to_be_clickable(self.file_init_link)
        self.click(self.file_init_link)
        return FileInitializationPage()
    
    @allure.step("Get the file initialization list")
    def get_list_of_file_init(self):
        elements = self.find_elements(self.file_init_list)
        return [element.text.strip() for element in elements if element.text.strip()]
    
    @allure.step("Click the tektome button")
    def click_tektome(self):
        self.click(self.Tektome_button)
        return FileInitializationPage()
    
    @allure.step("Select user from filter")
    def select_filter_by_user(self):
        self.wait_for_element_to_be_clickable(self.filter_user)
        self.click(self.filter_user)
        self.wait_for_element_to_be_clickable(self.select_user_name)
        self.click(self.select_user_name)
        return FileInitializationPage()

    @allure.step("Verify file is retrying")
    def verify_file_retry(self):
        try:
            self.find_element(self.updated_name)
            return False  
        except Exception:  
            return True
        
    @allure.step("Get uploaded files list in File Initialization page")
    def get_first_uploaded_files(self):
        element = self.find_element(self.all_file_list)
        return [element.text.strip()]
    #delete test
    @allure.step("Dismiss delete confirmation alert")
    def dismiss_deleting_alert(self):
        self.dismiss_alert()

    @allure.step("Accept delete confirmation alert")
    def accept_deleting_alert(self):
        self.accept_alert()

    @allure.step("Verify file is deleted")
    def verify_file_deleted(self):
        try:
            self.find_element(self.updated_name)
            return False  
        except Exception:  
            return True  
    @allure.step("Filter using status of file initialization started")
    def filter_by_file_init_started(self):
        self.wait_for_element_to_be_clickable(self.filter_started)
        self.click(self.filter_started)
        
    
    @allure.step("Filter using status of file initialization queued")
    def filter_by_file_init_queued(self):
        self.wait_for_element_to_be_clickable(self.filter_queued)
        self.click(self.filter_queued)
   
    @allure.step("Filter using status of file initialization Failed")
    def filter_by_file_init_failed(self):
        self.wait_for_element_to_be_clickable(self.filter_failed)
        self.click(self.filter_failed)

    @allure.step("Filter using status of file initialization Completed")
    def filter_by_file_init_completed(self):
        self.wait_for_element_to_be_clickable(self.filter_completed)
        self.click(self.filter_completed)

    @allure.step("verify retry from the file initialization list for failed files")
    def retry_failed_files(self):
        self.wait_for_element_to_be_clickable(self.file_select_button_1)
        self.click(self.file_select_button_1)
        self.wait_for_element_to_be_clickable(self.retry_button)
        self.click(self.retry_button)
    
    @allure.step("Refresh the webpage")  
    def refresh_webpage(self):
        self.driver.refresh()
        
    @allure.step("verify download from the file initialization list for failed files")
    def download_failed_files(self):
        self.wait_for_element_to_be_clickable(self.file_select_button_2)
        self.click(self.file_select_button_2)
        self.wait_for_element_to_be_clickable(self.download_button)
        self.click(self.download_button)
      
    @allure.step("verify delete from the file initialization list for failed files")
    def delete_failed_files(self):
        self.wait_for_element_to_be_clickable(self.file_select_button_2)
        self.click(self.file_select_button_2)
        self.wait_for_element_to_be_clickable(self.delete_button)
        self.click(self.delete_button)
      
    @allure.step("verify preview in file initialization list")
    def preview_files_in_file_init(self):
        self.click(self.Tektome_button)
        return FileInitializationPage()
    
    @allure.step("Click preview button")
    def click_preview_button(self):
        self.click(self.preview_button)

    @allure.step("Verify file preview is displayed")
    def verify_preview(self):
        self.wait_for_element(self.exit_preview_button)
        return True

    @allure.step("Exit file preview")
    def click_exit_preview_button(self):
        self.click(self.exit_preview_button)