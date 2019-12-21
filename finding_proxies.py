# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 14:18:11 2019

@author: Parth
"""
import requests

proxy1 = {
    'http': 'socks5://user:pass@91.108.156.198:4145',
    'https': 'socks5://user:pass@91.108.156.198:4145',
}


#r = requests.get('https://api.getproxylist.com/proxy')
#print(r.json())

r = requests.get('https://httpbin.org/ip',proxies=proxy1)