from selenium.webdriver.common.by import By
from time import sleep
from bases.base_page import BasePage
from pages import LOGIN_BUTTON_XPATH, USERNAME_TEXBOX_XPATH, PASSWORD_TEXBOX_XPATH , PRODUCTS_TITLE_XPATH

class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def do_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        self.find(By.XPATH, PRODUCTS_TITLE_XPATH)
        sleep(3)
        print("\n\nLogin successful!")

    def enter_username(self, username):
        username_textbox = self.find(By.XPATH, USERNAME_TEXBOX_XPATH)
        username_textbox.send_keys(username)

    def enter_password(self, password):
        password_textbox = self.find(By.XPATH, PASSWORD_TEXBOX_XPATH)
        password_textbox.send_keys(password)

    def click_login(self):
        self.click(By.XPATH, LOGIN_BUTTON_XPATH)
     