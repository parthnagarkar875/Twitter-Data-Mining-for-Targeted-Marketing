# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 12:47:44 2019

@author: Parth
"""
import active
import collections
from collections import Counter
import pickle 
import string
import numpy as np
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from math import ceil
import tweepy
import psycopg2
import re

url_list=list()
username_list=list()
user_profile_list=list()
stored_tweets=list()

query='hiranandani'

try:     
    conn = psycopg2.connect(database='Hiranandani', user = "postgres", password = "parth123n@#*", host = "127.0.0.1", port = "5432")
except:
    print("Create database first")
        


active.create_tweet_table(query)
#active.create_user_table()
















