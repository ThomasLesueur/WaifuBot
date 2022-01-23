import tweepy
import os
import requests
from dotenv import load_dotenv

load_dotenv()
def bearer_oauth(self, r):
    bearer_token = str(os.getenv('BEARER_TOKEN'))

    """
    Method required by bearer token authentication.
    """
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

class TwitterService:
    api_key = str(os.getenv('API_KEY'))
    api_secret = str(os.getenv('API_SECRET_KEY'))
    access_token = str(os.getenv('ACCESS_TOKEN'))
    secret_token = str(os.getenv('ACCESS_TOKEN_SECRET'))

    def set_api(self):
        auth = tweepy.OAuthHandler(self.api_key, self.api_secret)
        auth.set_access_token(self.access_token, self.secret_token)

        # Create API object
        api = tweepy.API(auth)

        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")
        return api

    def post_tweet(self, content):
        # Authenticate to Twitter
        api = self.set_api()
        api.update_status("", media_ids=content)

    def get_media_id(self, image):
        api = self.set_api()
        media = api.simple_upload(image)
        return media.media_id