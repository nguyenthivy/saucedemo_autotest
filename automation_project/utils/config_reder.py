import json
import os

class ConfigReader:
    _config = None

    @staticmethod
    def load_config():
        file_path = os.path.join(os.path.dirname(__file__),'saucedemo_url.json')
        with open(file_path, 'r') as file:
            ConfigReader._config = json.load(file)
        return ConfigReader._config
    
    @staticmethod
    def get_base_url():
        return ConfigReader.load_config()['base_url']
    
    @staticmethod
    def get_username():
        return ConfigReader.load_config()['cridentials']['username']
    
    @staticmethod
    def get_password():
        return ConfigReader.load_config()['cridentials']['password']
    
    @staticmethod
    def get_timeout():
        return ConfigReader.load_config()['timeout']
    
    @staticmethod
    def get_producttag():
        return ConfigReader.load_config()['products']['productstag']
    
    @staticmethod
    def get_first_name():
        return ConfigReader.load_config()['checkout_infomation']['firstname']
    
    @staticmethod
    def get_last_name():
        return ConfigReader.load_config()['checkout_infomation']['lastname']
    
    @staticmethod
    def get_postal_code():
        return ConfigReader.load_config()['checkout_infomation']['postalcode']