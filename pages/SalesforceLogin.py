import time

from selenium.webdriver.common.by import By


class SalesforceLogin():
    def __init__(self, driver):
        self.driver = driver

    _username_input = "//span[contains(@class,'o-form-input')]//input[@type='text']"
    _next_button = "//input[@value='Next']"
    _password_input = "//span[contains(@class,'o-form-input')]//input[@type='password']"
    _verify_button = "//input[@type='submit']"
    _security_answer_method = "//div[@data-se='security_question']//a"

    def open_page(self):
        self.driver.get("https://biotheranostics--lisqa.sandbox.lightning.force.com/lightning/n/BTX_Home")

    def getUsernameField(self):
        return self.driver.find_element(By.XPATH, self._username_input)

    def getPasswordField(self):
        return self.driver.find_element(By.XPATH, self._password_input)

    def getNextButton(self):
        return self.driver.find_element(By.XPATH,self._next_button)

    def getVerifyButton(self):
        return self.driver.find_element(By.XPATH,self._verify_button)

    def getSecurityMethod(self):
        return self.driver.find_element(By.XPATH,self._security_answer_method)

    def enterUsername(self, username):
        self.getUsernameField().click()
        self.getUsernameField().send_keys(username)

    def ClickNextButton(self):
        self.getNextButton().click()

    def enterPassword(self, password):
            self.getPasswordField().click()
            self.getPasswordField().send_keys(password)

    def enterSecurityAnswer(self,answer):
        self.getPasswordField().click()
        self.getPasswordField().send_keys(answer)

    def ClickVerifyButton(self):
            self.getVerifyButton().click()

    def ChooseSecurityMethod(self):
        self.getSecurityMethod().click()

    def login(self,username, password, answer):
        self.enterUsername(username)
        self.ClickNextButton()
        time.sleep(5)
        self.enterPassword(password)
        self.ClickVerifyButton()
        time.sleep(5)
       # self.ChooseSecurityMethod()
        #time.sleep(3)
        self.enterSecurityAnswer(answer)
        self.ClickVerifyButton()


