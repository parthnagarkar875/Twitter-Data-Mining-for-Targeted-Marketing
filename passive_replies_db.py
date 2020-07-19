# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 16:59:31 2019

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
consumer_key=''
consumer_secret= ''
access_token=''
access_token_secret=''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
word='passive'
query_word='Hiranandani'
query = "SELECT id, username,tweet_text, created_at,location,polarity FROM {}".format(query_word)

try:     
    conn = psycopg2.connect(database=query_word, user = "postgres", password = "parth123n@#*", host = "127.0.0.1", port = "5432")
except:
    print("Create database first")

cur= conn.cursor()


if(conn):
    '''
    Check if this table exits. If not, then create a new one.
    '''
    mycursor = conn.cursor()
    mycursor.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(word))
    if mycursor.fetchone()[0] != 1:
        cur.execute('''CREATE TABLE {} (USERNAME TEXT,LOCATION TEXT);'''.format(word))
        conn.commit()
    mycursor.close()

df=pd.read_sql(query,con=conn)

ids=cur.execute("select distinct id from {}".format(query_word))
id1=cur.fetchall()

print("Getting unique tweets.")
def unique(tweet_id):
    unique_tweets=list()
    queue=set()
    for i in tweet_id:
        if i not in queue:
            try:
                tweet = api.get_status(i)
                unique_tweets.append(tweet)
                queue.add(i)
            except:
                continue
    return unique_tweets

with concurrent.futures.ThreadPoolExecutor(8) as executor:
    future = executor.submit(unique, id1)
    unique_value = future.result()

print("--- %s seconds ---" % (time.time() - start_time))

    
print("Getting replies.")
def replies(tweets):
    li=list()
    queue=set()
    try: 
        for j in tweets:
            if j not in queue:
                if 'hiranandani' not in (j.user.screen_name).lower():
                    reply=api.search(q=j.user.screen_name,since_id=j.id,count=10000)
                    print("For User: ",j.user.screen_name)
                    for i in reply:
                        if i.in_reply_to_status_id==j.id:
                            li.append(i.user.screen_name)                
                            print(i.user.screen_name)
                            print("\n")           
                    queue.add(j)                        
    except Exception as e:
        print(e)
    return li




with concurrent.futures.ThreadPoolExecutor(8) as executor:
    future = executor.submit(replies, unique_value)
    return_value1 = future.result()

print("--- %s seconds ---" % (time.time() - start_time))


df1=pd.read_sql("select username from passive",con=conn)

u_name=list(df1['username'])

for i in return_value1:
    if i not in u_name:
        sql = "INSERT INTO {} (username,location) VALUES (%s, %s)".format(word)
        val = (i, return_value1[i])
        cur.execute(sql,val)

















