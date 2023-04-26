import time

from selenium.webdriver.common.by import By


class Activities():
    def __init__(self, driver):
        self.driver = driver

    _activity_tabelement = "//ul[@class='slds-tabs_default__nav']//li[@title='Activities']"
    _checkbox_element = "//div[contains(@id,'upcoming-activities-section')]//ul//li//label"
    _markstatus_element = "(//div[contains(@class,'PathAssistant')]//button//span[text()='Mark Status as Complete'])[2]"

    def getActivitiesElement(self):
        return self.driver.find_element(By.XPATH, self._activity_tabelement)

    def getMarkStatusElement(self):
        return self.driver.find_element(By.XPATH, self._markstatus_element)

    def NavigateToActivities(self):
        self.getActivitiesElement().click()
        time.sleep(3)

    def getActivitiesCheckbox(self):
        return self.driver.find_elements(By.XPATH, self._checkbox_element)

    def Markallactivities(self):
        activities = self.getActivitiesCheckbox()
        for activity in activities:
            activity.click()

    def MarkStatusasComplete(self):
        time.sleep(5)
        self.getMarkStatusElement().click()

