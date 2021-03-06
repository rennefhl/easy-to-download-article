# -*- coding: utf-8 -*-
"""
@author: Renne
"""

import urllib.request   
import re   
from bs4 import BeautifulSoup   
import time
from selenium import webdriver
import socket

socket.setdefaulttimeout(20)  

def crawler_download_withdriver():       
    webinput=(input('需要下载的文献的网站为(如果有多个网址请用空格隔开):'))
    weblist=webinput.split(" ")

    
    download_list=[]
    for i in range(len(weblist)):
        web2='https://sci-hub.tw//'+weblist[i]
        for x in range(5):          
            try:
                print('analysing:',web2)
                page = urllib.request.urlopen(web2)   
                contents = page.read()
                break
            except:
                print('Fail analysing')
        
        soup = BeautifulSoup(contents,'lxml')
        for ul in soup.find_all('ul'):
            dl=ul.find('li')  #此时dl的格式是bs4.element.Tag
    
        dlstr=''
        for x in dl:
            dlstr=dlstr+str(x) #转换成str
    
        pattern=re.compile('https.+download=true')   #匹配从https开始，到download=true结束的内容
        result=pattern.findall(dlstr)
        download_list=download_list+result
        print('Finish analysing')
        time.sleep(2)
               
        
    for url in download_list: # change here to download other files
        print('Beginning file download with Chrome: {n}'.format(n=url))
        driver.get(url) # get web
    print('Mission Complete')


if __name__ == '__main__':
    driver = webdriver.Chrome() #open chrome
    crawler_download_withdriver()