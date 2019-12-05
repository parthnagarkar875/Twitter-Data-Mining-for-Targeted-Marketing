# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 14:15:51 2019

@author: Parth
"""
import io
import re
import sys
import pickle
import os
from math import ceil
import active
import tweepy
consumer_key='rNrnFupaEqKt0eb7hjbdHKdWg'
consumer_secret= 'DTTMoQOrCBmngaXmOnFhrBjdjwtT54x0AbGvNwwuqyYNWwEvc7'
access_token='1002268050513575936-gGrQUmDiMyCxO2Y88lc3ojqNzbtLGm'
access_token_secret='G572YTe2S5TQTTaXhFvl1WyNopa8ilrkgWSlCXBZQwU4C'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



'''
for i in reply:
    print(i.in_reply_to_status_id)
    url2=url1
    url2+=i.user.screen_name+'/status/'+str(i.id)
    print(url2)
'''

#creating a separate folder for  each tweet
query='ShameOnAnjana'
profile_file=query+'/Profiles.csv'
status_file=query+'/status.csv'
tweets_file=query+'/tweets.pickle'

#Opening the file containing previously stored tweets
try:
    h=open(tweets_file,'rb')
except:
    print("Run the initial code first.")

tweets=pickle.load(h)

status_and_replies=dict()

url1='https://twitter.com/'
try: 
    for j in tweets:
        reply=api.search(q=j.user.screen_name,since_id=j.id,count=10000)
        print("For User: ",j.user.screen_name)
        url3=url1
        url3+=j.user.screen_name+'/status/'+str(j.id) 
        li=list()
        for i in reply:
            if i.in_reply_to_status_id==j.id:
                url2=url1
                url2+=i.user.screen_name+'/status/'+str(i.id)
                
                li.append(url2)                
                print(url2)
            print("\n\n")
        status_and_replies[url3]=li
except Exception as e:
    print(e)





