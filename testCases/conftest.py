import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.fixture()
def setup():
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
    return driver

