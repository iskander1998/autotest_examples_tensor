from selenium.webdriver.common.by import By
import os

class Sbis_Downloads:
    def __init__(self, driver):
        self.driver = driver
    
    def windows_slot_click(self):
        windows_slot = self.driver.find_element(By.XPATH, "//span[text()='Windows']")
        windows_slot.click()
    
    def download_web_setup_plugin_click(self):
        download_click = self.driver.find_element(By.XPATH, "//a[@href='https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe']")
        download_click.click()

    def download_file_version_check(self):
        download_click = self.driver.find_element(By.XPATH, "//a[@href='https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe']")
        file = os.path.getsize(r'downloads\sbisplugin-setup-web.exe')
        file_size = (f"{file//1024/1024:.2f}")
        file_web_name = download_click.text
        file_web_version = (file_web_name.split())[-2]
        assert file_size == file_web_version