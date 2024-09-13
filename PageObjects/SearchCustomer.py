from selenium import webdriver
from selenium.webdriver.common.by import By

class SearchCustomer:
    txtsearchEmail_xpath = "//input[@id='SearchEmail']"
    txtsearchfirstname_xpath= "//input[@id='SearchFirstName']"
    txtlastname_xpath= "//input[@id='SearchLastName']"
    btnSearchcustomer_xpath= "//button[@id='search-customers']"
    linksearch_xpath= "//div[@class='search-text']"

    table_xpath= "//table[@id='customers-grid']"
    tableRows_xpath= '//*[@id="customers-grid"]/tbody/tr'
    tablecolumn_xpath='//*[@id="customers-grid"]/tbody/tr/td'

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.txtsearchEmail_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtsearchEmail_xpath).send_keys(email)
    def setfirstname(self, firstname):
        self.driver.find_element(By.XPATH, self.txtsearchfirstname_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtsearchfirstname_xpath).send_keys(firstname)
    def setlastname(self,lastname):
        self.driver.find_element(By.XPATH, self.txtlastname_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtlastname_xpath).send_keys(lastname)

    def clicksearch(self):
        self.driver.find_element(By.XPATH, self.btnSearchcustomer_xpath).click()

    def getNoofRows(self):
        return len(self.driver.find_element(By.XPATH, self.tableRows_xpath))
    def getNoofColumns(self):
        return len(self.driver.find_element(By.XPATH, self.tablecolumn_xpath))
    def customersearchemail(self,email):
        flag=False
        for r in range(1, self.getNoofRows()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            emailid=table.find_elament(By.XPATH,'//*[@id="customers-grid"]/tbody/tr["+str(r)+"/td[2]').text
            if emailid== email:
                flag= True
                break
        return flag
    def searchcustomerbyname(self,Name):
        flag=False
        for r in range(1, self.getNoofRows()+1):
            table= self.driver.find_element(By.XPATH, self.table_xpath)
            name=table.find_elament(By.XPATH, '//*[@id="customers-grid"]/tbody/tr["+str(r)+"/td[3]').text
            if name==Name:
                flag=True
                break
        return flag






