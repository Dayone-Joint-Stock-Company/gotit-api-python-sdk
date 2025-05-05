from gotit_api_python_sdk.configuration import Configuration
from gotit_api_python_sdk.api_client import ApiClient
from config import Config

class GotItAPIClient:
    def __init__(self):
        self.configuration = Configuration(host=Config.API_HOST)
        self.authorization = Config.X_GI_AUTHORIZATION

    def get_client(self):
        return ApiClient(self.configuration)

    def get_authorization(self):
        return self.authorization 