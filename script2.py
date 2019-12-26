import concurrent.futures 
import pickle
import re
import smtplib
import dns.resolver
import time
import psycopg2

inputAddress='nagarkarparth@gmail.com'
fromAddress= 'abc@gmail.com'
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
 
addressToVerify= str(inputAddress)
 
match=re.match(regex,addressToVerify)
 
if match==None:
    print('Bad syntax')
    raise ValueError("Bad syntax")
    
splitAddress= addressToVerify.split('@')
domain=str(splitAddress[1])

records= dns.resolver.query(domain,'MX')
for i in records:    
    print("The records are: ",i.exchange)

mxRecord= records[0].exchange
print("The MX record is: ",mxRecord)

mxRecord= str(mxRecord)
 
server=smtplib.SMTP()
server.set_debuglevel(0)

server.connect(mxRecord)
server.helo(server.local_hostname)
server.mail(fromAddress)
code,message =server.rcpt(str(addressToVerify))
server.quit()

if code==250:
   # valid_emails.append(inputAddress)
    print(inputAddress)
    print("Success")
    #sql = "INSERT INTO 'emails' (valid) VALUES (%s)"
    #val = (str(addressToVerify))
    #mycursor.execute(sql, val)
    #conn.commit()
else:
    print("Bad")
