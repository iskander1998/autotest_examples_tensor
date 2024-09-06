import time
from pages.sbis_homepage import Sbis_Homepage
from pages.sbis_downloads import Sbis_Downloads

def test_third_scenario(driver):
    sbis_homepage = Sbis_Homepage(driver)
    sbis_homepage.open()
    sbis_homepage.click_downloads()
    time.sleep(3)
    sbis_downloads = Sbis_Downloads(driver)
    sbis_downloads.windows_slot_click()
    sbis_downloads.download_web_setup_plugin_click()
    time.sleep(30) # Время загрузки, можно регулировать
    sbis_downloads.download_file_version_check()