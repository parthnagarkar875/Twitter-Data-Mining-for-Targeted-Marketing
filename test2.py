# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 15:10:47 2019

@author: Parth
"""
import active
import tweepy
import pickle
consumer_key='rNrnFupaEqKt0eb7hjbdHKdWg'
consumer_secret= 'DTTMoQOrCBmngaXmOnFhrBjdjwtT54x0AbGvNwwuqyYNWwEvc7'
access_token='1002268050513575936-gGrQUmDiMyCxO2Y88lc3ojqNzbtLGm'
access_token_secret='G572YTe2S5TQTTaXhFvl1WyNopa8ilrkgWSlCXBZQwU4C'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

query='Hiranandani'
tweets_file=query+'/tweets.pickle'
passive_file=query+'/passive.csv'

#Opening the file containing previously stored tweets
try:
    h=open(tweets_file,'rb')
except:
    print("Run the initial code first.")

tweets=pickle.load(h)

locations=dict()

for i in tweets:
    locations[i.user.screen_name]=i.user.location








