import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # API Configuration
    API_HOST = "https://api-biz-stg.gotit.vn"
    X_GI_AUTHORIZATION = os.getenv('X_GI_AUTHORIZATION', '')
    PRIVATE_KEY_STR = os.getenv('PRIVATE_KEY_STR', '')

    # Flask Configuration
    FLASK_APP = "app.py"
    FLASK_ENV = "development"
    DEBUG = True

    # API Default Values
    DEFAULT_PAGE = 1
    DEFAULT_PAGE_SIZE = 200
    DEFAULT_MIN_PRICE = 1000
    DEFAULT_MAX_PRICE = 10000000
    DEFAULT_STORE_PAGE = 1
    DEFAULT_STORE_PAGE_SIZE = 50 