# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 14:03:11 2019

@author: Parth
"""
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

query_word='Hiranandani'
word=[query_word.lower()]
query = "SELECT id, username,tweet_text, created_at,location,polarity FROM {}".format(query_word)

try:     
    conn = psycopg2.connect(database=query_word, user = "postgres", password = "parth123n@#*", host = "127.0.0.1", port = "5432")
except:
    print("Create database first")


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



print("Pulling tweets")
searched_tweets=active.pull_tweets(query_word)

for i in searched_tweets:
    if i.retweeted:
        continue
    text1 = active.deEmojify(i.text)     
    text=active.clean_tweet(text1)
    sentiment = TextBlob(text).sentiment
    polarity = sentiment.polarity

    # Store all data in MySQL
    if(conn):
        mycursor = conn.cursor()
        if 'hiranandani' not in (i.user.screen_name).lower():
            sql = "INSERT INTO {} (id,username, tweet_text,created_at,location,polarity) VALUES \
                   (%s, %s,%s, %s, %s, %s)".format(word[0])
            val = (i.id, i.user.screen_name,i.text,i.created_at,i.user.location,polarity)
            mycursor.execute(sql, val)
            
            conn.commit()
        


conn.commit()
conn.close()



