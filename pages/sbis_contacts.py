from selenium.webdriver.common.by import By

class Sbis_Contacts:
    def __init__(self, driver):
        self.driver = driver

    def click_tensor_image(self):
        image_tensor = self.driver.find_element(By.XPATH, '//img[@alt="Разработчик системы СБИС — компания «Тензор»"]')
        image_tensor.click()

    def region_name_check(self, region_name):
        web_region_name = self.driver.find_element(By.XPATH, "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']")
        assert web_region_name.text == region_name

    def region_name_click(self):
        web_region_name = self.driver.find_element(By.XPATH, "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']")
        web_region_name.click()

    def offices_list_check(self):
        office_list = self.driver.find_elements(By.XPATH, """//div[@class="controls-ListView__itemV-relative controls-ListView__itemV controls-ListView__item_default controls-ListView__item_contentWrapper js-controls-ListView__editingTarget  controls-ListView__itemV_cursor-pointer  controls-ListView__item_showActions js-controls-ListView__measurableContainer controls-ListView__item__unmarked_default controls-ListView__item_highlightOnHover controls-hover-background-default controls-Tree__item"]""")
        assert len(office_list) > 0

    def change_region(self, region):
        choosen_region = self.driver.find_element(By.XPATH, f"//span[@title='{region}']")
        choosen_region.click()
    
    def city_offices_check(self, city):
        offices_city = self.driver.find_element(By.XPATH, "//div[@id='city-id-2']")
        assert offices_city.text == f'{city}'
    def url_kamchatka_check(self):
        assert self.driver.current_url == 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'
    def website_title_kamchatka_check(self):
        assert self.driver.title == 'СБИС Контакты — Камчатский край'