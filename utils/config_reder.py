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
    
