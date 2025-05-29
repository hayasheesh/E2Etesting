import threading

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class InitDriver:

    driver = None

    def __init__(self):
        self.session_id = threading.local()
        self.session_browser = threading.local()
        self.timeout_sec = 20

    @classmethod
    def init_driver(cls):
        if cls.driver is None:
            cls.driver = InitDriver()
        return cls.driver

    def set_driver(self, browser):
        if browser == "chrome":
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        elif browser == "chrome-headless":
            options = ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--start-maximized")
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        elif browser == "edge":
            options = EdgeOptions()
            self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        else:
            print("specify a valid webdriver")
        self.wait = WebDriverWait(self.driver, self.timeout_sec)
        return self.driver

    def get_web_driver(self):
        return self.driver

    def get_session_id(self):
        return self.session_id.value

    def get_session_browser(self):
        return self.session_browser.value
    
    def open_url(self, url):
        self.driver.get(url)

    def web_quit(self):
        if self.driver is not None:
            self.driver.quit()
        
