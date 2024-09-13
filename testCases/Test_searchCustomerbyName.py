import pytest

from PageObjects.LoginPage import LoginPage
from utilities.readproperties import Readconfig
from PageObjects.AddCustomer import AddCustomer
from utilities.customlogger import LogGen
from PageObjects.SearchCustomer import SearchCustomer
import time

class Test_005_SearchcustmerByname:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getPassword()
    password = Readconfig.getPassword()

    logger = LogGen.loggen()
    @pytest.mark.regression
    def test_searchCustomerbyname(self, setup):
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
        self.logger.info("****** starting search customer by name**********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.ClickonCustomersMenu()
        self.addcust.Clickoncustomersmenuitem()

        searchcust = SearchCustomer(self.driver)

        searchcust.setfirstname("Victoria")
        searchcust.setlastname("Terces")
        searchcust.clicksearch()

        time.sleep(5)
        status = searchcust.searchcustomerbyname("Victoria Terces")
        assert True == status



