import tweepy
from textblob import TextBlob

consumer_key='7KR7D3P1aSDompKTypJO99YFk'
consumer_secret='PHUvJSHGMoVrXhpKYwFcSoIvoBn1qViy6a9ORklEVWsQBgQuO0'

access_token='1241559837252575232-2of8dDZcrG4ENzIbSP4uo9k41VJuZR'
access_token_secret='AqEzRw2UPVjxQGkwd1vMLaTotln3nRuaMLoppEzJl6IPn'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api=tweepy.API(auth)

public_tweets=api.search('lockdown')

for tweet in public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)
    print(" ")
