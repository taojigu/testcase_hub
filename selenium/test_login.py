from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from config.saucedemo import Saucedemo
from util.url_util import compare_urls

"""
Test case ID: TC_LOGIN_01
Test valid login of saucedemo
"""
def test_valid_login_saucedemo(web_driver):
    #driver = chrome_driver
    url = Saucedemo.saucedemo_login_url()
    web_driver.get(url)
    user_name = web_driver.find_element(By.ID,'user-name')
    assert user_name.is_displayed()
    user_name.clear()
    user_name.send_keys(Saucedemo.standard_user_name())
    password = web_driver.find_element(By.ID,'password')
    assert password.is_displayed()
    password.clear()
    password.send_keys(Saucedemo.password())
    login_button= web_driver.find_element(By.ID,'login-button')
    assert login_button.is_displayed()
    login_button.click()
    sleep(5)
    assert compare_urls(web_driver.current_url,Saucedemo.inventory_page_url())
    pass

