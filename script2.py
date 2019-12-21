
import re
import smtplib
import dns.resolver

def verify(inputAddress):
    fromAddress= 'abc@gmail.com'
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

    addressToVerify= str(inputAddress)
    
    match=re.match(regex,addressToVerify)
    
    if match==None:
        print('Bad syntax')
        raise ValueError("Bad syntax")
        
    splitAddress= addressToVerify.split('@')
    domain=str(splitAddress[1])
    print("Domain:", domain)
    
    records= dns.resolver.query(domain,'MX')
    mxRecord= records[0].exchange
    mxRecord= str(mxRecord)
    
    server=smtplib.SMTP()
    server.set_debuglevel(0)
    
    server.connect(mxRecord)
    server.helo(server.local_hostname)
    server.mail(fromAddress)
    code,message =server.rcpt(str(addressToVerify))
    server.quit()
    
    if code==250:
        print("Success")
    else:
        print("Bad")
    

list1=['amarnani.lavin@gmail.com','miral.gandhi4@gmail.com','trollavin@gmail.com','nagarkarparth2201@gmail.com','nagarkarparth@yahoo.com','kala69iyer@gmail.com','nagarkarparth22@gmail.com','harsha_nihar@yahoo.co.in']


for i in list1:
    print(i)
    verify(i)
    
    
verify('parthn.agarkar199@gmail.com')