from selenium.webdriver.common.by import By


# page_url = https://www.hudl.com/register/signup
class HudlRegisterSignupPage(object):
    def __init__(self, driver):
        self.driver = driver

        self.headline_request_free_demo = (By.XPATH, "//h1")

    @property
    def get_headline_request_free_demo(self):
        return self.driver.find_element(*self.headline_request_free_demo)
