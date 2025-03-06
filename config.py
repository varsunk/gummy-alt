# config class to define an object that can store all configuration details
import os
from dotenv import load_dotenv
import yaml

class Config:
    def __init__(self, yml_file: str):
        self._yml_file = yml_file
        self._read_yml(self._yml_file)
        self._read_env()

    @property
    def app_name(self):
        return self._app_name

    @property
    def app_agent(self):
        return self._app_agent

    @property
    def app_secret(self):
        return self._app_secret

    @property
    def app_client_id(self):
        return self._app_client_id
    
    @property
    def app_grant_type(self):
        return self._app_grant_type

    @property
    def account_username(self):
        return self._username

    @property
    def account_password(self):
        return self._password

    @property
    def token_acquire_url(self):
        return self._token_acq_url

    @property
    def request_url(self):
        return self._request_url

    def _read_yml(self, yml_file: str):
        # load yaml config
        config = None
        with open(yml_file, 'r') as cfg:
            config = yaml.safe_load(cfg)

        self._config = config
        self._app_name = self._config["app"]["name"]
        self._app_agent = self._config["app"]["agent"]
        self._token_acq_url = self._config["requests"]["token_acquire_url"]
        self._request_url = self._config["requests"]["request_url"]

    def _read_env(self):
        # load environment variables
        load_dotenv()
        # app info
        self._app_secret = os.getenv("APP_SECRET")
        self._app_client_id = os.getenv("APP_CLIENT_ID")
        self._username = os.getenv("ACCOUNT_USERNAME")
        self._password = os.getenv("ACCOUNT_PASSWORD")
        self._grant_type = os.getenv("APP_GRANT_TYPE")

