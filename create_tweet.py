from requests_oauthlib import OAuth1Session
import os
import json
import sys
import base64

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")

# Get the request token
request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

try:
    fetch_response = oauth.fetch_request_token(request_token_url)
except ValueError:
    print(
        "There may have been an issue with the consumer_key or consumer_secret you entered."
    )
    
resource_owner_key = fetch_response.get("oauth_token")
resource_owner_secret = fetch_response.get("oauth_token_secret")
print("Got OAuth token: %s" % resource_owner_key)

# Get authorization
base_authorization_url = "https://api.twitter.com/oauth/authorize"
authorization_url = oauth.authorization_url(base_authorization_url)
print("Please go here and authorize: %s" % authorization_url)
verifier = input("Paste the PIN here: ")

# Get the access token
access_token_url = "https://api.twitter.com/oauth/access_token"
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier,
)
oauth_tokens = oauth.fetch_access_token(access_token_url)

access_token = oauth_tokens["oauth_token"]
access_token_secret = oauth_tokens["oauth_token_secret"]

# Make the request
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)






total_bytes = os.path.getsize("./shiba.jpg");
print(total_bytes)


# INIT
init_data = {
     'command': 'INIT',
      'media_type': 'image/jpg',
      'total_bytes': total_bytes,
      'media_category': 'tweet_image'
}
init_response = oauth.post(url="https://upload.twitter.com/1.1/media/upload.json", data=init_data)
media_id = init_response.json()["media_id"]

# UPLOAD

segment_id = 0
bytes_sent = 0
file = open("./shiba.jpg", 'rb')

while bytes_sent < total_bytes:
    chunk = file.read(4*1024*1024)
    
    print("APPEND")
    
    request_data = {
        "command": "APPEND",
        "media_id": media_id,
        "segment_index": segment_id
    }
    
    files = {
        "media": chunk
    }
    
    req = oauth.post(url="https://upload.twitter.com/1.1/media/upload.json", data=request_data, files=files)
    
    if req.status_code < 200 or req.status_code > 299:
        print(req.status_code)
        print(req.text)
        sys.exit(0)

    segment_id = segment_id + 1
    bytes_sent = file.tell()

    print('%s of %s bytes uploaded' % (str(bytes_sent), str(total_bytes)))

print('Upload chunks complete.')


print('FINALIZE')
finalize_data = {
      'command': 'FINALIZE',
      'media_id': media_id
    }

req = oauth.post(url="https://upload.twitter.com/1.1/media/upload.jso", data=request_data)
print(req.json())

processing_info = req.json().get('processing_info', None)
check_status()



# publish_data = {
#     "text": "I am shibe",
#     "media_ids": media_id
# }

payload = {
    "text": "I am shibe",
    "media": {"media_ids": [f"{media_id}"]}
}

response = oauth.post(
    "https://api.twitter.com/2/tweets",
    json=payload,
)

print(response.json())

# with open('./shiba.jpg', 'rb') as img_file:
#     b64_string = base64.b64encode(img_file.read())

# payload = {"media_data" :  b64_string.decode('utf-8'),
#            "media_category": "tweet_image"
#            }

# response = oauth.post(
#     "https://upload.twitter.com/1.1/media/upload.json",
#      json=payload
# )

# Making the request
# response = oauth.post(
#     "https://api.twitter.com/2/tweets",
#     json=payload,
# )

# if response.status_code != 201:
#     raise Exception(
#         "Request returned an error: {} {}".format(response.status_code, response.text)
#     )

# print("Response code: {}".format(response.status_code))

# # Saving the response as JSON
# json_response = response.json()
# print(json.dumps(json_response, indent=4, sort_keys=True))