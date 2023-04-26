class AddingSpecimen():
    def __init__(self, driver):
        self.driver = driver

    _newspecimen_button = "//a[@title='New']"
    _dateofcollection_element = "//input[@name='Date_of_Collection__c']"
    _dateofreceiving_element = "//input[@name='Date_Received__c']"
    _externalspecimenid_element = "//input[@name='External_Specimen_ID__c']"
    _labactionselect_element = "//button[contains(@aria-label,'Lab Action')]"
    _labactiontype_element = "//button[contains(@aria-label,'Lab Action')]/parent::div/following-sibling::div/lightning-base-combobox-item/span/span[@class='slds-truncate']"
    _specimentypeselect_element = "//button[contains(@aria-label,'Specimen Type')]"
    _specimentype_element = "//button[contains(@aria-label,'Specimen Type')]/parent::div/following-sibling::div/lightning-base-combobox-item/span/span[@class='slds-truncate']"
    _cancel_button = "//button[@name='CancelEdit']"
    _save_button = "//button[@name='SaveEdit']"
    _saveandnew_button = "//button[@name='SaveAndNew']"

