#!/usr/bin/env python3

import os
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = 
access_token_secret = 
consumer_key = 
consumer_secret = 

class StdOutListener(StreamListener):
    def on_data(self, data):
        global path
        try:
            with open(path + '/tweets.json', 'a') as output:
                output.write(data)
        except BaseException as e:
            print("Error:", e)
        return 1
    def on_error(self, status):
        print(status)
        return 1

if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    listener = StdOutListener()
    path = os.path.dirname(__file__)
    stream = Stream(auth, listener)
    stream.filter(track=['trump', 'Trump'])