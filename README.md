<style>

svg {
  height: 10px;
}

</style>

<h1 align= "center">
 Inspirational Shiba Inu Twitter Bot
</h1>


<p align="center">
<img src="./public/shiba_tweet.png"  width="600"/>
</p>

<p align="center">
    <svg viewBox="328 355 335 276" xmlns="http://www.w3.org/2000/svg">
  <path d="
    M 630, 425
    A 195, 195 0 0 1 331, 600
    A 142, 142 0 0 0 428, 570
    A  70,  70 0 0 1 370, 523
    A  70,  70 0 0 0 401, 521
    A  70,  70 0 0 1 344, 455
    A  70,  70 0 0 0 372, 460
    A  70,  70 0 0 1 354, 370
    A 195, 195 0 0 0 495, 442
    A  67,  67 0 0 1 611, 380
    A 117, 117 0 0 0 654, 363
    A  65,  65 0 0 1 623, 401
    A 117, 117 0 0 0 662, 390
    A  65,  65 0 0 1 630, 425
    Z"
    style="fill:#3BA9EE;"/>
    </svg>
Tweet <a href="https://twitter.com/daily_shiba_inu" target="_blank">@daily_shiba_inu</a> for an inspirational quote!</p>

<p>
 This bot was created with love and as a way to get back into Python coding. I've always been interested in automation and figured this was a great way to learn more about automation with Python. 
 </p>
 
 <p>The bot is a Flask application hosted on AWS. Currently, the bot tweets an inspirational quote from the <a href="https://zenquotes.io/api/random" target="_blank">Zen Quotes API</a> alongside a random Shiba Inu image from the <a href="http://shibe.online/" target="_blank">Shibe API</a>. The Twitter API is then used to upload and post the image. 
</p>

<p>
<img src="./public/shiba_icon.png" width="20"/>The bot also checks for mentions every 5 minutes and will respond with some wisdom!
</p>

<h2 align= "center">
 Creating Your Own Bot <img src="./public/doge.png" width="20">
</h2>


If you wish to use this project as a template for creating your own bot, do the following.

## Prerequisites

* Create a developer account with Twitter
* Request elevated access to be able to use the API v2 (necessary to upload images)
* Save your keys in a .env or somewhere safe.
* Create an account with AWS or your hosting service of choice

## Installation

```bash
# Clone the repo
$ git clone https://github.com/sarahdepalo/twitter-bot.git

# Change into the directory
$ cd twitterbot

# Install dependencies
$ pip install -r requirements.txt

# Swap out your credentials in constants.py
# Publish a post
$ python3 daily_post.py
```

