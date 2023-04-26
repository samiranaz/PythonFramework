import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class PatientService():
    def __init__(self, driver):
        self.driver = driver

    _fulfillment_metrics = "(//span[text()='Fulfillment Metrics'])[2]"
    _followup_date = "//input[@name='Follow_Up_Date__c']"
    _completed_date = "//input[@name='Completed_Date__c']"
    _save_button = "//button[@name='SaveEdit']"
    _cancel_button = "//button[@name='CancelEdit']"
    _activity_tab = "(//a[@data-label = 'Activity'])[2]"
    _proceed_button = "(//a[@title = 'Proceed'])[2]"
    _mark_currentstatus = "(//button//span[text()='Mark as Current Status'])[2]"
    _edit_button = "(//button[@title='Edit Follow Up Date'])[2]"
    _orders_element = "(//span[@id='window'][contains(text(),'Orders')])[2]"
    _orderid_element = "(//table[@aria-label='Orders']//a[contains(@title,'ORD')])[2]"


    def getFulfillmentMetrics(self):
       return self.driver.find_element(By.XPATH, self._fulfillment_metrics)

    def getFollowUpDate(self):
        return self.driver.find_element(By.XPATH, self._followup_date)

    def getCompletedDate(self):
        return self.driver.find_element(By.XPATH, self._completed_date)

    def getSaveButton(self):
        return self.driver.find_element(By.XPATH, self._save_button)

    def getEditButton(self):
        return self.driver.find_element(By.XPATH, self._edit_button)

    def getActivityTab(self):
        return self.driver.find_element(By.XPATH, self._activity_tab)

    def getProceedButton(self):
        return self.driver.find_element(By.XPATH, self._proceed_button)

    def getMarkCurrentStatus(self):
        return self.driver.find_element(By.XPATH, self._mark_currentstatus)

    def getOrderElement(self):
        return self.driver.find_element(By.XPATH, self._orders_element)

    def getOrderID(self):
        return self.driver.find_element(By.XPATH, self._orderid_element)

    def scrollToElement(self, element):
        actions = ActionChains(self.driver)
        actions.scroll_to_element(element)
        actions.perform()

    def CompletePS(self):
        self.scrollToElement(self.getFulfillmentMetrics())
        self.getEditButton().click()
        self.getFollowUpDate().send_keys("4/21/2023")
        self.getCompletedDate().click().send_keys("4/21/2023")
        self.getSaveButton().click()
        time.sleep(3)
        self.scrollToElement(self.getActivityTab())
        self.getProceedButton().click()
        self.getMarkCurrentStatus().click()
        time.sleep(5)

    def BackToOrder(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.getOrderElement()).perform()
        actions.move_to_element(self.getOrderID()).click().perform()
        time.sleep(10)



