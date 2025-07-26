import pytest
from selenium import webdriver
from utils.config_reder import ConfigReader
import allure

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_call", rep)

class BaseTest:
    @pytest.fixture(scope="class",autouse=True)
    def setup(self, request):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get((ConfigReader.get_base_url()))
        request.cls.driver = self.driver
        yield
        self.driver.quit()

        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
            allure.attach(
            self.driver.get_screenshot_as_png(),
            name= f"failed_{request.node.name}",
            attachment_type=allure.attachment_type.PNG
        )
        self.driver.quit()


    