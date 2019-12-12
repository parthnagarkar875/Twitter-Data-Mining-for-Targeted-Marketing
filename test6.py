# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 10:57:45 2019

@author: Parth
"""
import tweepy
import re
import mysql.connector
import pandas as pd
from textblob import TextBlob
TRACK_WORDS = 'hiranandani'
TABLE_NAME = "hiranandani"

TABLE_ATTRIBUTES = "id_str VARCHAR(255), created_at DATETIME, text VARCHAR(255), \
            polarity FLOAT, subjectivity INT, user_created_at VARCHAR(255), user_location VARCHAR(255), \
            user_description VARCHAR(255), user_followers_count INT, longitude DOUBLE, latitude DOUBLE, \
            retweet_count INT, favorite_count INT"


consumer_key='rNrnFupaEqKt0eb7hjbdHKdWg'
consumer_secret= 'DTTMoQOrCBmngaXmOnFhrBjdjwtT54x0AbGvNwwuqyYNWwEvc7'
access_token='1002268050513575936-gGrQUmDiMyCxO2Y88lc3ojqNzbtLGm'
access_token_secret='G572YTe2S5TQTTaXhFvl1WyNopa8ilrkgWSlCXBZQwU4C'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)


def clean_tweet(tweet): 
    ''' 
    Use simple regex statemnents to clean tweet text by removing links and special characters
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) \
                                |(\w+:\/\/\S+)", " ", tweet).split()) 
def deEmojify(text):
    '''
    Strip all non-ASCII characters to remove emoji characters
    '''
    if text:
        return text.encode('ascii', 'ignore').decode('ascii')
    else:
        return None



class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if status.retweeted:
            return True

        id_str = status.id_str
        created_at = status.created_at
        text1 = deEmojify(status.text)     
        text=clean_tweet(text1)
        sentiment = TextBlob(text).sentiment
        polarity = sentiment.polarity
        subjectivity = sentiment.subjectivity
            
        user_created_at = status.user.created_at
        user_location = deEmojify(status.user.location)
        user_description = deEmojify(status.user.description)
        user_followers_count =status.user.followers_count
        longitude = None
        latitude = None
        if status.coordinates:
            longitude = status.coordinates['coordinates'][0]
            latitude = status.coordinates['coordinates'][1]
                
        retweet_count = status.retweet_count
        favorite_count = status.favorite_count     # Quick check contents in tweets
        print(status.text)
        #print("Long: {}, Lati: {}".format(longitude, latitude))
            
        # Store all data in MySQL
        if mydb.is_connected():
            mycursor = mydb.cursor()
            sql = "INSERT INTO {} (id_str,created_at,text,polarity,\
                   subjectivity, user_created_at, user_location,\
                   user_description, user_followers_count, longitude,\
                   latitude, retweet_count, favorite_count) VALUES \
                   (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(TABLE_NAME)
            val = (id_str, created_at, text, polarity, subjectivity, user_created_at, user_location, \
                user_description, user_followers_count, longitude, latitude, retweet_count, favorite_count)
            mycursor.execute(sql, val)
            mydb.commit()
            mycursor.close()
        
        
        
        
        
    def on_error(self, status_code):
        '''
        Since Twitter API has rate limits, 
        stop srcraping data as it exceed to the thresold.
        '''
        if status_code == 420:
            # return False to disconnect the stream
            return False




mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="parth123n@#*",
    database="hiranandanidb",
    charset = 'utf8'
)
if mydb.is_connected():
    '''
    Check if this table exits. If not, then create a new one.
    '''
    mycursor = mydb.cursor()
    mycursor.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(TABLE_NAME))
    if mycursor.fetchone()[0] != 1:
        mycursor.execute("CREATE TABLE {} ({})".format(TABLE_NAME, TABLE_ATTRIBUTES))
        mydb.commit()
    mycursor.close()
    
try:
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)
    myStream.filter(languages=["en"], track = TRACK_WORDS)
    
    mydb.close()
except Exception as e:
    print(e)



import pickle
import mysql.connector
import pandas as pd
import time
import itertools
import math
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import plotly.express as px
import datetime
from IPython.display import clear_output
import plotly.offline as py
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import tweepy
import numpy as np
import re
import nltk
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob
consumer_key='rNrnFupaEqKt0eb7hjbdHKdWg'
consumer_secret= 'DTTMoQOrCBmngaXmOnFhrBjdjwtT54x0AbGvNwwuqyYNWwEvc7'
access_token='1002268050513575936-gGrQUmDiMyCxO2Y88lc3ojqNzbtLGm'
access_token_secret='G572YTe2S5TQTTaXhFvl1WyNopa8ilrkgWSlCXBZQwU4C'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)
tweets_file='Hiranandani/tweets.pickle'


def clean_tweet(tweet): 
    ''' 
    Use simple regex statemnents to clean tweet text by removing links and special characters
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) \
                                |(\w+:\/\/\S+)", " ", tweet).split()) 
def deEmojify(text):
    '''
    Strip all non-ASCII characters to remove emoji characters
    '''
    if text:
        return text.encode('ascii', 'ignore').decode('ascii')
    else:
        return None


try:
    h=open(tweets_file,'rb')
except:
    print("Run the initial code first.")

tweets=pickle.load(h)

TABLE_NAME='hiranandani'

created_at=[]
sentiments=[]
text2=[]
for i in tweets:
    created_at.append(i.created_at)
    text2.append(i.text)
    text1 = deEmojify(i.text)     
    text=clean_tweet(text1)
    sentiment = TextBlob(text).sentiment
    polarity = sentiment.polarity
    sentiments.append(polarity)


df={'Time':pd.Series(created_at),'Text':pd.Series(text2),'Sentiment':pd.Series(sentiments)}
finaldata=pd.DataFrame(df)

sen=df['Sentiment']
sen1=list(sen)
sen2=list()
for i in sen1:
    sen2.append(round(i))


