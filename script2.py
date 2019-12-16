# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 14:35:11 2019

@author: Parth
"""
from textblob import TextBlob
import collections
from collections import Counter
import pickle 
import string
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from math import ceil
import tweepy
import active
import numpy as np
import psycopg2
#creating a separate folder for  each tweet

consumer_key='rNrnFupaEqKt0eb7hjbdHKdWg'
consumer_secret= 'DTTMoQOrCBmngaXmOnFhrBjdjwtT54x0AbGvNwwuqyYNWwEvc7'
access_token='1002268050513575936-gGrQUmDiMyCxO2Y88lc3ojqNzbtLGm'
access_token_secret='G572YTe2S5TQTTaXhFvl1WyNopa8ilrkgWSlCXBZQwU4C'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)


query_word='Hiranandani'
word=['No_Loco']

#Opening the file containing previously stored tweets
try:
    h=open('Hiranandani/tweets_hira_new.pickle','rb')
except:
    print("Run the initial code first.")

real_tweets=pickle.load(h)


try:     
    conn = psycopg2.connect(database=query_word, user = "postgres", password = "parth123n@#*", host = "127.0.0.1", port = "5432")
except:
    print("Create database first")

        
active.create_tweet_table(query_word)
for i in real_tweets:
    try:
        text1 = active.deEmojify(i.text)     
        text=active.clean_tweet(text1)
        sentiment = TextBlob(text).sentiment
        polarity = sentiment.polarity
        #userOBJ = api.get_user(i.username)
        if(conn):
            mycursor = conn.cursor()
            sql = "INSERT INTO {} (id,username, tweet_text,created_at,polarity) VALUES \
                   (%s, %s,%s, %s, %s)".format(word[0])
            val = (i.id, i.username,i.text,i.date,polarity)
            mycursor.execute(sql, val)
            
            conn.commit()
    except:
        continue

conn.close()












