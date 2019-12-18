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

working_mumbai= "(buying mumbai flat) OR (buying mumbai property) OR (buying mumbai real estate) OR (purchasing mumbai flat) OR (purchasing mumbai property) OR (purchasing real estate mumbai) OR (buy mumbai flat) OR (buy mumbai property) OR (buy mumbai real estate) OR (purchase mumbai flat) OR (purchase mumbai property) OR (purchase real estate mumbai) -sale"


#n
query3= "(buying mumbai house) OR (buying mumbai flat) OR (buying mumbai property) OR (buying mumbai real estate) OR (purchasing mumbai house) OR (purchasing mumbai flat) OR (purchasing mumbai property) OR (purchasing real estate mumbai) OR (buy mumbai house) OR (buy mumbai flat) OR (buy mumbai property) OR (buy mumbai real estate) OR (purchase mumbai house) OR (purchase mumbai flat) OR (purchase mumbai property) OR (purchase real estate mumbai) -sale"

query2=" (buying mumbai home) OR (buying mumbai house) OR (buying mumbai flat) OR (buying mumbai property) OR (buying mumbai real estate) OR (purchasing mumbai home) OR (purchasing mumbai house) OR (purchasing mumbai flat) OR (purchasing mumbai property) OR (purchasing real estate mumbai) OR (buy mumbai home) OR (buy mumbai house) OR (buy mumbai flat) OR (buy mumbai property) OR (buy mumbai real estate) OR (purchase mumbai home) OR (purchase mumbai house) OR (purchase mumbai flat) OR (purchase mumbai property) OR (purchase real estate mumbai) -sale"





query_chennai= "(buying chennai flat) OR (buying chennai property) OR (buying chennai real estate) OR (purchasing chennai flat) OR (purchasing chennai property) OR (purchasing real estate chennai) OR (buy chennai flat) OR (buy chennai property) OR (buy chennai real estate) OR (purchase chennai flat) OR (purchase chennai property) OR (purchase real estate chennai) -sale"

home_house= "(buying mumbai home) OR (buying mumbai house) OR (purchasing mumbai home) OR (purchasing mumbai house) OR (buy mumbai home) OR (buy mumbai house) OR (purchase mumbai home) OR (purchase mumbai house) -sale"

looking_searching= "(looking mumbai flat) OR (looking mumbai property) OR (looking mumbai real estate) OR (searching mumbai flat) OR (searching mumbai property) OR (searching real estate mumbai) OR (look mumbai flat) OR (look mumbai property) OR (look mumbai real estate) OR (search mumbai flat) OR (search mumbai property) OR (search real estate mumbai) -sale"

shift="(shift mumbai flat) OR (shifting mumbai flat) OR (shift mumbai property) OR (shifting mumbai property) OR (shift mumbai house) OR (shifting mumbai house) -pack"
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

Buying a house in Mumbai
Purchasing a house in Mumbai
Buy a home
Purchasing a home

I am shifting to Mumbai
I am moving to Mumbai

I am looking to buy a flat in Mumbai
I am looking to purchase a flat in mumbai

I am searching for a flat in Mumbai

'''
















