# Stream tweets from Twitter using a hashtag or other string.
# mostly taken from http://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/

__author__ = 'Brad'

# Import Tweepy and create authorization settings.
import tweepy
from tweepy import OAuthHandler

# Authentication settings
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


import json
from tweepy import Stream
from tweepy.streaming import StreamListener

file_name = 'test3.json';

# Define the stream class.
class MyListener(StreamListener): # MyListener is an istance of StreamListener
    def on_data(self, data): # function
        try:
            with open(file_name, 'a') as f:
                f.write(data) # Save the incoming tweet
                #f.write('\n') # I found that this extra line causes problems when opening
                print(json.loads(data)["text"]) # print as a sanity check
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

# Open the stream with a particular filter
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#LouisAppreciationDay'])


