from selenium.webdriver.common.by import By



# page_url = https://www.hudl.com/login/help#
class HudlLoginHelpPage(object):
    def __init__(self, driver):
        self.driver = driver

        self.headline_login_help = (By.XPATH, "//h2[@data-qa-id='login-help-headline']")

    @property
    def get_headline_login_help(self):
        return self.driver.find_element(*self.headline_login_help)
