# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 17:21:11 2019

@author: Parth
"""
import active
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



url_list=list()
username_list=list()
user_profile_list=list()
stored_tweets=list()


#creating a separate folder for  each tweet
query='Hiranandani'
profile_file=query+'/Profiles.csv'
status_file=query+'/status.csv'
tweets_file=query+'/tweets.pickle'
active.create_project_directory(query)

#Pulling and storing tweets
searched_tweets=active.pull_tweets(query)
active.write_data(searched_tweets,tweets_file)
url_list1, username_list1,user_profile_list1=active.get_url_data(searched_tweets)
user_profile_list.extend(user_profile_list1)

#Getting the frequency of Users
counter=collections.Counter(username_list1)

#Storing the unique profile urls
set1=set(user_profile_list)
user_profile_final=list(set1)
d={'Profile':pd.Series(user_profile_final)}
finaldata=pd.DataFrame(d)
finaldata.to_csv(profile_file,index=False,encoding='UTF-8')

#Storing the unique status urls
url_set=set(url_list1)
url_list_final=list(url_set)
df={'Posts URL':pd.Series(url_list_final)}
finaldata=pd.DataFrame(df)
finaldata.to_csv(status_file,index=False,encoding='UTF-8')


#Analysis of negative tweets
neg=active.analytics(searched_tweets)
word=active.wordcloud(neg)

