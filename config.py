from os import environ, path
from dotenv import load_dotenv
import sys



ROOT = path.dirname(path.abspath(__file__))
sys.path.append(ROOT)
load_dotenv()

class Config:
    """
    Config parent class
    """
    DEBUG = False
    TESTING = False
    SECRET_KEY = environ.get('SECRET_KEY')
    

class DevConfig(Config):
    """
    Development config class

    """
    DEBUG = True

class TestConfig(Config):
    """
    Testing config class
    """
    TESTING = True

class ProdConfig(Config):
    """
    Production config class
    """
    DEBUG = False
    TESTING = False

config_dict = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig,
    'default': DevConfig
}
