# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 13:08:49 2019

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
import pandas as pd
from pathlib import Path
import os
from math import ceil
import active
import concurrent.futures 
import tweepy
start_time = time.time()
consumer_key='rNrnFupaEqKt0eb7hjbdHKdWg'
consumer_secret= 'DTTMoQOrCBmngaXmOnFhrBjdjwtT54x0AbGvNwwuqyYNWwEvc7'
access_token='1002268050513575936-gGrQUmDiMyCxO2Y88lc3ojqNzbtLGm'
access_token_secret='G572YTe2S5TQTTaXhFvl1WyNopa8ilrkgWSlCXBZQwU4C'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)


#creating a separate folder for  each tweet
query='Hiranandani'
profile_file=query+'/Profiles.csv'
status_file=query+'/status.csv'
tweets_file=query+'/tweets.pickle'
passive_file=query+'/passive.csv'
#Opening the file containing previously stored tweets
try:
    h=open(tweets_file,'rb')
except:
    print("Run the initial code first.")

tweets=pickle.load(h)

print("Extracting URLs from the previously stored tweets.")
tweets_id=active.get_tweet_id(tweets)
tweet_id=set(tweets_id)

print("Getting unique tweets.")
def unique(tweet_id):
    unique_tweets=list()
    for i in tweet_id:
        tweet = api.get_status(i)
        unique_tweets.append(tweet)
    return unique_tweets

with concurrent.futures.ThreadPoolExecutor(8) as executor:
    future = executor.submit(unique, tweet_id)
    unique_value = future.result()



print("Getting replies.")
def replies(tweets):
    li=list()
    url1='https://twitter.com/'
    try: 
        for j in tweets:
            if 'hirandandani' not in (j.user.screen_name).lower():
                reply=api.search(q=j.user.screen_name,since_id=j.id,count=10000)
                print("For User: ",j.user.screen_name)
                url3=url1
                url3+=j.user.screen_name+'/status/'+str(j.id) 
                for i in reply:
                    if i.in_reply_to_status_id==j.id:
                        url2=url1
                        url2+=i.user.screen_name
                        li.append(url2)                
                        print(url2)
                    print("\n")           
    except Exception as e:
        print(e)
    return li




with concurrent.futures.ThreadPoolExecutor(8) as executor:
    future = executor.submit(replies, unique_value)
    return_value1 = future.result()

#like=set(return_value)
#print(len(like))

print("--- %s seconds ---" % (time.time() - start_time))

my_file = Path(passive_file)
if my_file.is_file():
    df=pd.read_csv(passive_file)
    urls2=df['list']
    urls3=list(urls2)
    urls3.extend(return_value1)
    set1=set(urls3)
    user_likes=list(set1)
    df={'list':pd.Series(user_likes)}
    finaldata=pd.DataFrame(df)
    finaldata.to_csv(passive_file,index=False,encoding='UTF-8')
else:
    df={'list':pd.Series(return_value1)}
    finaldata=pd.DataFrame(df)
    finaldata.to_csv(passive_file,index=False,encoding='UTF-8')
