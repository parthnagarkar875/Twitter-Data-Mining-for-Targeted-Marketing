
import re
import smtplib
import dns.resolver

def verify(inputAddress):
    fromAddress= 'abc@gmail.com'
    regex='^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
    
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
    



for i in list1:
    print(i)
    verify(i)
    