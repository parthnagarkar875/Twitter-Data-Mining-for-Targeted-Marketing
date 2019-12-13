# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 15:12:45 2019

@author: Parth
"""

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
import active
from pathlib import Path
import pandas as pd
import concurrent.futures 
import psycopg2
import tweepy
start_time = time.time()
consumer_key='rNrnFupaEqKt0eb7hjbdHKdWg'
consumer_secret= 'DTTMoQOrCBmngaXmOnFhrBjdjwtT54x0AbGvNwwuqyYNWwEvc7'
access_token='1002268050513575936-gGrQUmDiMyCxO2Y88lc3ojqNzbtLGm'
access_token_secret='G572YTe2S5TQTTaXhFvl1WyNopa8ilrkgWSlCXBZQwU4C'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)
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


















