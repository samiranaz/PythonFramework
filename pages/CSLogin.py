from selenium.webdriver.common.by import By


class ClientServiceLogin():
    def __init__(self, driver):
        self.driver = driver

    _login_button = "//td[@id='topButtonRow']//input[@title='Login']"
    _logout_button = "//a[@class='action-link']"
    def open_page(self):
        self.driver.get("https://biotheranostics--lisqa.sandbox.lightning.force.com/lightning/setup/ManageUsers/page?address=%2F0051400000Bhyz4%3Fnoredirect%3D1%26isUserEntityOverride%3D1")

    def getLoginButton(self):
        return self.driver.find_element(By.XPATH,self._login_button)

    def getLogoutButton(self):
        return self.driver.find_element(By.XPATH, self._logout_button)

    def ClickLoginButton(self):
        self.getLoginButton().click()

    def ClickLogoutButton(self):
        self.getLogoutButton().click()

    def open_pslogin(self):
        self.driver.get("https://biotheranostics--lisqa.sandbox.lightning.force.com/lightning/setup/ManageUsers/page?address=%2F0055Y00000HYBVB%3Fnoredirect%3D1%26isUserEntityOverride%3D1")
