import tweepy
from textblob import TextBlob

consumer_key = '[consumer_key]'
consumer_key_secret = '[consumer_key_secret]'

access_token = '[access_token]'
access_token_secret = '[access_token_secret]'

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Dogs')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	if analysis.sentiment[0]>0:
		print 'Positive'
	else:
		print 'Negative'
	print("")