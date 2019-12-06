# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 13:08:49 2019

@author: Parth
"""
import time
import threading
import urllib
import re
import io
import re
import sys
from time import sleep
import pickle
import os
from math import ceil
import active
import concurrent.futures 
import tweepy
start_time = time.time()
consumer_key='rNrnFupaEqKt0eb7hjbdHKdWg'
consumer_secret= 'DTTMoQOrCBmngaXmOnFhrBjdjwtT54x0AbGvNwwuqyYNWwEvc7'
access_token='1002268050513575936-gGrQUmDiMyCxO2Y88lc3ojqNzbtLGm'
access_token_secret='G572YTe2S5TQTTaXhFvl1WyNopa8ilrkgWSlCXBZQwU4C'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)


#creating a separate folder for  each tweet
query='Hiranandani'
profile_file=query+'/Profiles.csv'
status_file=query+'/status.csv'
tweets_file=query+'/tweets.pickle'

#Opening the file containing previously stored tweets
try:
    h=open(tweets_file,'rb')
except:
    print("Run the initial code first.")

tweets=pickle.load(h)




def replies(tweets):
    li=list()
    url1='https://twitter.com/'
    try: 
        for j in tweets:
            if 'hirandandani' not in (j.user.screen_name).lower():
                reply=api.search(q=j.user.screen_name,since_id=j.id,count=10000)
                print("For User: ",j.user.screen_name)
                url3=url1
                url3+=j.user.screen_name+'/status/'+str(j.id) 
                for i in reply:
                    if i.in_reply_to_status_id==j.id:
                        url2=url1
                        url2+=i.user.screen_name
                        li.append(url2)                
                        print(url2)
                    print("\n")           
    except Exception as e:
        print(e)
    return li




with concurrent.futures.ThreadPoolExecutor(8) as executor:
    future = executor.submit(replies, tweets)
    return_value = future.result()

#like=set(return_value)
#print(len(like))



print("--- %s seconds ---" % (time.time() - start_time))

df=pd.read_csv(profile_file)
urls=list(df['Profile'])

#Only extend/add new profile URL if they are already not present
for i in user_profile_list:
    if i not in urls:
        urls.extend(i)


urls1=set(urls)
urls_final=list(urls1)
d={'Profile':pd.Series(urls_final)}
finaldata=pd.DataFrame(d)
finaldata.to_csv(profile_file,index=False,encoding='UTF-8')











