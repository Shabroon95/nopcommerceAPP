import pytest

from PageObjects.LoginPage import LoginPage
from utilities.readproperties import Readconfig
from utilities.customlogger import LogGen
from utilities import ExcelUtils
import time

class Test_002_Login:
    baseURL=Readconfig.getApplicationURL()

    logger=LogGen.loggen()
    path="C:\\Users\\Ansar\\PycharmProjects\\pythonProject1\\nopcommerceApp\\TestData\\logindata.xlsx"

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("************Verifying loginDDT test*****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows=ExcelUtils.getRowCount(self.path, "Sheet1")
        print("print number of rows",self.rows)
        lst_status = []
        for r in range(2, self.rows+1):
            self.username = ExcelUtils.readData(self.path, "Sheet1",r, 1)
            self.password = ExcelUtils.readData(self.path, "Sheet1",r, 2)
            self.exp = ExcelUtils.readData(self.path, "Sheet1", r   , 3)
            self.lp.SetUserName(self.username)
            self.lp.SetPasswaord(self.password)
            self.lp.clicklogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == 'pass':
                    self.logger.info("**********Testcase passed******")
                    self.lp.clicklogout()
                    lst_status.append("pass")
                elif self.exp== 'fail':
                    self.logger.info("******test case failed*********")
                    self.lp.clicklogout()
                    lst_status.append("fail")
            elif act_title != exp_title:
                if self.exp == 'pass':
                    self.logger.info("****test case failed***********")
                    lst_status.append('fail')
                elif self.exp == 'fail':
                    self.logger.info("*****Test case pass***********")
                    lst_status.append('pass')
            if 'fail' not in lst_status:
                self.logger.info("****** login DDT test passed******")
                self.driver.close()
                assert True
            else:
                self.logger.info("****** login DDT test failed*******")
                assert False



        self.logger.info("****** Login DDT test case ended*************")



