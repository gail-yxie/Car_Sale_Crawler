#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# login wechat using wechat_sender
import datetime  
from wxpy import *
bot = Bot(cache_path=True)
now = datetime.datetime.now()
news = 'Latest few posts from UT CSSA:'+  now.strftime('%Y.%m.%d-%H:%M:%S') + '\n'+'\n'


# get information from UT CSSA
import codecs
import requests
from bs4 import BeautifulSoup

url1 = 'http://www.utcssa.net/forum.php?mod=forumdisplay&fid=9'
url2 = 'http://www.utcssa.net/forum.php?mod=forumdisplay&fid=3&filter=typeid&typeid=13'

# first part
data = requests.get(url1).text
soup = BeautifulSoup(data,"lxml")
news = news + 'Car Sale Part \n'

count = 0
num = 1
for link in soup.find_all('a', attrs={"class":'s xst'}):
    count = count + 1
    if count >= 17:
        break         
    if count >= 12:
        new = '['+str(num)+'] '+link.getText()+'\n' +link.get('href') + '\n'
        num = num + 1 
        news = news + new

# second part
data = requests.get(url2).text
soup = BeautifulSoup(data,"lxml")
news = news + '\n Car Sale Mixed Part\n'

count = 0
for link in soup.find_all('a', attrs={"class":'s xst'}):   
    count = count + 1
    if count >= 4:
        break         
    if count >= 1:
        new = '['+str(num)+'] '+link.getText()+'\n' +link.get('href') + '\n'
        num = num + 1
        news = news + new
        
bot.file_helper.send(news)
        


    

    
    

