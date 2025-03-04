# collect all the necessary credentials for the app
import requests
import requests.auth
import os
from dotenv import load_dotenv
import yaml

# load env variables
load_dotenv()

# app info
APP_SECRET = os.getenv("APP_SECRET")
APP_CLIENT_ID = os.getenv("APP_CLIENT_ID")

# personal credentials
USERNAME = os.getenv("ACCOUNT_USERNAME")
PASSWORD = os.getenv("ACCOUNT_PASSWORD")
GRANT_TYPE = os.getenv("APP_GRANT_TYPE")

# load yaml config
config = None
with open("gummy_config.yaml", 'r') as cfg:
    config = yaml.safe_load(cfg)

# making the request for the oauth token
client_auth = requests.auth.HTTPBasicAuth(APP_CLIENT_ID, APP_SECRET)
post_data = {
    "grant_type": GRANT_TYPE,
    "username": USERNAME,
    "password": PASSWORD
}
headers = {
    "User-Agent": config["app"]["agent"]
}

response = requests.post(
    config["requests"]["token_acquire_url"] + "/api/v1/access_token",
    auth=client_auth,
    data=post_data,
    headers=headers
)

# print response json (user should take note of their oauth token in order to use token)
# TODO: write the response.json values to a file for proper formatting
print(response.json())
