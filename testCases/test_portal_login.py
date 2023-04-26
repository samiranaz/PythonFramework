import time
import unittest
from selenium.webdriver.chrome.service import Service as Service
from selenium import webdriver
from pages.PhysicianPortalLogin import PortalLogin
from pages.UnsubmittedTests import UnsubmittedTestPage
from pages.HomePage import Homepage
from pages.SubmitRequestPage import SubmitRequestPage
from pages.OrderSubmitted import OrderSubmitted
from pages.SalesforceLogin import SalesforceLogin
from pages.CSLogin import ClientServiceLogin
from pages.SalesforceHome import SalesforceHomePage
from pages.ActivityPage import Activities
from pages.PatientServices import PatientService
import pytest


class PortalTestLogIn(unittest.TestCase):
    baseURL = "https://biotheranostics--lisqa.sandbox.my.site.com/s/"
    chromeservice = Service(executable_path="")
    driver = webdriver.Chrome(service=chromeservice)
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseURL)
    lp = PortalLogin(driver)
    ut = UnsubmittedTestPage(driver)
    hp = Homepage(driver)
    str = SubmitRequestPage(driver)
    os = OrderSubmitted(driver)
    sl = SalesforceLogin(driver)
    cs = ClientServiceLogin(driver)
    sh = SalesforceHomePage(driver)
    ac = Activities(driver)
    ps = PatientService(driver)

    @pytest.mark.run(order=1)
    def test_valid_login(self):

        self.lp.login("pavani.uppala@technossus.com.lis", "Spivulet@123456")
        result = self.lp.verifyLoginSuccessful()
        assert result == True


    @pytest.mark.run(order=2)
    def test_opening_unsubmittedrequest(self):
        self.hp.clickUnsubmittedRequestsButton()
        self.ut.chooseCTIDType()
        self.ut.ChooseOrderbyPatient()


    @pytest.mark.run(order=3)
    def test_submitting_testrequest(self):
        self.str.submitTestRequest()
        self.os.FetchOrderID()
        time.sleep(15)

    @pytest.mark.run(order=4)
    def test_salesforce_login(self):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.sl.open_page()
        self.driver.implicitly_wait(5)
        self.sl.login("sonu.raj", "$pivulet2023", "tabu")
        self.driver.switch_to.window(self.driver.window_handles[1])


    @pytest.mark.run(order=5)
    def test_loginas_CS(self):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[2])
        self.cs.open_page()
        time.sleep(3)
        self.cs.ClickLoginButton()
        time.sleep(5)

    @pytest.mark.run(order=6)
    def test_complete_CSReview(self):
         self.sh.SearchOrder(self.os.orderid)
         self.sh.ClickCheckboxes()
         self.sh.PopulatePathologistInformation()
         self.ac.NavigateToActivities()
         self.ac.Markallactivities()
         self.ac.MarkStatusasComplete()
         self.sh.CreatePS()
         self.cs.ClickLogoutButton()

    @pytest.mark.run(order=7)
    def test_loginas_PS(self):
        self.cs.open_pslogin()
        time.sleep(3)
        self.cs.ClickLoginButton()
        time.sleep(5)

    @pytest.mark.run(order=7)
    def test_complete_PSReview(self):
        self.sh.SearchOrder(self.os.orderid)
        self.sh.NavigateToBilling()
        self.sh.PopulatePayorID()
        self.ps.CompletePS()
        self.ps.BackToOrder()
        self.ac.NavigateToActivities()
        self.ac.Markallactivities()
        self.ac.MarkStatusasComplete()
        self.cs.ClickLogoutButton()


















