from flask import *
from twitter_config import twitter_api

show_tweets = Blueprint('show_tweets', __name__, template_folder='templates')

def is_good_tweet(tweet):
	return not tweet.startswith("rt") and not tweet.startswith("@") and "http" not in tweet

@show_tweets.route('/show_tweets', methods=['GET', 'POST'])
def show_tweets_form_route():

	if request.method == "POST":
		return redirect(url_for('show_tweets.show_tweets_specified_route', username=request.form['request_username']))

	return render_template("show_tweets_form.html")

@show_tweets.route('/show_tweets/<username>', methods=['GET', 'POST'])
def show_tweets_specified_route(username):

	tweets = twitter_api.user_timeline(screen_name=username, count=5000)
	tweets_list = []
	for tweet in tweets:
		tweets_list.append(tweet.text.encode('utf-8').lower())

	f = open('test/'+username+'.txt', 'w')
	for tweet in tweets_list:
		if is_good_tweet(tweet):
			f.write(tweet+"\n")

	return render_template("show_tweets.html")