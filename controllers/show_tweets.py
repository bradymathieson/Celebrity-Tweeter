from flask import *
from twitter_config import twitter_api

show_tweets = Blueprint('show_tweets', __name__, template_folder='templates')

@show_tweets.route('/show_tweets', methods=['GET', 'POST'])
def show_tweets_route():

	# new tweet data
	if request.method == "POST":
		new_tweet = request.form['tweet_content']
		twitter_api.update_status(new_tweet)

	return render_template("show_tweets.html")