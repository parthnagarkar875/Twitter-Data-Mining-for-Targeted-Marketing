import string
import numpy as np
import pandas as pd
import tweepy
import re
from datetime import datetime
from dateutil import tz
import time

consumer_key='rNrnFupaEqKt0eb7hjbdHKdWg'
consumer_secret= 'DTTMoQOrCBmngaXmOnFhrBjdjwtT54x0AbGvNwwuqyYNWwEvc7'
access_token='1002268050513575936-gGrQUmDiMyCxO2Y88lc3ojqNzbtLGm'
access_token_secret='G572YTe2S5TQTTaXhFvl1WyNopa8ilrkgWSlCXBZQwU4C'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

url_list=list()
username_list=list()
user_profile_list=list()
stored_tweets=list()

query='IITBombay'
word=[query.lower()]
    
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if status.retweeted:
            return True
        from_zone = tz.tzutc()
        to_zone = tz.tzlocal()
        
        utc = status.created_at
        
        
        # Tell the datetime object that it's in UTC time zone since 
        # datetime objects are 'naive' by default
        utc = utc.replace(tzinfo=from_zone)
        
        # Convert time zone
        central = utc.astimezone(to_zone)
        print(central)
    
        
        
    def on_error(self, status_code):
        '''
        Since Twitter API has rate limits, 
        stop srcraping data as it exceed to the thresold.
        '''
        if status_code == 420:
            # return False to disconnect the stream
            return False


try:
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)
    myStream.filter(languages=["en"], track = word)
    
except Exception as e:
    print(e)


