from selenium.webdriver.common.by import By

class Tensor_Homepage:
    
    def __init__(self, driver):
        self.driver = driver
    def sila_text_check(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        sila_text = self.driver.find_element(By.XPATH, "//p[text()='Сила в людях']")
        assert sila_text.text == 'Сила в людях'
    def about_click(self):
        about_sila = self.driver.find_element(By.XPATH, "//a[@href='/about']")
        about_sila.click()
    def about_page_check(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.driver.current_url