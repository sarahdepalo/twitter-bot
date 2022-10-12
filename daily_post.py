import get_assets
import publish
from constants import IMAGE_FILENAME as img_file

def post():
    # Updates the local file ./shiba.jpg to be used in the tweet
    get_assets.fetch_shiba()
    # Gets the inspirational quote and author from the API
    quote_data = get_assets.fetch_quote()
    quote = quote_data["quote"]
    author = quote_data["author"]
    # Starts the image uploading and tweet process.
    image = publish.ImageTweet(img_file)
    image.upload_init()
    image.upload_append()
    media_id = image.upload_finalize()
    # Tweets the image and quote + author
    publish.tweet(quote, author, media_id)

if __name__ == "__main__":
    post()