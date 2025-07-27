from selenium.webdriver.common.by import By
from time import sleep
from bases.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.LOGIN_BUTTON_XPATH = "//input[@id='login-button']"
        self.USERNAME_TEXBOX_XPATH = "//input[@id='user-name']"  
        self.PASSWORD_TEXBOX_XPATH = "//input[@id='password']"
        self.PRODUCTS_TITLE_XPATH = "//span[text()='Products']"

    def do_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        self.find(By.XPATH, self.PRODUCTS_TITLE_XPATH)
        sleep(3)
        print("\n\nLogin successful!")

    def enter_username(self, username):
        username_textbox = self.find(By.XPATH, self.USERNAME_TEXBOX_XPATH)
        username_textbox.send_keys(username)

    def enter_password(self, password):
        password_textbox = self.find(By.XPATH, self.PASSWORD_TEXBOX_XPATH)
        password_textbox.send_keys(password)

    def click_login(self):
        self.click(By.XPATH, self.LOGIN_BUTTON_XPATH)
     