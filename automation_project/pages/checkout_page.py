from selenium.webdriver.common.by import By
from time import sleep
from bases.base_page import BasePage

class Checkout_Page(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.FIRSTNAME_TEXBOX_XPATH = "//input[@id='first-name']"
        self.LASTNAME_TEXBOX_XPATH = "//input[@id='last-name']"      
        self.POSTALCODE_TEXBOX_XPATH = "//input[@id='postal-code']"
        self.CONTINUE_BUTTON_XPATH = "//input[@id='continue']"
        self.FINISH_BUTTON_XPATH = "//button[@id='finish']"
        self.MESSAGE_THANK_YOU_XPATH = "//h2[text()='Thank you for your order!']"
        self.MESSAGE_CHECKOUT_SUCCESS_XPATH = "//div[text()='Your order has been dispatched, and will arrive just as fast as the pony can get there!']"

    def do_finish_checkout(self, firstname, lastname, postalcode):
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_postalcode(postalcode)
        self.click_continue()
        self.click_finish()
        self.find(By.XPATH, self.MESSAGE_THANK_YOU_XPATH)
        self.find(By.XPATH, self.MESSAGE_CHECKOUT_SUCCESS_XPATH)
        print("\n\nCheckout successful!")
        sleep(3)

    def enter_firstname(self, firstname):
        firstname_textbox = self.find(By.XPATH, self.FIRSTNAME_TEXBOX_XPATH)
        firstname_textbox.send_keys(firstname)

    def enter_lastname(self, lastname):
        lastname_textbox = self.find(By.XPATH, self.LASTNAME_TEXBOX_XPATH)
        lastname_textbox.send_keys(lastname)

    def enter_postalcode(self, postalcode):
        postalcode_textbox = self.find(By.XPATH, self.POSTALCODE_TEXBOX_XPATH)
        postalcode_textbox.send_keys(postalcode)

    def click_continue(self):
        self.click(By.XPATH, self.CONTINUE_BUTTON_XPATH)

    def click_finish(self):
        self.click(By.XPATH, self.FINISH_BUTTON_XPATH)

    