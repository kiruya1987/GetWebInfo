import requests
import lxml
from bs4 import BeautifulSoup
import threading
import urljoin
import hashlib
import sys
from lxml import etree

import urllib3
import re   
from bs4 import BeautifulSoup  
from distutils.filelist import findall  

requests.packages.urllib3.disable_warnings()


#//*[@id="wrap_all"]/div[2]/div/main/article/div[3]/div[1]/div[12]/a
#//*[@id="wrap_all"]/div[2]/div/main/article/div[3]/div[1]/div[5]/span/a

#//*[@id="wrap_all"]/div[2]/div/main/article/div[3]/div[1]/div[13]/span/a
#https://k4f4w9c2.stackpathcdn.com/wp-content/uploads/01_big_files_kim7/2018_best_ppt/City-of-Business-Man-PowerPoint-Template.pptx

with open("PPTurl.txt", "r") as f: 
    while True:
        data = f.readline()
        if not data:
            break
        url = data
        res = requests.get(url, verify = False)
        soup = BeautifulSoup(res.content,"html.parser")  
        for ppts in soup.find_all('a',href = re.compile('pptx')):
            print(ppts['href'])

# url = 'https://www.free-powerpoint-templates-design.com/merry-christmas-powerpoint-templates/'

# res = requests.get(url, verify = False)

# soup = BeautifulSoup(res.content,"html.parser")  

# for ppts in soup.find_all('a',href = re.compile('pptx')):
#     print(ppts['href'])
