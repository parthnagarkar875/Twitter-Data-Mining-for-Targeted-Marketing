# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 15:10:47 2019

@author: Parth
"""
import active
import tweepy
import pickle
import mysql.connector

consumer_key='rNrnFupaEqKt0eb7hjbdHKdWg'
consumer_secret= 'DTTMoQOrCBmngaXmOnFhrBjdjwtT54x0AbGvNwwuqyYNWwEvc7'
access_token='1002268050513575936-gGrQUmDiMyCxO2Y88lc3ojqNzbtLGm'
access_token_secret='G572YTe2S5TQTTaXhFvl1WyNopa8ilrkgWSlCXBZQwU4C'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="parth123n@#*"
)

print(mydb) 
