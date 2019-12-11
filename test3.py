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
import datetime

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="parth123n@#*",
    database="instagramdb",
    charset = 'utf8'
)


timenow = (datetime.datetime.utcnow() - datetime.timedelta(hours=0, minutes=30)).strftime('%Y-%m-%d %H:%M:%S')
query = "SELECT id_str, text, created_at, polarity, user_location FROM {}" \
                 .format(settings.TABLE_NAME)
df = pd.read_sql(query, con=db_connection)

for i in df['text'][:20]:
    t=TextBlob(i).sentiment
    print(t.polarity)

