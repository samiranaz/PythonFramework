from selenium.webdriver.common.by import By


class Homepage():
    def __init__(self, driver):
        self.driver = driver

    _ordertypelist_ = "//button[contains(@class,'slds-truncate')]"
    _menuitemslist_ = "//ul[@class='slds-tabs_default__nav']//li"
    _unsubmitted_requests = "//li[@role='presentation']//a[text()='Unsubmitted Requests']"

    def getUnsubmittedRequests(self):
        return self.driver.find_element(By.XPATH,self._unsubmitted_requests)

    def clickUnsubmittedRequestsButton(self):
        self.getUnsubmittedRequests().click()