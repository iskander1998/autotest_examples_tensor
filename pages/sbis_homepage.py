from selenium.webdriver.common.by import By

class Sbis_Homepage:
    def __init__(self, driver):
        self.driver = driver
    def open(self):
        self.driver.get('https://sbis.ru/')

    def click_contacts(self):
        contacts_header_menu = self.driver.find_element(By.XPATH, '//a[text()="Контакты"]')
        contacts_header_menu.click()
    
    def click_downloads(self):
        download_page = self.driver.find_element(By.XPATH, "//a[@href='/download']")
        download_page.click()