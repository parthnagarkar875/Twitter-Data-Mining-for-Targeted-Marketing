import requests
url = 'https://httpbin.org/ip'
proxies = {
    "http": 'http://209.90.63.108:80', 
    "https": 'http://209.90.63.108:80'
}
response = requests.get(url)
print(response.json())



import requests
import socks
import socket
#s = socks.socksocket() # Same API as socket.socket in the standard lib
socks.set_default_proxy(socks.SOCKS4, "197.234.13.36",4145)
socket.socket = socks.socksocket

#s.set_proxy(socks.SOCKS5, "168.232.152.99",4145)

url = 'https://httpbin.org/ip'
proxies = {
    "http": 'http://190.186.59.22:52335', 
    "https": 'http://190.186.59.22:52335'
}
response = requests.get(url)
print(response.json())


'''
from verifier import Verifier
# Use normal SMTP to connect to the server
normal_verifier = Verifier(source_addr='user@example.com') # No proxy
results = normal_verifier.verify('nagarkarparth@gmail.com')
# Use socks proxy to connect over SMTP
socks_verifier =  Verifier(
    source_addr='user@example.com',
    proxy_type='socks5',
    proxy_addr='socks5.your-proxy-provider.com',
    proxy_port=1080,
    proxy_username='funky-username',
    proxy_password='crazy-password'
)
results = socks_verifier.verify('myemail@example.com')

import urllib3
proxy = urllib3.ProxyManager('http://209.90.63.108:80')
h=proxy.request('GET', 'https://httpbin.org/ip')


import smtplib

sender = 'from@fromdomain.com'
receivers = ['nagarkaparth@yahoo.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print("Successfully sent email")
except Exception as e:
   print(e)
'''

