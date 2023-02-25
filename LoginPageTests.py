import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from PageObject.HudlHomePage import HudlHomePage
from PageObject.HudlLoginPage import HudlLoginPage
from PageObject.HudlPage import HudlPage
from PageObject.HudlLoginHelpPage import HudlLoginHelpPage
from PageObject.HudlRegisterSignupPage import HudlRegisterSignupPage


class TestWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
        self.driver.maximize_window()
        self.driver.get("https://www.hudl.com/")
        hudl_page = HudlPage(self.driver)
        hudl_page.get_link_login.click()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_successfully_login(self):
        hudl_login_page = HudlLoginPage(self.driver)
        hudl_login_page.login(email="Andre.pienaar@hotmail.co.uk", password="Hudl@P@22w0rd")

        hudl_home_page = HudlHomePage(self.driver)
        input_search_locator, input_search_value = hudl_home_page.input_search
        input_search = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((input_search_locator, input_search_value))
        )
        assert input_search.is_displayed()

    def test_fail_login_without_input(self):
        hudl_login_page = HudlLoginPage(self.driver)
        hudl_login_page.login(email="", password="")

        error_message_locator, error_message_value = hudl_login_page.error_message
        error_message = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((error_message_locator, error_message_value))
        )
        assert error_message.is_displayed()

    def test_fail_login_with_wrong_email(self):
        hudl_login_page = HudlLoginPage(self.driver)
        hudl_login_page.login(email="test@test,com", password="Hudl@P@22w0rd")

        error_message_locator, error_message_value = hudl_login_page.error_message
        error_message = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((error_message_locator, error_message_value))
        )
        assert error_message.is_displayed()

    def test_fail_login_with_wrong_password(self):
        hudl_login_page = HudlLoginPage(self.driver)
        hudl_login_page.login(email="Andre.pienaar@hotmail.co.uk", password="TestPassword")

        error_message_locator, error_message_value = hudl_login_page.error_message
        error_message = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((error_message_locator, error_message_value))
        )
        assert error_message.is_displayed()

    def test_need_help_link(self):
        hudl_login_page = HudlLoginPage(self.driver)
        hudl_login_page.get_link_need_help.click()

        hudl_login_help_page = HudlLoginHelpPage(self.driver)
        headline_login_help_locator, headline_login_help_value = hudl_login_help_page.headline_login_help
        headline_login_help = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((headline_login_help_locator, headline_login_help_value))
        )
        assert headline_login_help.is_displayed()

    def test_signup_link(self):
        hudl_login_page = HudlLoginPage(self.driver)
        hudl_login_page.get_link_signup.click()

        hudl_register_signup_page = HudlRegisterSignupPage(self.driver)
        headline_request_free_demo_locator, headline_request_free_demo_value = \
            hudl_register_signup_page.headline_request_free_demo

        headline_request_free_demo = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((headline_request_free_demo_locator, headline_request_free_demo_value))
        )
        assert headline_request_free_demo.is_displayed()
        
if __name__ == '__main__':
    unittest.main()
    
