from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class PortalLogin(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _username_input = "//input[@placeholder='Username']"
    _password_input = "//input[@placeholder='Password']"
    _login_link = "//span[text()='Log in ']"

    def getUsernameField(self):
        return self.driver.find_element(By.XPATH,self._username_input)

    def getPasswordField(self):
        return self.driver.find_element(By.XPATH,self._password_input)

    def getLoginButton(self):
        return self.driver.find_element(By.XPATH,self._login_link)

    def enterUsername(self, username):
        self.getUsernameField().click()
        self.getUsernameField().send_keys(username)

    def enterPassword(self, password):
        self.getPasswordField().click()
        self.getPasswordField().send_keys(password)

    def ClickLoginButton(self):
        self.getLoginButton().click()

    def login(self,username, password):
        self.enterUsername(username)
        self.enterPassword(password)
        self.ClickLoginButton()

    def verifyLoginSuccessful(self):
        result= self.isElementPresent("//div[@class='welcomeMessage']","xpath")
        return result





