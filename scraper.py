# making praw calls to scrape subreddits for post information and comment information
import praw
import credentials

class Scraper:
    def __init__(self, yml_file: str):
        self.credential_info = credentials.retrieve_credentials(yml_file)
    
    def scrape_subreddit(subreddit_name: str):
        # TODO: need to call praw, scrape subreddit posts + comments, pass into LLM api and receive summarization + actionable insights, etc.
        pass
