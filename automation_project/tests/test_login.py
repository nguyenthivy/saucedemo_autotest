from bases.base_test import BaseTest
from pages.login_page import LoginPage
from utils.config_reder import ConfigReader
import allure

class TestLoginWeb(BaseTest):
    @allure.story("valid Login")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_valid(self):
        login_page = LoginPage(self.driver)
        login_page.do_login(ConfigReader.get_username(), ConfigReader.get_password())







