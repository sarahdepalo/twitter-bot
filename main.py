from requests_oauthlib import OAuth1Session
import os
import json
import tweepy
import requests
import base64

# consumer_key = os.environ.get("CONSUMER_KEY")
# consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")

client = tweepy.Client(bearer_token=access_token)

# Get the Shiba Inu image url from the api 
shiba_api = "http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true"

try:
    response = requests.get(shiba_api)
except:
    print("error while calling API")

# Parse the results and extract the url and image extension
data = response.text
parsed_url = json.loads(data)[0]
image_extension = parsed_url.split('.')[-1]

# Download the shiba image to later upload as media and tweet
img_data = requests.get(parsed_url).content
with open('shiba.' + image_extension, 'wb') as handler:
    handler.write(img_data)
 
# In order to upload an image to Twitter, the image needs to be base64 format - we can do that using the base64 module
with open('shiba.' + image_extension, 'rb') as img_file:
    b64_string = base64.b64encode(img_file.read())
    
# If you have issues and need to remove the b from the prefix of base64 use this:
# b64_string.decode('utf-8)
print(b64_string)

# Next steps = use twitter API to upload image to twitter and get the returned media_id
# This media_id will be used to create a tweet




# client.create_tweet(media={"http://shibe.online/api/shibes?count=1&urls=[true/false]&httpsUrls=true"})



# query = 'dog -is:retweet'
# file_name = "tweets.txt"
# if not os.path.exists(file_name):
#     open(file_name, 'w').close()

# with open(file_name, 'a+') as filehandle:
#     for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, tweet_fields=['text', 'created_at'], max_results=100).flatten(limit=10):
#         filehandle.write('%s\n' % tweet.text)