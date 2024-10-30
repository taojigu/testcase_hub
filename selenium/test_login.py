from time import sleep
from selenium.webdriver.common.by import By
from config.saucedemo import Saucedemo
from util.url_util import compare_urls


def find_element_by_id(web_driver, element_id):
    element = web_driver.find_element(By.ID, element_id)
    assert element.is_displayed()
    return element


class TestSauceDemoLogin:

    @classmethod
    def setup_class(cls):
        cls.user_name_id = 'user-name'
        cls.password_id = 'password'
        cls.login_button_id = 'login-button'
        cls.error_message = "Epic sadface: Username and password do not match any user in this service"

    def test_valid_login_saucedemo(self,web_driver):
        """
        Test case ID: TC_Saucedemo_LOGIN_01
        Test valid login of saucedemo
        """

        url = Saucedemo.saucedemo_login_url()
        web_driver.get(url)
        user_name = web_driver.find_element(By.ID, self.user_name_id)
        assert user_name.is_displayed()
        user_name.clear()
        user_name.send_keys(Saucedemo.standard_user_name())
        password = web_driver.find_element(By.ID,self.password_id)
        assert password.is_displayed()
        password.clear()
        password.send_keys(Saucedemo.password())
        login_button= web_driver.find_element(By.ID,self.login_button_id)
        assert login_button.is_displayed()
        login_button.click()
        sleep(5)
        assert compare_urls(web_driver.current_url,Saucedemo.inventory_page_url())
        pass

    def test_unregister_user_login(self,web_driver):
        """
        TestCase ID: TC_Saucedemo_LOGIN_02
        Test Case 2: Verify login with unregistered username
        """
        web_driver.get(Saucedemo.saucedemo_login_url())
        user_name = find_element_by_id(web_driver,self.user_name_id)
        user_name.clear()
        user_name.send_keys(Saucedemo.unregister_user_name())
        password = find_element_by_id(web_driver,self.password_id)
        password.clear()
        password.send_keys(Saucedemo.password())
        login_button = find_element_by_id(web_driver,self.login_button_id)
        login_button.click()
        sleep(1)

        error_button = web_driver.find_element(By.XPATH,'//button[@class="error-button" and @data-test="error-button"]')
        assert error_button.is_displayed()
        container = web_driver.find_element(By.XPATH, '//h3[@data-test="error"]')
        err_msg = container.text
        assert err_msg == self.error_message