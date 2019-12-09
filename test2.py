# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 15:10:47 2019

@author: Parth
"""
import active
import tweepy
import pickle
import mysql.connector
import datetime
import pandas as pd
import settings

consumer_key='rNrnFupaEqKt0eb7hjbdHKdWg'
consumer_secret= 'DTTMoQOrCBmngaXmOnFhrBjdjwtT54x0AbGvNwwuqyYNWwEvc7'
access_token='1002268050513575936-gGrQUmDiMyCxO2Y88lc3ojqNzbtLGm'
access_token_secret='G572YTe2S5TQTTaXhFvl1WyNopa8ilrkgWSlCXBZQwU4C'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)


db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="parth123n@#*",
    database="instagramdb",
    charset = 'utf8'
 )
'''
time_now = datetime.datetime.utcnow()
time_10mins_before = datetime.timedelta(hours=0,minutes=10).strftime('%Y-%m-%d %H:%M:%S')
time_interval = time_now - time_10mins_before
'''

query = "SELECT id_str, text, created_at, polarity,user_location FROM {}".format(settings.TABLE_NAME)
df = pd.read_sql(query, con=db_connection)

df['created_at'] = pd.to_datetime(df['created_at'])

result = df.groupby([pd.Grouper(key='created_at', freq='2s'), 'polarity']).count().unstack(fill_value=0).stack().reset_index()

result = result.rename(columns={ "id_str": "Num of '{}' mentions".format(settings.TRACK_WORD),"created_at":"Time in UTC" })

time_series = result["Time in UTC"][result['polarity']==0].reset_index(drop=True)






