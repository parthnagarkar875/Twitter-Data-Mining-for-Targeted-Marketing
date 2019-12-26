# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 11:37:29 2019

@author: Parth
"""

import GetOldTweets3 as got
from textblob import TextBlob
 
tweetCriteria = got.manager.TweetCriteria().setUsername("@N_Hiranandani")\
                                           .setMaxTweets(1000)
tweet = got.manager.TweetManager.getTweets(tweetCriteria)

nounlist=list()
for i in tweet:
    blob = TextBlob(i.text)
    for nouns in blob.noun_phrases:
        nounlist.append(nouns)
        

