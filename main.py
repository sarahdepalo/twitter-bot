import get_assets
import upload_image

IMAGE_FILENAME = './shiba.jpg'

if __name__ == '__main__':
  # Updates the local file ./shiba.jpg to be used in the tweet
  get_assets.fetch_shiba()
  # Gets the inspirational quote and author from the API
  quote_data = get_assets.fetch_quote()
  quote = quote_data["quote"]
  author = quote_data["author"]
  # Starts the image uploading and tweet process.  
  tweet = upload_image.ImageTweet(IMAGE_FILENAME)
  tweet.upload_init()
  tweet.upload_append()
  tweet.upload_finalize()
  # Tweets the image and quote + author   
  tweet.tweet(quote, author)