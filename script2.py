# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:21:46 2019

@author: Parth
"""
import time
import threading
import urllib
import re
import io
import active
import re
import sys
from time import sleep
import pickle
import os
from textblob import TextBlob
from math import ceil
from pathlib import Path
import pandas as pd
import concurrent.futures 
import psycopg2
import GetOldTweets3 as got
import tweepy

table= "keywords"
count=0
val="select id from keywords"

try:     
    conn = psycopg2.connect(database='Hiranandani', user = "postgres", password = "parth123n@#*", host = "127.0.0.1", port = "5432")    
except:
    print("Create database first")



if count==0:
    df=pd.read_sql(val,conn)
    

for i in tweet:
    try:
        text1 = active.deEmojify(i.text)     
        text=active.clean_tweet(text1)
        sentiment = TextBlob(text).sentiment
        polarity = sentiment.polarity
        stat=api.get_status(i.id)
        loco=stat.user.location
        fname=stat.user.name
        # Store all data in MySQL
        if(conn):
            mycursor = conn.cursor()
            sql = "INSERT INTO {} (id, name, username, tweet_text, created_at, location, polarity) VALUES \
                   (%s, %s, %s, %s, %s, %s, %s)".format(table)
            val = (i.id, fname, i.username,i.text,i.date, loco, polarity)
            mycursor.execute(sql, val)
            
            conn.commit()
    except:
        continue


mycursor.close()
conn.close()


