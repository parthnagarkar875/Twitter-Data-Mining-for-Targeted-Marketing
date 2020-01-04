# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 10:49:48 2020

@author: Parth
"""

# =============================================================================
# import ezgmail
# import os
# os.chdir('C:/Users/Parth/Internship')
# #ezgmail.init()
# 
# ezgmail.send('nagarkarparth@gmail.com', 'Hello', 'Hello world')
# =============================================================================


from twilio.rest import Client
accountSID = 'AC35ca651cec70a1dc7aadffa43d365d0b'
authToken  = 'b7de1bbd1e9a75784f311712deff5710'
twilioCli = Client(accountSID, authToken)
myTwilioNumber = '+12053199665'
myCellPhone = '+919930426913'
message = twilioCli.messages.create(body='Mr. Watson - Come here - I want to see you.', from_=myTwilioNumber, to=myCellPhone)
