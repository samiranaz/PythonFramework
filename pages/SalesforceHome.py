
import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By


from pages import OrderSubmitted




class SalesforceHomePage():
    def __init__(self, driver):
        self.driver = driver


    _search_box = "//button[@aria-label='Search']"
    _searchbox_input = "//input[@placeholder='Search...']"
    _order_id_element = "(//span[contains(@class,'slds-grid')]//a[contains(@title,'ORD')])[1]"
    _insurancecard_checkboxelement = "//input[@name='Insurance_Card_Received__c']"
    _pathologyreport_checkbox_element = "//input[@name='Pathology_Report_Received__c']"
    _requiredfieldandforms_element = "//span[@title='Required Fields and Forms']"
    _pathologyfacility_information = "//span[@title='Pathology Facility Information']"
    _pathologypractice_selectelement = "//flexipage-field[@data-field-id='RecordPathology_Practice_cField1']//div//input"
    _pathologypractice_listelement= "//flexipage-field[@data-field-id='RecordPathology_Practice_cField1']//div//ul//li"
    _pathologist_nameelement = "//input[@name='Pathologist_Name__c']"
    _edit_pathologist_button = "//button[@title='Edit Pathologist']"
    _editforms_button ="//button[@title='Edit Insurance Card Received']"
    _save_button= "//button[@name='SaveEdit']"
    _cancel_button = "//button[@name='CancelEdit']"
    _dropdown_menu = "//div//div[@role='menu']//slot//runtime_platform_actions-action-renderer"
    _dropdown_button = "//div[contains(@class,'actionsContainer')]//div//lightning-button-menu[contains(@class,'slds-dropdown-trigger_click')]//button"
    _billing_menu = "(//a[@data-label='Billing'])[3]"
    _insurance_payor_element = "(//span[@title='Insurance Payor'])[3]"
    _edit_payorid = "//button[@title='Edit Payor ID']"
    _enter_payorid = "(//input[@placeholder='Search Insurance Payors...'])[3]"
    _payoridlist_element = "//div//ul//li[@class='slds-listbox__item']"
    _ps_id = "//span[@id='window']"


    def getSearchBox(self):
        return self.driver.find_element(By.XPATH, self._search_box)

    def getSearchBoxInput(self):
        return self.driver.find_element(By.XPATH, self._searchbox_input)

    def getOrderID(self):
        return self.driver.find_element(By.XPATH, self._order_id_element)

    def getEditFormButton(self):
        return self.driver.find_element(By.XPATH, self._editforms_button)

    def getEditPathologistButton(self):
        return self.driver.find_element(By.XPATH, self._edit_pathologist_button)

    def getSaveButton(self):
        return self.driver.find_element(By.XPATH, self._save_button)

    def getCancelButton(self):
        return  self.driver.find_element(By.XPATH,self._cancel_button)

    def getRequiredFieldandFormElement(self):
        return self.driver.find_element(By.XPATH, self._requiredfieldandforms_element)

    def getInsuranceCardCheckbox(self):
        return self.driver.find_element(By.XPATH, self._insurancecard_checkboxelement)

    def getPathologyCardCheckbox(self):
        return self.driver.find_element(By.XPATH, self._pathologyreport_checkbox_element)

    def getPathologistNameElement(self):
        return self.driver.find_element(By.XPATH, self._pathologist_nameelement)

    def getPathologyFacilityElement(self):
        return self.driver.find_element(By.XPATH, self._pathologyfacility_information)


    def getPathologyPractice(self):
        return self.driver.find_element(By.XPATH, self._pathologypractice_selectelement)

    def getPathologyPracticeList(self):
        return self.driver.find_elements(By.XPATH, self._pathologypractice_listelement)

    def getDropDownButton(self):
        return self.driver.find_element(By.XPATH, self._dropdown_button)

    def getDropdownListElement(self):
        return self.driver.find_elements(By.XPATH, self._dropdown_menu)

    def getBillingMenu(self):
        return self.driver.find_element(By.XPATH, self._billing_menu)

    def getInsurancePayor(self):
        return self.driver.find_element(By.XPATH,self._insurance_payor_element)

    def getPayorIdEditButton(self):
        return self.driver.find_element(By.XPATH, self._edit_payorid)

    def getPayorIdList(self):
        return self.driver.find_elements(By.XPATH, self._payoridlist_element)

    def getPSId(self):
        return self.driver.find_element(By.XPATH, self._ps_id)



    def ClickSearchBox(self):
        self.getSearchBox().click()

    def ClickOrderID(self):
        self.getOrderID().click()

    def scrollToElement(self, element):
        actions = ActionChains(self.driver)
        actions.scroll_to_element(element)
        actions.perform()

    def SearchOrder(self,id):
        self.ClickSearchBox()
        time.sleep(3)
        self.getSearchBoxInput().send_keys(id, Keys.ENTER)
        time.sleep(3)
        self.ClickOrderID()

    def ClickCheckboxes(self):
        self.scrollToElement(self.getRequiredFieldandFormElement())
        self.getEditFormButton().click()
        self.getInsuranceCardCheckbox().click()
        self.getPathologyCardCheckbox().click()
        self.getSaveButton().click()

    def ChoosePathologyPractice(self):

        self.getPathologyPractice().click().send_keys("Smoke Test Pathology Group - Dallas")
        medicalpracticelist = self.getPathologyPracticeList()
        medicalpracticelist.click()

    def PopulatePathologistInformation(self):
        self.scrollToElement(self.getPathologyFacilityElement())
        self.getEditPathologistButton().click()
        self.getPathologistNameElement().click().send_keys("Pavani")
        self.ChoosePathologyPractice()
        self.getSaveButton().click()

    def CreatePS(self):

        self.getDropDownButton().click()
        actions = self.getDropdownListElement()
        for action in actions:
            action[4].click()

    def NavigateToBilling(self):
        self.getBillingMenu().click()

    def PopulatePayorID(self):
        self.scrollToElement(self.getInsurancePayor())
        self.getPayorIdEditButton().click().send_keys("1st")
        id = self.getPayorIdList()
        for element in id:
            element[0].click()
        self.getSaveButton().click()
        time.sleep(5)
        self.getPSId().click()






















