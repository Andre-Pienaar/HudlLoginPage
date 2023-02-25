from selenium.webdriver.common.by import By


# page_url = https://www.hudl.com/login
class HudlLoginPage(object):
    def __init__(self, driver):
        self.driver = driver

        # Page locator
        self.link_signup = (By.XPATH, "//a[@href='/register/signup']")
        self.input_email = (By.XPATH, "//input[@data-qa-id='email-input']")
        self.input_password = (By.XPATH, "//input[@data-qa-id='password-input']")
        self.button_login = (By.XPATH, "//button[@data-qa-id='login-btn']")
        self.error_message = (By.XPATH, "//div[contains(@class, 'nner')]")
        self.link_need_help = (By.XPATH, "//a[@data-qa-id='need-help-link']")

    @property
    def get_link_signup(self):
        return self.driver.find_element(*self.link_signup)

    @property
    def get_email_input(self):
        return self.driver.find_element(*self.input_email)

    @property
    def get_password_input(self):
        return self.driver.find_element(*self.input_password)

    @property
    def get_login_button(self):
        return self.driver.find_element(*self.button_login)

    @property
    def get_error_message(self):
        return self.driver.find_element(*self.error_message)

    @property
    def get_link_need_help(self):
        return self.driver.find_element(*self.link_need_help)

    def login(self, email, password):
        self.get_email_input.send_keys(email)
        self.get_password_input.send_keys(password)
        self.get_login_button.click()
