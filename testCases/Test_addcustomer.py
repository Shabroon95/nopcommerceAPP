import pytest
from selenium.webdriver.common.by import By

from PageObjects.LoginPage import LoginPage
from utilities.readproperties import Readconfig
from PageObjects.AddCustomer import AddCustomer
from utilities.customlogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURL = Readconfig.getApplicationURL()
    username= Readconfig.getUsermail()
    password = Readconfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_addcustomer(self, setup):
        self.logger.info("******* Test_003_addcustomer *****************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        # If CAPTCHA apprs, wait for manual completion
        #input("Complete the CAPTCHA and press Enter to continue...")
        self.lp=LoginPage(self.driver)
        self.lp.SetUserName(self.username)
        self.lp.SetPasswaord(self.password)
        self.lp.clicklogin()
        #time.sleep(3)
        # If CAPTCHA appears, wait for manual completion
        #input("Complete the CAPTCHA and press Enter to continue...")
        self.logger.info("*******Login successful************")
        self.logger.info("****** starting Add new customer test**********")

        self.addcust=AddCustomer(self.driver)
        self.addcust.ClickonCustomersMenu()
        self.addcust.Clickoncustomersmenuitem()
        self.addcust.addnewCustomer()
        self.logger.info("***********providing customer info************")
        self.email= random_generator()+"@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setpassword("test@123")
        self.addcust.setfirstname("Nirmala")
        self.addcust.setlastname("kadapa")
        self.addcust.setgenderfemale("female")
        self.addcust.setdateofbirth("30/11/1985")
        self.addcust.setCompanyname("busyQA")
        self.addcust.setcustomerroles("Guests")
        self.addcust.setmangeofvendor("vendor 2")
        self.addcust.setadmincontent("This for testing ...")
        self.addcust.clickonsave()
        self.logger.info("****saving customer info*****")
        self.logger.info("************ validation started*********")
        self.msg= self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissable']").text
        print(self.msg)

        if "The new customer has been added successfully" in self.msg:
            assert True == True
            self.logger.info("****Add customer test passed********")
        else:
            self.driver.save_screenshot("C:\\Users\\Ansar\\PycharmProjects\\pythonProject1\\nopcommerceApp\\Screenshots\\addcustomer.png")
            self.logger.error("****** Add customer test failed ****************")
            assert True ==False
            self.driver.close()
            self.logger.info("***** Ending add customer test*****************")






def random_generator(size=8, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))
