import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By



class SubmitRequestPage():
    def __init__(self, driver):
        self.driver = driver

    _orderstatuslistelement_ = "//ul[@aria-label='Path Options']//li"
    _statusmessage_ = "//div[@class='cCustomTestRequestRecordPage']//div//h1"
    _systemInformationElement_ = "//span[@title='System Information']"
    _checkBoxListElement_ = "//div[@data-aura-class='cSubmitTestRequest'][2]//label[@class='slds-checkbox__label']"
    _submitTestRequestButton_ = "//button[text()='Submit Test Request']"

    def getSystemInformationElement(self):
        return self.driver.find_element(By.XPATH,self._systemInformationElement_)

    def getCheckBoxListElement(self):
        return self.driver.find_elements(By.XPATH,self._checkBoxListElement_)

    def getSubmitTestRequestButton(self):
        return self.driver.find_element(By.XPATH, self._submitTestRequestButton_)

    def ClickSubmitTestRequestButton(self):
        self.getSubmitTestRequestButton().click()

    def selectCheckBoxes(self):
        selectcheckboxes = self.getCheckBoxListElement()
        for element in selectcheckboxes:
             element.click()

    def scrollToElement(self):
        actions = ActionChains(self.driver)
        actions.scroll_to_element(self.getSystemInformationElement())
        actions.perform()

    def submitTestRequest(self):
        time.sleep(5)
        self.scrollToElement()
        time.sleep(3)
        self.selectCheckBoxes()
        time.sleep(3)
        self.ClickSubmitTestRequestButton()



