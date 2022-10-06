import os

# File information
IMAGE_FILENAME = './shiba.jpg'
ID_FILE = "last_mention_id.txt"

# Bot username
USERNAME = "daily_shiba_inu"

# Twitter API Endpoints
# Chunk uploading enpoint used for INIT - FINALIZE
MEDIA_UPLOAD_ENDPOINT = 'https://upload.twitter.com/1.1/media/upload.json'
POST_TWEET_ENDPOINT = 'https://api.twitter.com/1.1/statuses/update.json'
USERS_ENDPOINT = "https://api.twitter.com/2/users"

# Twitter API vars
CONSUMER_KEY = os.environ.get("API_KEY")
CLIENT_SECRET = os.environ.get("API_KEY_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")