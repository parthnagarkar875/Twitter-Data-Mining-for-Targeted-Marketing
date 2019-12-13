import pandas as pd
import psycopg2
import pickle


df=pd.read_csv('Hiranandani/passive.csv')
query_word='Hiranandani'
query="INSERT INTO passive(username,location) values(%s,%s)"

try:     
    conn = psycopg2.connect(database=query_word, user = "postgres", password = "parth123n@#*", host = "127.0.0.1", port = "5432")
except:
    print("Create database first")
    
cur=conn.cursor()
try:
    h=open('Hiranandani/tweets.pickle','rb')
except:
    print("Run the initial code first.")

tweets=pickle.load(h)
uname_loc=dict()

for i in tweets:
    uname_loc[i.user.screen_name]=i.user.location


for i in uname_loc:
    val=(i,uname_loc[i])
    cur.execute(query,val)
    
conn.commit()
conn.close()