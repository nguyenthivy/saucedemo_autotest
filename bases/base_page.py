
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select as Select
from utils.config_reder import ConfigReader



class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, by, value, timeout=ConfigReader.get_timeout()):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))
    
    def find_all(self, by, value, timeout=ConfigReader.get_timeout()):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((by, value)))
    
    def select_dropdown(self,by, value,select_text):
        select_dropdown=Select(self.find(by, value))
        select_dropdown.select_by_visible_text(select_text)

    def click(self, by, value):
        self.find(by, value).click()

    def send_keys(self, by, value, text):
        self.find(by, value).send_keys(text)



    