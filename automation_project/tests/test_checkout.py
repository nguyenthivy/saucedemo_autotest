import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Doạn này đảm bảo rằng các module trong thư mục cha có thể được import vào
from bases.base_test import BaseTest
from pages.login_page import LoginPage
from pages.inventory_page import Inventory_Page
from pages.cart_page import Cart_Page
from pages.checkout_page import Checkout_Page
from utils.config_reder import ConfigReader
import allure


class TestCheckcard(BaseTest):
    @allure.story("valid Login")
    @allure.severity(allure.severity_level.CRITICAL)
    def testcard(self):
        login_page = LoginPage(self.driver)
        login_page.do_login(ConfigReader.get_username(), ConfigReader.get_password())

        inventory_page = Inventory_Page(self.driver)
        inventory_page.do_add_to_cart(ConfigReader.get_producttag())

        cart_page= Cart_Page(self.driver)
        cart_page.do_checkout()

        checkout_page = Checkout_Page(self.driver)
        checkout_page.do_finish_checkout(ConfigReader.get_first_name(), 
                                  ConfigReader.get_last_name(), 
                                  ConfigReader.get_postal_code())
       

        


        

