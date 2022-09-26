import requests
import json

def fetch_shiba():
    # Get the Shiba Inu image url from the Shiba API
    shiba_api = "http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true"

    try: 
        res = requests.get(shiba_api)
    except:
        print("Error while calling API")
        
    # Parse the results and extract the url and image extension
    data = res.text
    parsed_url = json.loads(data)[0]
    image_extension = parsed_url.split('.')[-1]

    # Download the shiba image to later upload as media and tweet
    img_data = requests.get(parsed_url).content
    with open('shiba.' + image_extension, 'wb') as handler:
        handler.write(img_data)

def fetch_quote():
    # Get the inspirational quote from the quote API
    quote_api = "https://zenquotes.io/api/random"

    try:
        res = requests.get(quote_api)
    except:
        print("Error while calling API")
        
    # Parse the results and assign quote and author
    data = res.json()[0]
    return data
 

    