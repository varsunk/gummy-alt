# An alternative to gummy search for my own personal use
import praw
import os
from dotenv import load_dotenv
import yaml
import requests

def scrape_subreddit(subreddit: string, num_posts: int):
    """
    Use praw capabilities to scrape a specific subreddit for its most recent n posts
    """

    client = praw.Reddit(
        client_id,
        client_secret,
        user_agent
    )


if __name__ == "__main__":
    # capture env variables
    config = None
    with open("gummy_config.yaml", 'r') as cfg:
        config = yaml.safe_load(cfg)

    load_dotenv()
    # USER_AGENT = os.getenv("")

    # make a sample request using credentials
    OAUTH = """eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzQxMTUxNDEwLjM5NTk1N
CwiaWF0IjoxNzQxMDY1MDEwLjM5NTk1MywianRpIjoicDgzWEZIdjNaLWo0QmJQX2pla1o3SkdPZWhJdXdRIiwiY2lkIjoiZ3h2QXBjWGlvTFhRai1scUlOTVZEZyIsImxpZCI6InQyX3JpcnQyNWoiLCJhaWQiOiJ0Ml9yaXJ0MjVqIiwibGNh
IjoxNTE1NjI3NDMwMjI0LCJzY3AiOiJlSnlLVnRKU2lnVUVBQURfX3dOekFTYyIsImZsbyI6OX0.IoErPz6t0qNZzLcYqv0EpIoTlczX6Oo_Uh11cA74_sSHPBGqldPmc821Y1cBJtssnCkn4bV0x_HK_UKGpkP0k_zUglPMq5azoPfRjvAw395
RM8jSC2vzlGqbbGZNzdlKXX5ocwRHvsmCxENSqNyDI4PIxkU7ya8u4zO69W5225u2cbUwrNe-OSD1wu2drzPolDJr-rFgRfEuvoH3UGD4i75RrR28iYAuKDyxs7nErEf-iELr00_Q_qUOAwnsZUqUqr1lLQEfVBt99E6drA7Q1TnA6iXKtym8oN
EWFEHnoY2czQ2j_a77dr5pF_-dFQIEe99dhTRf_2pOKG5O8zUhOA"""
    
    # request information
    headers = {
        "Authorization": "bearer " + OAUTH,
        "User-Agent": config["app"]["agent"]
    }

    response = requests.get(
        config["requests"]["request_url"] + "/api/v1/me", # just as an example
        headers=headers
    ) 

    print(response.json())
