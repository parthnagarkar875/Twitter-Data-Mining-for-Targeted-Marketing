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
#from nltk.corpus import stopwords 
#from nltk.tokenize import word_tokenize 
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


tweet=api.search('Messi',lang='en',count=100)

for i in tweet:
    
    


query_word='Hiranandani'
word=['passive']

#Opening the file containing previously stored tweets
try:
    h=open('Hiranandani/passive.pickle','rb')
except:
    print("Run the initial code first.")

users=pickle.load(h)

df=users.reset_index()
df=df.rename(columns = {"index": "Users", "Users":"Location"}) 


try:     
    conn = psycopg2.connect(database=query_word, user = "postgres", password = "parth123n@#*", host = "127.0.0.1", port = "5432")
except:
    print("Create database first")

        
cur=conn.cursor()
cur.execute('''CREATE TABLE {} (USERNAME TEXT, LOCATION TEXT);'''.format(word[0]))

conn.commit()
    
for j,i in df.iterrows():
    query='INSERT INTO {} (username, location) VALUES (%s, %s)'.format(word[0])
    val= (i['Users'],i['Location'])
    cur.execute(query,val)
    conn.commit()


conn.close()



st="Real estate issue. Make a video to help people what to do and help me also. I have purchased under-construction property from Mumbai's well-known builder. At time of purchase he said he has all permissions for 23 floors of building, I have purchased flat at 21st."
t=TextBlob(st)
print(t.subjectivity)
print(t.objectivity)

