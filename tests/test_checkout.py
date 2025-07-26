import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Doạn này đảm bảo rằng các module trong thư mục cha có thể được import vào
from bases.base_test import BaseTest
from pages.login_page import LoginPage
from pages.cart_page import Cart_Page
from utils.config_reder import ConfigReader
import allure
from allure_commons.types import Severity

class TestCheckcard(BaseTest):
    @allure.story("valid Login")
    @allure.severity(allure.severity_level.CRITICAL)
    def testcard(self):
        login_page = LoginPage(self.driver)
        login_page.do_login(ConfigReader.get_username(), ConfigReader.get_password())
        cart_page = Cart_Page(self.driver)
        cart_page.do_findproduct()
        cart_page.click_ckeckout()


        

