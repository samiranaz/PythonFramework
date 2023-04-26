import time

from selenium.webdriver.common.by import By


class UnsubmittedTestPage():
    def __init__(self, driver):
        self.driver = driver

    _unsubmittedrequestpatientlistelement_ = "//div[@class='slds-p-bottom_small']//table//tbody//tr//th[@data-label='Patient Name']//a"
    _testtype_button_ = "//span[text()='Test Type']"
    _menuitemslistelement_ = "//div[@class='slds-p-bottom_small']//table//tr//th[contains(@class,'slds-is-sortable')]"

    def getTestTypeButton(self):
        return self.driver.find_element(By.XPATH, self._testtype_button_)

    def clickTestTypeButton(self):
        self.getTestTypeButton().click()

    def getPatientListElement(self):
        return self.driver.find_elements(By.XPATH, self._unsubmittedrequestpatientlistelement_)

    def ChooseOrderbyPatient(self):
        patientname = self.getPatientListElement()
        patientname[0].click()


    def chooseCTIDType(self):
        time.sleep(5)
        self.clickTestTypeButton()
        time.sleep(3)
        self.clickTestTypeButton()
        time.sleep(9)