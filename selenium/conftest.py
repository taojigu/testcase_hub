
import pytest
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='session')
def web_driver():
    driver_path="../resources/chromedriver-mac-x64/chromedriver"
    driver = webdriver.Chrome()
    #driver = webdriver.Chrome(driver_path)
    yield driver
    driver.quit()