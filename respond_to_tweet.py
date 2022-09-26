# Need to lookup user Id first. 
# If mentions == 0 return
# Need to store the last responded to tweet in a txt file. 
# This way the script won't reply to old mentions
# Otherwise for each mention in mentions 
# Create tweet with image and quote
# If tweet has hashtag shiba in it return with image + bork bork

import os
import requests
from requests_oauthlib import OAuth1

USERNAME = "daily_shiba_inu"

USER_ID_ENPOINT = "https://api.twitter.com/2/users/by"
MENTIONS_URL_ENDPOINT = "https://api.twitter.com/2/users"

CONSUMER_KEY = os.environ.get("API_KEY")
CLIENT_SECRET = os.environ.get("API_KEY_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

oauth = OAuth1(CONSUMER_KEY,
  client_secret=CLIENT_SECRET,
  resource_owner_key=ACCESS_TOKEN,
  resource_owner_secret=ACCESS_TOKEN_SECRET)

# Get user ID to use to look up mentions
def get_user_id():
  req = requests.get(url=f"{USER_ID_ENPOINT}?usernames={USERNAME}", auth=oauth)

  res = req.json()
  user_id = res["data"][0]["id"]

  return user_id

# Get all new mentions
def get_mentions(user_id):
    req = requests.get(url=f"{MENTIONS_URL_ENDPOINT}/{user_id}/mentions", auth=oauth)
    
    res = req.json()
    print(res)
    length = res["meta"]["result_count"]
    # If no new mentions return
    if length == 0:
        print("No new mentions")
        return
    mentions = res["data"]
    # Reverse the order so the oldest tweets get replied to first
    for mention in reversed(mentions):
        # Generate image and post
        print(mention["text"])
    
  
    

user_id = get_user_id()
get_mentions(user_id)