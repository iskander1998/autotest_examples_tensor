import time
from pages.sbis_homepage import Sbis_Homepage
from pages.sbis_contacts import Sbis_Contacts
from pages.tensor_homepage import Tensor_Homepage
from pages.tensor_about import Tensor_About

def test_first_scenario(driver):
    sbis_homepage = Sbis_Homepage(driver)
    sbis_homepage.open()
    sbis_homepage.click_contacts()
    time.sleep(3)
    sbis_contacts = Sbis_Contacts(driver)
    sbis_contacts.click_tensor_image()
    time.sleep(3)
    tensor_homepage = Tensor_Homepage(driver)
    tensor_homepage.sila_text_check()
    tensor_homepage.about_click()
    tensor_homepage.about_page_check()
    tensor_about = Tensor_About(driver)
    tensor_about.comparison_picture_sizes_check()