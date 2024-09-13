import pytest
from selenium.webdriver.common.by import By

from PageObjects.LoginPage import LoginPage
from utilities.readproperties import Readconfig
from PageObjects.AddCustomer import AddCustomer
from utilities.customlogger import LogGen
from PageObjects.SearchCustomer import SearchCustomer
import time

class Test_004_SearchcustomerbyEmail:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUsermail()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_searchcustomer(self, setup):
        self.logger.info("******* Test_003_addcustomer *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        # If CAPTCHA apprs, wait for manual completion
        # input("Complete the CAPTCHA and press Enter to continue...")
        self.lp = LoginPage(self.driver)
        self.lp.SetUserName(self.username)
        self.lp.SetPasswaord(self.password)
        self.lp.clicklogin()
        # time.sleep(3)
        # If CAPTCHA appears, wait for manual completion
        # input("Complete the CAPTCHA and press Enter to continue...")
        self.logger.info("*******Login successful************")
        self.logger.info("****** starting Add new customer test**********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.ClickonCustomersMenu()
        self.addcust.Clickoncustomersmenuitem()

        searchcust = SearchCustomer(self.driver)

        searchcust.setEmail("asfffff@gmail.com")
        searchcust.clicksearch()

        time.sleep(5)
        status = searchcust.customersearchemail("asfffff@gmail.com")
        assert True == status





