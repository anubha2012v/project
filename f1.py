import tweepy
from textblob import TextBlob

consumer_key='7KR7D3P1aSDompKTypJO99YFk'
consumer_secret='PHUvJSHGMoVrXhpKYwFcSoIvoBn1qViy6a9ORklEVWsQBgQuO0'

access_token='1241559837252575232-dco9Y6ozavq3pCwTozFLpmC9QFHxql'
access_token_secret='aMDb57gFKq2kBCpssZAQ6L7hkgAAC9LkVFZyRRukfULxu'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api=tweepy.API(auth)

public_tweets=api.search('lockdown')

for tweet in public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis)
