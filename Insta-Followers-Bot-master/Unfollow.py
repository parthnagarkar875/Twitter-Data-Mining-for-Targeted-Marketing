# import psycopg2 as pg2
# secret='helloparth'
# conn = pg2.connect(database='dvdrental',user='postgres',password=secret)
# cur=conn.cursor()
# cur.execute('SELECT * FROM payment')
# cur.fetchone()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd

chromedriver_path = '/usr/bin/chromedriver' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('')  #specify username
password = webdriver.find_element_by_name('password')
password.send_keys('')  #specify password
button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div > div > form > div > button')
button_login.click()
sleep(5)
notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN> div > div > div.mt3GC > button.aOOlW.HoLwm')
notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications
webdriver.get('https://www.instagram.com/jumpgoat199')
sleep(3)
now = webdriver.find_element_by_css_selector('li.Y8-fY:nth-child(3) > a:nth-child(1)')
now.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications
sleep(3)
# stri=str()
for i in range(1,300):
    sleep(15)
    stri='body > div.RnEpo.Yx5HN > div > div.isgrP > ul > div > li:nth-child('
    stri=stri+str(i)
    stri=stri+') > div > div.Pkbci > button'
    print(stri)
    print(i)
    now = webdriver.find_element_by_css_selector(stri)
    now.click()  # comment these last 2 lines out, if you don't get a pop up asking about notifications
    sleep(15)

    webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()


