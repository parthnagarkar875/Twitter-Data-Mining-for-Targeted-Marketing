import time
import threading
import urllib
import re
import io
import re
import sys
from time import sleep
import pickle
import os
from math import ceil
from pathlib import Path
import pandas as pd
import concurrent.futures 
import psycopg2
import GetOldTweets3 as got
import tweepy
start_time = time.time()
consumer_key='rNrnFupaEqKt0eb7hjbdHKdWg'
consumer_secret= 'DTTMoQOrCBmngaXmOnFhrBjdjwtT54x0AbGvNwwuqyYNWwEvc7'
access_token='1002268050513575936-gGrQUmDiMyCxO2Y88lc3ojqNzbtLGm'
access_token_secret='G572YTe2S5TQTTaXhFvl1WyNopa8ilrkgWSlCXBZQwU4C'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

query2=" (buying mumbai flat) OR (buying mumbai property) OR (buying mumbai real estate) OR (purchasing mumbai flat) OR (purchasing mumbai property) OR (purchasing real estate mumbai) OR (buy mumbai flat) OR (buy mumbai property) OR (buy mumbai real estate) OR (purchase mumbai flat) OR (purchase mumbai property) OR (purchase real estate mumbai) -sale"
query_chennai= "(buying chennai flat) OR (buying chennai property) OR (buying chennai real estate) OR (purchasing chennai flat) OR (purchasing chennai property) OR (purchasing real estate chennai) OR (buy chennai flat) OR (buy chennai property) OR (buy chennai real estate) OR (purchase chennai flat) OR (purchase chennai property) OR (purchase real estate chennai) -sale"

tweetCriteria = got.manager.TweetCriteria().setQuerySearch(query2)\
                                           .setSince("2019-01-01")\
                                           .setUntil("2019-12-16")\
                                           .setMaxTweets(1000)
tweet = got.manager.TweetManager.getTweets(tweetCriteria)


for i in tweet:
    print(i.date,"\n\n")

'''
I am buying a flat in Mumbai
I am purchasing a property in Mumbai

I want to purchase a flat in Mumbai.
I want to purchase a property in Mumbai

I want to buy a flat in Mumbai
I want to buy a property in Mumbai

'''



