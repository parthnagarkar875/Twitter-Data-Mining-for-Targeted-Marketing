# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 10:57:45 2019

@author: Parth
"""
import facebook
token='EAAmMobTZBYy8BAIXmKF7Lt9hXVsNUjwkgfPDfzi73q3i6SCZBvzXSFF8iN4n0CsZCzO2uaBAaduAJiYcZCBhz1UxZC7ZBvxDqS0lRCfqt6ZBeOd4E5vOIRrboZBc0JMkLlaujozG5F37vmuQjmHvHCaAikcT1Lz5Scy1tbyRfEdlZBAZDZD'
graph = facebook.GraphAPI(access_token=token)
events = graph.request('/search?q=Poetry&type=event&limit=10000')

