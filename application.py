from flask import Flask
import daily_post
import respond
import atexit
from apscheduler.schedulers.background import BackgroundScheduler

application = Flask(__name__)

@application.route("/")

def index():
    return "Follow @daily_shiba_inu!"


def post():
    daily_post.post()
    print("Success!")

def reply():
    user_id = respond.get_user_id()
    respond.respond_to_mentions(user_id)


scheduler = BackgroundScheduler()
# Run the main application once every day
scheduler.add_job(func=post, trigger="interval", days=1)
# Run the respond function once every 5 minutes
scheduler.add_job(func=reply, trigger="interval", minutes=5)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

if __name__ == "__main__":
    application.run(port=5000, debug=True)
