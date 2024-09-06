import time
from pages.sbis_homepage import Sbis_Homepage
from pages.sbis_contacts import Sbis_Contacts

def test_second_scenario(driver):
    sbis_homepage = Sbis_Homepage(driver)
    sbis_homepage.open()
    sbis_homepage.click_contacts()
    sbis_contacts = Sbis_Contacts(driver)
    sbis_contacts.region_name_check('Республика Татарстан') # Введите свой регион
    sbis_contacts.offices_list_check()
    sbis_contacts.city_offices_check('Казань')
    sbis_contacts.region_name_click()
    time.sleep(3)
    sbis_contacts.change_region('Камчатский край') # Введите регион на какой переключиться
    time.sleep(3)
    sbis_contacts.region_name_check('Камчатский край')
    sbis_contacts.offices_list_check()
    sbis_contacts.city_offices_check('Петропавловск-Камчатский')
    sbis_contacts.url_kamchatka_check()
    sbis_contacts.website_title_kamchatka_check()