from selenium.webdriver.common.by import By


# page_url = www.hudl.com
class HudlPage:
    def __init__(self, driver):
        self.driver = driver

        # Page locator
        self.link_login = (By.XPATH, "//a[@data-qa-id='login']")

    @property
    def get_link_login(self):
        return self.driver.find_element(*self.link_login)
