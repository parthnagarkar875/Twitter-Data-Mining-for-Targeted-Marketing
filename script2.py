# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 14:35:11 2019

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

cur=conn.cursor()
query = "SELECT * FROM {}".format(word[0]) 
df = pd.read_sql(query, con=conn)

url="https://twitter.com/"
list1=[]
for j,i in df.iterrows():
    if 'hiranandani' not in (i['username']).lower():
        url2=url
        url2+=i['username']+"/status/"+str(i.id)
        list1.append(url2)


li=set(list1)
print(len(li))