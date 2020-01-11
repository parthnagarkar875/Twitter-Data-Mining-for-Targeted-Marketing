# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 10:49:48 2020

@author: Parth
"""
# =============================================================================
# from time import sleep
# import ezgmail
# import os
# os.chdir('C:/Users/Parth/Internship')
# #ezgmail.init()
# 
# ezgmail.send('nagarkarparth22@gmail.com', 'Wake Up', 'Wakeeee up')
# 
# ezgmail.send('nagarkarparth22@gmail.com', 'Wake Up', 'Wakeeee up')
# ezgmail.send('nagarkarparth22@gmail.com', 'Wake Up', 'Wakeeee up')
# ezgmail.send('nagarkarparth22@gmail.com', 'Wake Up', 'Wakeeee up')
# ezgmail.send('nagarkarparth22@gmail.com', 'Wake Up', 'Wakeeee up')
# ezgmail.send('nagarkarparth22@gmail.com', 'Wake Up', 'Wakeeee up')
# ezgmail.send('nagarkarparth22@gmail.com', 'Wake Up', 'Wakeeee up')
# ezgmail.send('nagarkarparth22@gmail.com', 'Wake Up', 'Wakeeee up')
# ezgmail.send('nagarkarparth22@gmail.com', 'Wake Up', 'Wakeeee up')
# 
# =============================================================================
# =============================================================================
# from twilio.rest import Client
# accountSID = 'AC35ca651cec70a1dc7aadffa43d365d0b'
# authToken  = 'b7de1bbd1e9a75784f311712deff5710'
# twilioCli = Client(accountSID, authToken)
# myTwilioNumber = '+12053199665'
# myCellPhone = '+919930426913'
# message = twilioCli.messages.create(body='Mr. Watson - Come here - I want to see you.', from_=myTwilioNumber, to=myCellPhone)
# 
# =============================================================================




# =============================================================================
# import requests
# import json
# 
# URL = 'https://www.sms4india.com/api/v1/sendCampaign'
# 
# # get request
# def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
#   req_params = {
#   'apikey':apiKey,
#   'secret':secretKey,
#   'usetype':useType,
#   'phone': phoneNo,
#   'message':textMessage,
#   'senderid':senderId
#   }
#   return requests.post(reqUrl, req_params)
# 
# # get response
# response = sendPostRequest(URL, 'E869BX0K8NTXIZCAPTZK8MJ6JLGT49ZF', '4KPW4G13VRHHHTTI', 'prod', '09930426913', 'active-sender-id', 'message-text' )
# """
#   Note:-
#     you must provide apikey, secretkey, usetype, mobile, senderid and message values
#     and then requst to api
# """
# # print response if you want
# print response.text
# 
# =============================================================================




# =============================================================================
# import requests
# import json
# 
# URL = 'https://www.sms4india.com/api/v1/sendCampaign'
# 
# # get request
# def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
#   req_params = {
#   'apikey':apiKey,
#   'secret':secretKey,
#   'usetype':useType,
#   'phone': phoneNo,
#   'message':textMessage,
#   'senderid':senderId
#   }
#   return requests.post(reqUrl, req_params)
# 
# # get response
# response = sendPostRequest(URL, '77KLNJ3P3XL3X6B6ZH4U9084WCL58NNK', '5PNKRM4ZDQ9WTQKV', 'prod', '09930426913', '+919930199203', 'Wake up' )
# """
#   Note:-
#     you must provide apikey, secretkey, usetype, mobile, senderid and message values
#     and then requst to api
# """
# # print response if you want
# print(response.text)
# =============================================================================




import multiprocessing as mp
print("Number of processors: ", mp.cpu_count())










