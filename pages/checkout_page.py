from selenium.webdriver.common.by import By
from time import sleep
from bases.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

