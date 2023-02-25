from selenium.webdriver.common.by import By


# page_url = https://www.hudl.com/home
class HudlHomePage(object):
    def __init__(self, driver):
        self.driver = driver

        # Page locator
        self.input_search = (By.XPATH, "//input[@title='Search']")
        self.menu_team_switcher = (By.XPATH, "//div[contains(@data-qa-id, 'teamswitcher')]")
        self.item_user = (By.XPATH, "//div[@class='hui-globaluseritem']")

    @property
    def get_input_search(self):
        return self.driver.find_element(*self.input_search)

    @property
    def get_menu_team_switcher(self):
        return self.driver.find_element(*self.menu_team_switcher)

    @property
    def get_item_user(self):
        return self.driver.find_element(*self.item_user)
