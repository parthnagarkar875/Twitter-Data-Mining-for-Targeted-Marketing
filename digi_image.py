# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 11:37:29 2019

@author: Parth
"""
import nltk

from nltk import word_tokenize
import GetOldTweets3 as got
from textblob import TextBlob
 
tweetCriteria = got.manager.TweetCriteria().setUsername("@N_Hiranandani")\
                                           .setMaxTweets(1000)
tweet = got.manager.TweetManager.getTweets(tweetCriteria)

nounlist=list()
for i in tweet:
    try:
        text1 = active.deEmojify(i.text) 
#         print(text1)
        text=active.clean_tweet(text1)
        clean.append(text)
        blob = TextBlob(text)
        for nouns in blob.noun_phrases:
            nounlist.append(nouns)
    except:
        continue

from nltk.tag import StanfordNERTagger

st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')




import stanfordnlp
stanfordnlp.download('en')   # This downloads the English models for the neural pipeline
nlp = stanfordnlp.Pipeline() # This sets up a default neural pipeline in English
doc = nlp("Barack Obama was born in Hawaii.  He was elected president in 2008.")
doc.sentences[0].print_dependencies()