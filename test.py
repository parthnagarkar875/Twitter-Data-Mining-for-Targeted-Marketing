# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 10:57:45 2019

@author: Parth
"""
import facebook
import os
import json
import urllib
import pprint

'''
token='EAAmMobTZBYy8BAIXmKF7Lt9hXVsNUjwkgfPDfzi73q3i6SCZBvzXSFF8iN4n0CsZCzO2uaBAaduAJiYcZCBhz1UxZC7ZBvxDqS0lRCfqt6ZBeOd4E5vOIRrboZBc0JMkLlaujozG5F37vmuQjmHvHCaAikcT1Lz5Scy1tbyRfEdlZBAZDZD'
graph = facebook.GraphAPI(token)
events = graph.request('/search?q=Poetry&type=event&limit=10000')
'''


# get Facebook access token from environment variable
ACCESS_TOKEN = 'EAAmMobTZBYy8BAIXmKF7Lt9hXVsNUjwkgfPDfzi73q3i6SCZBvzXSFF8iN4n0CsZCzO2uaBAaduAJiYcZCBhz1UxZC7ZBvxDqS0lRCfqt6ZBeOd4E5vOIRrboZBc0JMkLlaujozG5F37vmuQjmHvHCaAikcT1Lz5Scy1tbyRfEdlZBAZDZD'

# build the URL for the API endpoint
host = "https://graph.facebook.com"
path = "/me"
params = urllib.parse.urlencode({"access_token": ACCESS_TOKEN})

url = "{host}{path}?{params}".format(host=host, path=path, params=params)

# open the URL and read the response
resp = urllib.request.urlopen(url).read()

# convert the returned JSON string to a Python datatype 
me = json.loads(resp)

# display the result
print(me)


