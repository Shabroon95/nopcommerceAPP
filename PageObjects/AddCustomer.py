from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class AddCustomer:
    #add customer page
    lnkcustomers_menu_xpath= "//a[@href='#']//p[contains(text(),'Customers')]"
    lnlcustomers_menuitem_xpath= "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[normalize-space()='Add new']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstname_xpath= "//input[@id='FirstName']"
    txtLastname_xpath= "//input[@id='LastName']"
    rdGendermale_xpath= "//label[normalize-space()='Male']"
    rdGenderfemale_xpath= "//label[normalize-space()='Female']"
    txtDOB_xpath = "//input[@id='DateOfBirth']"
    txtComapany_xpath= "//input[@id='Company']"
    txtCustomerrole_xpath = "//span[@aria-expanded='true']//input[@role='searchbox']"
    listitemAdministrator_xpath = "//li[@title='Administrators']"
    listitemRegistered_xpath= "//li[@title='Registered']"
    listitemvendor_xpath = "//li[@title='Vendors']"
    listitemGuests_xpath= "//li[@title='Guests']"
    drpmgrVendor_xpath = "//select[@id='VendorId']"
    rdActive_xpath= "//input[@id='Active']"
    txtAdmincomment_xpath= "//textarea[@id='AdminComment']"
    btnsave_xpath = "//button[@name='save']"
    listitem =[]

    def __init__(self,driver):
        self.driver=driver
    def ClickonCustomersMenu(self):
        self.driver.find_element(By.XPATH,self.lnkcustomers_menu_xpath).click()
    def Clickoncustomersmenuitem(self):
        self.driver.find_element(By.XPATH, self.lnlcustomers_menuitem_xpath).click()
    def addnewCustomer(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()
    def setEmail(self, emial):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(emial)
    def setpassword(self,password ):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(password)
    def setfirstname(self, firstname):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(firstname)

    def setlastname(self, lastname):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(lastname)
    def setgenderfemale(self):
        self.driver.find_element(By.XPATH, self.rdGenderfemale_xpath).click()

    def setgendermale(self):
        self.driver.find_element(By.XPATH, self.rdGendermale_xpath).click()
    def setdateofbirth(self,dob):
        self.driver.find_element(By.XPATH, self.txtDOB_xpath).send_keys(dob)
    def setCompanyname(self,companyname):
        self.driver.find_element(By.XPATH, self.txtComapany_xpath).send_keys(companyname)
    def setcustomerroles(self,role):
        self.driver.find_element(By.XPATH, self.txtCustomerrole_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem=self.driver.find_element(By.XPATH, self.listitemRegistered_xpath)
        elif role == "Administrators":
            self.listitem=self.driver.find_element(By.XPATH, self.listitemAdministrator_xpath)
        elif role == "Guests":
            #here user can be a registered or guest only one
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//li[@title='Registered']//span[@role='presentation'][normalize-space()='×']").click()
            self.listitem=self.driver.find_element(By.XPATH, self.listitemGuests_xpath)
        elif role == 'Registered':
            self.listitem=self.driver.find_element(By.XPATH, self.listitemRegistered_xpath)
        elif role=='vendors':
            self.listitem=self.driver.find_element(By.XPATH, self.listitemvendor_xpath)
        else:
            self.listitem =self.driver.find_element(By.XPATH, self.listitemGuests_xpath)
            time.sleep(3)
            self.driver.execute_script("arguments[0].click();",self.listitem)


    def setadmincontent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdmincomment_xpath).send_keys(content)
    def setmangeofvendor(self, value):
        drpdown= Select(self.driver.find_element(By.XPATH, self.drpmgrVendor_xpath))
        drpdown.select_by_visible_text(value)
    def setactive(self):
        self.driver.find_element(By.XPATH, self.rdActive_xpath).click()
    def clickonsave(self):
        self.driver.find_element(By.XPATH, self.btnsave_xpath).click()












