# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 16:23:32 2019

@author: Parth
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
import pickle

with open('emails.pickle', 'rb') as f:
    emails = pickle.load(f)



chromedriver_path = 'C:\Windows\chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
for i in emails:
    webdriver.get('https://verify-email.org/')
    sleep(3)
    
    
    email=webdriver.find_element_by_xpath(
                            '//*[@id="email"]')
    email.click()
    sleep(1)
    email.send_keys(i)
    sleep(3)
    
    robot=webdriver.find_element_by_xpath(
                            '//*[@id="verifyBtn"]')
    
    robot.click()
    sleep(5)
    
    username = webdriver.find_element_by_xpath('//*[@id="result-email"]').text
    l=username.split()
    if l[2]=='OK':
        print("yes")
    else:
        print("No")

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
import pickle
import socks
import socket

chromedriver_path = 'C:\Windows\chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.google.com/')
sleep(3)

box=webdriver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
box.click()
sleep(1)
email.send_keys('what is my ip')
sleep(3)

cli=webdriver.find_element_by_xpath(
                    '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')

cli.click()
sleep(5)















'''


