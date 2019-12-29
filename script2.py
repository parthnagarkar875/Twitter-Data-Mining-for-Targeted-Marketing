import os
from nltk.tag import StanfordNERTagger
import pandas as pd
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import GetOldTweets3 as got
import active
from textblob import TextBlob

tweetCriteria = got.manager.TweetCriteria().setUsername("@N_Hiranandani").setMaxTweets(10)
tweet = got.manager.TweetManager.getTweets(tweetCriteria)
nounlist=list()
clean=list()
for i in tweet:
    try:
        text1 = active.deEmojify(i.text) 
        text=active.clean_tweet(text1)
        clean.append(text)
        blob = TextBlob(text)
        for nouns in blob.noun_phrases:
            nounlist.append(nouns)
    except:
        continue
li1=pd.Series(nounlist)

active.wordcloud(li1)

#st = StanfordNERTagger('C:/Users/Parth/Contacts/Downloads/stanford-ner-2015-04-20/stanford-corenlp-full-2018-10-05/stanford-corenlp-full-2018-10-05/edu/stanford/nlp/models/ner/english.all.3class.distsim.crf.ser.gz','C:/Users/Parth/Contacts/Downloads/stanford-ner-2015-04-20/stanford-ner.jar',encoding='utf-8')

#Set environmental variables programmatically.
#Set the classpath to the path where the jar file is located
os.environ['CLASSPATH'] = "C:/Users/Parth/Contacts/Downloads/stanford-ner-2015-04-20/stanford-ner.jar"

#Set the Stanford models to the path where the models are stored
os.environ['STANFORD_MODELS'] = 'C:/Users/Parth/Contacts/Downloads/stanford-ner-2015-04-20/stanford-corenlp-full-2018-10-05/stanford-corenlp-full-2018-10-05/edu/stanford/nlp/models/ner'

#Set the java jdk path

java_path = "C:/Program Files/Java/jdk1.8.0_131/bin/java.exe"
os.environ['JAVAHOME'] = java_path


#Set the path to the model that you would like to use
stanford_classifier  =  'C:/Users/Parth/Contacts/Downloads/stanford-ner-2015-04-20/stanford-corenlp-full-2018-10-05/stanford-corenlp-full-2018-10-05/edu/stanford/nlp/models/ner/english.all.3class.distsim.crf.ser.gz'

#Build NER tagger object
st = StanfordNERTagger(stanford_classifier)
text='While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.'
tokenized_text = word_tokenize(text)
classified_text = st.tag(tokenized_text)

is_noun = lambda pos: pos[:3] == 'ORG'
nouns = [word for (word, pos) in classified_text if is_noun(pos)] 
print(nouns)
noun=pd.Series(nouns)
active.wordcloud(noun)