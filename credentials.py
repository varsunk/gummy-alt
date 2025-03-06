# collect all the necessary credentials for the app
import requests
import requests.auth
# import our own config class
import config

def retrieve_credentials(yml_file: str):
    app_config = config.Config(yml_file)

    # making the request for the oauth token
    client_auth = requests.auth.HTTPBasicAuth(app_config.app_client_id, app_config.app_secret)
    post_data = {
        "grant_type": app_config.app_grant_type,
        "username": app_config.account_username,
        "password": app_config.account_password
    }
    headers = {
        "User-Agent": app_config.app_agent
    }

    response = requests.post(
        app_config.token_acquire_url + "/api/v1/access_token",
        auth=client_auth,
        data=post_data,
        headers=headers
    )

    return response
