# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:19:19 2019

@author: Parth
"""

import settings
import mysql.connector
import pandas as pd
import time
import itertools
import math

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
#%matplotlib inline
import plotly.express as px
import datetime
from IPython.display import clear_output

import plotly.offline as py
import plotly.graph_objs as go
from plotly.subplots import make_subplots
py.init_notebook_mode()
    
import re
import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

while True:
    clear_output()
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="parth123n@#*",
        database="instagramdb",
        charset = 'utf8'
    )
    # Load data from MySQL
    timenow = (datetime.datetime.utcnow() - datetime.timedelta(hours=0, minutes=20)).strftime('%Y-%m-%d %H:%M:%S')
    query = "SELECT id_str, text, created_at, polarity, user_location FROM {} WHERE created_at >= '{}' " \
                     .format(settings.TABLE_NAME, timenow)
    df = pd.read_sql(query, con=db_connection)
    # UTC for date time at default
    df['created_at'] = pd.to_datetime(df['created_at'])

    fig = make_subplots(
        rows=2, cols=2,
        column_widths=[1, 0.4],
        row_heights=[0.6, 0.4],
        specs=[[{"type": "scatter", "rowspan": 2}, {"type": "choropleth"}],
               [            None                    , {"type": "bar"}]]
        )

    
    
    
    
    '''
    Plot the Line Chart
    
    # Clean and transform data to enable time series
    result = df.groupby([pd.Grouper(key='created_at', freq='2s'), 'polarity']).count().unstack(fill_value=0).stack().reset_index()
    result = result.rename(columns={"id_str": "Num of '{}' mentions".format(settings.TRACK_WORDS), "created_at":"Time in UTC"})  
    time_series = result["Time in UTC"][result['polarity']==0].reset_index(drop=True)
    fig.add_trace(go.Scatter(
        x=time_series,
        y=result["Num of '{}' mentions".format(settings.TRACK_WORDS)][result['polarity']==0].reset_index(drop=True),
        name="Neural",
        opacity=0.8), row=1, col=1)   
    fig.add_trace(go.Scatter(
        x=time_series,
        y=result["Num of '{}' mentions".format(settings.TRACK_WORDS)][result['polarity']==-1].reset_index(drop=True),
        name="Negative",
        opacity=0.8), row=1, col=1)
    fig.add_trace(go.Scatter(
        x=time_series,
        y=result["Num of '{}' mentions".format(settings.TRACK_WORDS)][result['polarity']==1].reset_index(drop=True),
        name="Positive",
        opacity=0.8), row=1, col=1)
    
    fig.show()
    
    time.sleep(60)
    '''
    
    


from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import tweepy
import settings  
import re
import tweepy
import mysql.connector
import pandas as pd
from textblob import TextBlob

consumer_key='rNrnFupaEqKt0eb7hjbdHKdWg'
consumer_secret= 'DTTMoQOrCBmngaXmOnFhrBjdjwtT54x0AbGvNwwuqyYNWwEvc7'
access_token='1002268050513575936-gGrQUmDiMyCxO2Y88lc3ojqNzbtLGm'
access_token_secret='G572YTe2S5TQTTaXhFvl1WyNopa8ilrkgWSlCXBZQwU4C'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

tweets=api.search('Messi',lang='en',count=100)

text_tweets=list()

stop_words=set(stopwords.words("english"))
for i in tweets:
    st=i.text
    word_tokens = word_tokenize(st)
    filtered_sentence = []   
    removetable = str.maketrans('', '', '@#%')
    out_list = [s.translate(removetable) for s in word_tokens]
    for w in out_list: 
        if w not in stop_words: 
            filtered_sentence.append(w) 
    x = [''.join(c for c in s if c not in string.punctuation) for s in filtered_sentence]
    x = [s for s in x if s]
    text_tweets.append(x)    


li=list()
for i in tweets:
    li.append(i.text)
finaldata={'text':pd.Series(li)}
df=pd.DataFrame(finaldata)

content = ' '.join(df['text'])
content = re.sub(r"http\S+", "", content)
content = content.replace('RT ', ' ').replace('&amp;', 'and')
content = re.sub('[^A-Za-z0-9]+', ' ', content)
content = content.lower()

tokenized_word = word_tokenize(content)

filtered_sent=[]
for w in tokenized_word:
    if w not in stop_words:
        filtered_sent.append(w)








