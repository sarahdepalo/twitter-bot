import requests
from requests_oauthlib import OAuth1
import get_assets
import publish
import constants as const

# Authenticate the connection
oauth = OAuth1(const.CONSUMER_KEY,
               client_secret=const.CLIENT_SECRET,
               resource_owner_key=const.ACCESS_TOKEN,
               resource_owner_secret=const.ACCESS_TOKEN_SECRET)

# Saves the latest mention_id to txt file
def save_mention_id(id):
    f = open(const.ID_FILE, "w")
    f.write(str(id))
    f.close()
    print("File updated with latest mention ID")
    return

# Retrieves the id from the last time the script ran
def get_mention_id():
    f = open(const.ID_FILE, "r")
    # Strip removes any whitespace from beginning and end of the string
    last_id = f.read().strip()
    f.close()
    return last_id

# Get user ID to use to look up mentions
def get_user_id():
    req = requests.get(
        url=f"{const.USERS_ENDPOINT}/by?usernames={const.USERNAME}", auth=oauth)

    res = req.json()
    user_id = res["data"][0]["id"]

    return user_id

# Takes author_id and returns username
def get_username(id):
    req = requests.get(
        url=f"{const.USERS_ENDPOINT}/{id}", auth=oauth)
    res = req.json()
    username = res["data"]["username"]
    return username

def like_tweet(tweet, user_id):
    print("Liking Tweet...")
    
    tweet_id = str(tweet["id"])    
    request_data = {
        'tweet_id': tweet_id
    }
    
    req = requests.post(url=f"{const.USERS_ENDPOINT}/{user_id}/likes", json=request_data, auth=oauth)
    print("Tweet Like Successful: ", req.json()["data"]["liked"])

# Get all new mentions
def respond_to_mentions(user_id):
    last_id = get_mention_id()
    # since_id returns results with tweet ID that is more recent than last_id
    # Adding the expansions is necessary to get the author ids 
    req = requests.get(
        url=f"{const.USERS_ENDPOINT}/{user_id}/mentions?since_id={last_id}&expansions=author_id", auth=oauth)

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
        
        # Like tweet - need the mention id and your own user_id gathered previously
        like_tweet(mention, user_id)
        # Generate new image
        get_assets.fetch_shiba()
        
        # Get Quote
        quote_data = get_assets.fetch_quote()
        quote = quote_data["quote"]
        author = quote_data["author"]
        
        text = f"@{mention_username} bork bork!"
        
        # Start the image uploading process
        image = publish.ImageTweet(const.IMAGE_FILENAME)
        image.upload_init()
        image.upload_append()
        media_id = image.upload_finalize()
        # Tweets the image and quote + author @the_user
        publish.tweet(quote, author, media_id, text)

    # Save the newest id in a txt file to be used the next time the script runs to avoid repeated mentions
    new_id = res["meta"]["newest_id"]
    save_mention_id(new_id)

