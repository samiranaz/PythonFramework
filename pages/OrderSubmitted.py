import time

from selenium.webdriver.common.by import By

class OrderSubmitted():
    def __init__(self, driver):
        self.driver = driver

    _orderidelement_ = "//span[@class= 'uiOutputText']"

    def getOrderIdElement(self):
        return self.driver.find_element(By.XPATH,self._orderidelement_)

    def FetchOrderID(self):
        time.sleep(10)
        self.orderid = self.getOrderIdElement().text
        return self.orderid







