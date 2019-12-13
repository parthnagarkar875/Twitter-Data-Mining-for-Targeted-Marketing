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

url_list=list()
username_list=list()
user_profile_list=list()
stored_tweets=list()

query='hiranandani'

try:     
    conn = psycopg2.connect(database='Hiranandani', user = "postgres", password = "parth123n@#*", host = "127.0.0.1", port = "5432")
except:
    print("Create database first")
        
    
    
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if status.retweeted:
            return True

        id_str = status.id_str
        created_at = status.created_at
        text1 = deEmojify(status.text)     
        text=clean_tweet(text1)
        sentiment = TextBlob(text).sentiment
        polarity = sentiment.polarity
        subjectivity = sentiment.subjectivity
            
        user_created_at = status.user.created_at
        user_location = deEmojify(status.user.location)
        user_description = deEmojify(status.user.description)
        user_followers_count =status.user.followers_count
        longitude = None
        latitude = None
        if status.coordinates:
            longitude = status.coordinates['coordinates'][0]
            latitude = status.coordinates['coordinates'][1]
                
        retweet_count = status.retweet_count
        favorite_count = status.favorite_count     # Quick check contents in tweets
        print(status.text)
        #print("Long: {}, Lati: {}".format(longitude, latitude))
            
        # Store all data in MySQL
        if mydb.is_connected():
            mycursor = mydb.cursor()
            sql = "INSERT INTO {} (id_str,created_at,text,polarity,\
                   subjectivity, user_created_at, user_location,\
                   user_description, user_followers_count, longitude,\
                   latitude, retweet_count, favorite_count) VALUES \
                   (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format('hiranandani')
            val = (id_str, created_at, text, polarity, subjectivity, user_created_at, user_location, \
                user_description, user_followers_count, longitude, latitude, retweet_count, favorite_count)
            mycursor.execute(sql, val)
            mydb.commit()
            mycursor.close()
        
        
        
        
        
    def on_error(self, status_code):
        '''
        Since Twitter API has rate limits, 
        stop srcraping data as it exceed to the thresold.
        '''
        if status_code == 420:
            # return False to disconnect the stream
            return False


if conn.is_connected():
    '''
    Check if this table exits. If not, then create a new one.
    '''
    mycursor = conn.cursor()
    mycursor.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format('hiranandani'))
    if mycursor.fetchone()[0] != 1:
        active.create_tweet_table(query)        
        conn.commit()
    mycursor.close()


try:
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)
    myStream.filter(languages=["en"], track = 'hiranandani')
    
    mydb.close()
except Exception as e:
    print(e)


















