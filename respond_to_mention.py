import os
import requests
from requests_oauthlib import OAuth1
import get_assets
import upload_image
from main import IMAGE_FILENAME

USERNAME = "daily_shiba_inu"
ID_FILE = "last_mention_id.txt"

USER_ID_ENPOINT = "https://api.twitter.com/2/users/by"
USERNAME_ENDPOINT = "https://api.twitter.com/2/users"
MENTIONS_ENDPOINT = "https://api.twitter.com/2/users"

CONSUMER_KEY = os.environ.get("API_KEY")
CLIENT_SECRET = os.environ.get("API_KEY_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

oauth = OAuth1(CONSUMER_KEY,
               client_secret=CLIENT_SECRET,
               resource_owner_key=ACCESS_TOKEN,
               resource_owner_secret=ACCESS_TOKEN_SECRET)

# Saves the latest mention_id to txt file
def save_mention_id(id):
    f = open(ID_FILE, "w")
    f.write(str(id))
    f.close()
    print("File updated with latest mention ID")
    return

# Retrieves the id from the last time the script ran
def get_mention_id():
    f = open(ID_FILE, "r")
    # Strip removes any whitespace from beginning and end of the string
    last_id = f.read().strip()
    f.close()
    return last_id

# Get user ID to use to look up mentions
def get_user_id():
    req = requests.get(
        url=f"{USER_ID_ENPOINT}?usernames={USERNAME}", auth=oauth)

    res = req.json()
    user_id = res["data"][0]["id"]

    return user_id

# Takes author_id and returns username
def get_username(id):
    req = requests.get(
        url=f"{USERNAME_ENDPOINT}/{id}", auth=oauth)
    res = req.json()
    username = res["data"]["username"]
    return username

# Get all new mentions
def respond_to_mentions(user_id):
    last_id = get_mention_id()
    # since_id returns results with tweet ID that is more recent than last_id
    # Adding the expansions is necessary to get the author ids 
    req = requests.get(
        url=f"{MENTIONS_ENDPOINT}/{user_id}/mentions?since_id={last_id}&expansions=author_id", auth=oauth)

    res = req.json()

    length = res["meta"]["result_count"]
    
    # If no new mentions return
    if length == 0:
        print("No new mentions")
        return
    
    mentions = res["data"]
    
    # Reverse the order so the oldest tweets get replied to first
    for mention in reversed(mentions):
        author_id =  mention["author_id"]
        # Get username to respond to
        mention_username = get_username(author_id)

        # Generate new image
        get_assets.fetch_shiba()
        
        # Get Quote
        quote_data = get_assets.fetch_quote()
        quote = quote_data["quote"]
        author = quote_data["author"]
        
        # Start the image uploading process
        tweet = upload_image.ImageTweet(IMAGE_FILENAME)
        tweet.upload_init()
        tweet.upload_append()
        tweet.upload_finalize()
        # Tweets the image and quote + author @the_user
        tweet.tweet(quote, author, mention_username)

    # Save the newest id in a txt file to be used the next time the script runs to avoid repeated mentions
    new_id = res["meta"]["newest_id"]
    save_mention_id(new_id)


user_id = get_user_id()
respond_to_mentions(user_id)
