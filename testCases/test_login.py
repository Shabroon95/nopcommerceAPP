import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import LoginPage
from utilities.readproperties import Readconfig
from utilities.customlogger import LogGen


@pytest.mark.sanity
class Test_001_Login:
    baseURL=Readconfig.getApplicationURL()
    username=Readconfig.getUsermail()
    password=Readconfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.sanity

    def test_homepagetitle(self, setup):
        self.logger.info("*************Test_001_Login**********************")
        self.logger.info("***********verifying homepage title************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**********home page Title testcase passed***********")

        else:
            self.driver.save_screenshot("C:\\Users\\Ansar\\PycharmProjects\\pythonProject1\\nopcommerceApp\\Screenshots\\test_homePageTitle.png")
            self.driver.close()
            self.logger.info("**********home page Title testcase failed***********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("************Verifying login test*****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.SetUserName(self.username)
        self.lp.SetPasswaord(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.save_screenshot("C:\\Users\\Ansar\\PycharmProjects\\pythonProject1\\nopcommerceApp\\Screenshots\\test_loginPageTitle.png")
            self.logger.info("*********** Login Home page Tiles test case passed************")
            self.driver.close()

        else:

            self.driver.save_screenshot("C:\\Users\\Ansar\\PycharmProjects\\pythonProject1\\nopcommerceApp\\Screenshots\\test_loginPageTitle.png")
            self.logger.info("**************Login home page title test case failed**********")
            assert False


