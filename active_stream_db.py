# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 12:47:44 2019

@author: Parth
"""
import active
import collections
from collections import Counter
import pickle 
import string
import numpy as np
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from math import ceil
import tweepy
import psycopg2
import re


consumer_key=''
consumer_secret= ''
access_token=''
access_token_secret=''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

url_list=list()
username_list=list()
user_profile_list=list()
stored_tweets=list()

query='Hiranandani'
word=[query.lower()]
try:     
    conn = psycopg2.connect(database=query, user = "postgres", password = "parth123n@#*", host = "127.0.0.1", port = "5432")
except:
    print("Create database first")
        
    
    
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if status.retweeted:
            return True
        print(status.text)
        text1 = active.deEmojify(status.text)     
        text=active.clean_tweet(text1)
        sentiment = TextBlob(text).sentiment
        polarity = sentiment.polarity

        # Store all data in MySQL
        if(conn):
            mycursor = conn.cursor()
            if 'hiranandani' not in (status.user.screen_name).lower():
                sql = "INSERT INTO {} (id,username, tweet_text,created_at,location,polarity) VALUES \
                       (%s, %s,%s, %s, %s, %s)".format(word[0])
                val = (status.id, status.user.screen_name,status.text,status.created_at,status.user.location,polarity)
                mycursor.execute(sql, val)
                
                conn.commit()
        mycursor.close()
        
        
        
    def on_error(self, status_code):
        '''
        Since Twitter API has rate limits, 
        stop srcraping data as it exceed to the thresold.
        '''
        if status_code == 420:
            # return False to disconnect the stream
            return False


if(conn):
    '''
    Check if this table exits. If not, then create a new one.
    '''
    mycursor = conn.cursor()
    mycursor.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(word[0]))
    if mycursor.fetchone()[0] != 1:
        active.create_tweet_table(query)        
        conn.commit()
    mycursor.close()


try:
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)
    myStream.filter(languages=["en"], track = word)
    
    conn.close()
except Exception as e:
    print(e)


