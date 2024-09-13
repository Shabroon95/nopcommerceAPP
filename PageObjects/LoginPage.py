from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_xpath = "//input[@id='Email']"
    textbox_password_xpath = '//*[@id="Password"]'
    button_login_xpath = '//*[@id="main"]/div/div/div/div[2]/div[1]/div/form/div[3]/button'
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def SetUserName(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def SetPasswaord(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clicklogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()

               


