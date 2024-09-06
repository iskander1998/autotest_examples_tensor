from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest
import os




@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    prefs = {
        'download.default_directory': fr"{os.getcwd()}\downloads",
        "safebrowsing.enabled": True,
        "download.prompt_for_download": False
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.enable_downloads = True
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(options=chrome_options, service=service)
    driver.maximize_window()
    yield driver