from flask import *
from twitter_config import twitter_api

new_tweet = Blueprint('new_tweet', __name__, template_folder='templates')

@new_tweet.route('/new_tweet', methods=['GET', 'POST'])
def new_tweet_route():

	# new tweet data
	if request.method == "POST":
		new_tweet = request.form['tweet_content']
		twitter_api.update_status(new_tweet)

	return render_template("new_tweet.html")