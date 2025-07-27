from selenium.webdriver.common.by import By
from time import sleep
from bases.base_page import BasePage


class Cart_Page(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.CHECKOUT_BUTTON_XPATH = "//button[text()='Checkout']"

    def do_checkout(self):
        self.click_checkout_button()

    def click_checkout_button(self):
        self.click(By.XPATH, self.CHECKOUT_BUTTON_XPATH)