import string
import numpy as np
import pandas as pd
import tweepy
import re
from datetime import datetime
from dateutil import tz
import time
import active
import GetOldTweets3 as got

consumer_key='rNrnFupaEqKt0eb7hjbdHKdWg'
consumer_secret= 'DTTMoQOrCBmngaXmOnFhrBjdjwtT54x0AbGvNwwuqyYNWwEvc7'
access_token='1002268050513575936-gGrQUmDiMyCxO2Y88lc3ojqNzbtLGm'
access_token_secret='G572YTe2S5TQTTaXhFvl1WyNopa8ilrkgWSlCXBZQwU4C'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

query='(purchase mumbai flat) OR (purchase mumbai property)'
query1= '(purchase mumbai flat) OR (purchase mumbai property) OR (rent flat mumbai) OR (rent property mumbai)'

tweetCriteria = got.manager.TweetCriteria().setQuerySearch('Hiranandani')\
                                           .setSince("2019-05-01")\
                                           .setUntil("2019-12-16")\
                                           .setMaxTweets(1000)
tweet = got.manager.TweetManager.getTweets(tweetCriteria)
#print(tweet.text)

url="https://twitter.com/"

list1=[]
for i in tweet:
    url2=url
    url2+=i.username+"/status/"+i.id
    list1.append(url2)