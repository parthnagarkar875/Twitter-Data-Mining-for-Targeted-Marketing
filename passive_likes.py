# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 14:15:51 2019

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

#Opening the file containing previously stored tweets
try:
    h=open(tweets_file,'rb')
except:
    print("Run the initial code first.")

tweets=pickle.load(h)



def get_user_ids_of_post_likes(post_id):
    try:
        json_data = urllib.request.urlopen('https://twitter.com/i/activity/favorited_popup?id=' + str(post_id)).read()
        json_data = json_data.decode('utf-8')
        found_ids = re.findall(r'data-user-id=\\"+\d+', json_data)
        unique_ids = list(set([re.findall(r'\d+', match)[0] for match in found_ids]))
        return unique_ids

    except urllib.request.HTTPError:
        return False

def get_uname(tweets):
    set1=set()
    likers=list()
    for i in tweets: 
        if i.id not in set1:
            if 'hiranandani' not in (i.user.screen_name).lower():
                id1=get_user_ids_of_post_likes(i.id)
                likers.extend(id1)        
                set1.add(i.id)
    set2=set()
    likers_uname=list()
    for i in likers:   
        if i not in set2:
            u=api.get_user(i)
            likers_uname.append(u.screen_name)            
            set2.add(i)



    return likers_uname



with concurrent.futures.ThreadPoolExecutor(8) as executor:
    future = executor.submit(get_uname, tweets)
    return_value = future.result()

#like=set(return_value)
#print(len(like))


print("--- %s seconds ---" % (time.time() - start_time))







