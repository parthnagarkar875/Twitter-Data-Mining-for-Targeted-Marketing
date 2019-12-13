# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 11:22:22 2119

@author: Parth
"""
import psycopg2
import pickle
from textblob import TextBlob
import re
def clean_tweet(tweet): 
    ''' 
    Use simple regex statemnents to clean tweet text by removing links and special characters
    '''
    return ' '.join(re.sub("(@[A-Za-z1-9]+)|([^1-9A-Za-z \t]) \
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
    h=open('Hiranandani/tweets.pickle','rb')
except:
    print("Run the initial code first.")

stored_tweets=pickle.load(h)

conn = psycopg2.connect(database="Hiranandani", user = "postgres", password = "parth123n@#*", host = "127.1.1.1", port = "5432")

cur = conn.cursor()
        

      
for i in stored_tweets:
    text1=i.text                    
    text=clean_tweet(text1)
    sentiment = TextBlob(text).sentiment
    polar = sentiment.polarity
    
    sql = "INSERT INTO {} (id,tweet_text,created_at,location,polarity) VALUES \
                   (%s, %s, %s, %s, %s)".format('hiranandani')
    val = (i.id, i.text,i.created_at,i.user.location,polar)
    cur.execute(sql, val)            
    conn.commit()

conn.close()             
            
            

'''          
cur = conn.cursor()
cur.execute('''#INSERT INTO yogiadityanath()''')
#print("Table created successfully")

#'''