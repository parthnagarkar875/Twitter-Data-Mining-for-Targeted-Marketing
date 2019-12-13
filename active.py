# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:25:37 2019

@author: Parth
"""
import psycopg2
import os
import collections
import re
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import pickle 
import string
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from math import ceil
import tweepy

url_list=list()
username_list=list()
user_profile_list=list()
stored_tweets=list()
consumer_key='rNrnFupaEqKt0eb7hjbdHKdWg'
consumer_secret= 'DTTMoQOrCBmngaXmOnFhrBjdjwtT54x0AbGvNwwuqyYNWwEvc7'
access_token='1002268050513575936-gGrQUmDiMyCxO2Y88lc3ojqNzbtLGm'
access_token_secret='G572YTe2S5TQTTaXhFvl1WyNopa8ilrkgWSlCXBZQwU4C'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

def create_tweet_table(name):
    conn = psycopg2.connect(database="Hiranandani", user = "postgres", password = "parth123n@#*", host = "127.0.0.1", port = "5432")
    cur= conn.cursor()
    cur.execute('''CREATE TABLE {} (ID BIGINT, TWEET_TEXT TEXT, CREATED_AT TIMESTAMP, LOCATION TEXT,POLARITY INT);'''.format(name))
    conn.commit()
    conn.close()

def create_user_table():
    conn = psycopg2.connect(database="tp", user = "postgres", password = "parth123n@#*", host = "127.0.0.1", port = "5432")
    cur= conn.cursor()
    cur.execute('''CREATE TABLE ACTIVE (USERNAME TEXT, POST_URL TEXT);''')
    cur.execute('''CREATE TABLE PASSIVE (USERNAME TEXT);''')
    conn.commit()
    conn.close()


def create_project_directory(directory):
    if not os.path.exists(directory):
        print("Creating a new Directory...")
        os.makedirs(directory)

def write_data(stored_tweets,filename):
    tweet_pickle=open(filename,'wb')
    pickle.dump(stored_tweets,tweet_pickle)
    tweet_pickle.close()

def clean_tweet(tweet): 
    ''' 
    Use sumple regex statemnents to clean tweet text by removing links and special characters
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

def get_tweet_id(tweets):
    tweet_ids=[]
    for i in tweets:
        tweet_ids.append(i.id)
    return tweet_ids

def get_indi_url_data(obj):
    url='https://twitter.com/'
    url+=obj.user.screen_name+'/status/'+str(obj.id)
    return url

def get_url_data(tweets):
    user_profile_list=[]
    up_url='https://twitter.com/'
    username_list=[]
    url_list=[]
    url='https://twitter.com/'


    #Only stores the usernames that don't have hiranandani in them. 
    for i in tweets:
        url1=url
        up_url1=up_url
        if 'hiranandani' not in (i.user.screen_name).lower():
            url1+=i.user.screen_name+'/status/'
            url1+=str(i.id)
            up_url1+=i.user.screen_name
            url_list.append(url1)
            username_list.append(i.user.screen_name)
            user_profile_list.append(up_url1)
            
    return url_list, username_list,user_profile_list



def flatten(x):
    result = []
    for el in x:
        if hasattr(el, "__iter__") and not isinstance(el, str):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result


def get_authorization():

    info = {"consumer_key": "rNrnFupaEqKt0eb7hjbdHKdWg",
            "consumer_secret": "DTTMoQOrCBmngaXmOnFhrBjdjwtT54x0AbGvNwwuqyYNWwEvc7",
            "access_token": "1002268050513575936-gGrQUmDiMyCxO2Y88lc3ojqNzbtLGm",
            "access_secret": "G572YTe2S5TQTTaXhFvl1WyNopa8ilrkgWSlCXBZQwU4C"}

    auth = tweepy.OAuthHandler(info['consumer_key'], info['consumer_secret'])
    auth.set_access_token(info['access_token'], info['access_secret'])
    return auth

'''
def get_tweets(query, n):
    _max_queries = 100  # arbitrarily chosen value
    api = tweepy.API(get_authorization(),wait_on_rate_limit=True)
    tweets = tweet_batch = api.search(q=query, count=n)
    ct = 1
    while len(tweets) < n and ct < _max_queries:
        print(len(tweets))
        tweet_batch = api.search(q=query, 
                                 count=n - len(tweets),
                                 max_id=tweet_batch.max_id)
        tweet_batch1=list()
        
        for i in tweet_batch:
            if i.id not in tweet_ids:
                tweet_batch1.append(i)    
        tweets.extend(tweet_batch1)
        ct += 1
    return tweets
'''
def pull_tweets(query):
    max_tweets=10000

    searched_tweets = []
    last_id = -1
    while len(searched_tweets) < max_tweets:
        count = max_tweets - len(searched_tweets)
        try:
            new_tweets = api.search(q=query, count=count, max_id=str(last_id - 1))
            if not new_tweets:
                break
            for i in new_tweets:
                url=get_indi_url_data(i)
                if url not in url_list:
                    #searched_tweets.extend(new_tweets)
                    searched_tweets.append(i)
                    last_id = new_tweets[-1].id
        except tweepy.TweepError as e:
                        # depending on TweepError.code, one may want to retry or wait
        # to keep things simple, we will give up on an error
            break

    return searched_tweets

#Sentiments of the tweets are predicted to classify them as negative, psoitive or neutral. 
def analytics(stored_tweets):
    neut=0
    pos=0
    neg=0
    negative=list()
    

    
    for i in stored_tweets:
        text1 = deEmojify(str(i.text))     
        text=clean_tweet(text1)
        blob=TextBlob(text)
        if blob.polarity<0:
            neg+=1
            negative.append(i)
        elif blob.polarity>0:
            pos+=1
        else:
            neut+=1
    negp=(neg/len(stored_tweets))*100
    neutp=(neut/len(stored_tweets))*100
    posp=(pos/len(stored_tweets))*100
#Plotting of pie chart to give information related to the negative, postiive and neutral tweets
    labels = 'Positive',"Negative","Neutral"
    sizes = [posp,negp,neutp]
    m=max(posp,negp,neutp)
    if m==posp:
        explode=(0.1,0,0)
    elif m==negp:
        explode = (0, 0.1, 0)
    else:
        explode= (0, 0, 0.1)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

    return negative

#wordcloud
def wordcloud(negative):
   # hello=[]
    stop_words = set(stopwords.words('english')) 
    text_tweets=list()
    for i in negative:
        if 'hiranandani' not in (i.user.screen_name).lower():
            st=i.text    
            text_tweets.append(st)
            '''
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
    for i in text_tweets:
        if 'RT' in i:
            i.remove('RT')
    
    username_set=set(username_list)
    
    for j in text_tweets:
        l3 = [x for x in j if x not in username_set]
        hello.append(l3)    
    '''
    finaldata={'text':pd.Series(text_tweets)}
    df=pd.DataFrame(finaldata)

    
    content = ' '.join(df['text'])
    content = re.sub(r"http\S+", "", content)
    content = content.replace('RT ', ' ').replace('&amp;', 'and')
    content = re.sub('[^A-Za-z0-9]+', ' ', content)
    content = content.lower()

    tokenized_word = word_tokenize(content)
    stop_words=set(stopwords.words("english"))
    filtered_sent=[]
    for w in tokenized_word:
        if w not in stop_words:
            filtered_sent.append(w)
    fdist = FreqDist(filtered_sent)
    fd = pd.DataFrame(fdist.most_common(13), columns = ["Word","Frequency"]).drop([0]).reindex()
    
    return fd
    
    
    '''
    flat_tweets=list(flatten(hello))
    
    for i in flat_tweets:
        if i.isalpha()==False:
            flat_tweets.remove(i)
    
    counter=collections.Counter(flat_tweets)
     
    for word in list(counter):
        if str(word).isalpha()==False:
            del counter[word]
            
    c1=counter.most_common()
    return c1
    '''








