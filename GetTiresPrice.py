#coding:utf-8

from bs4 import BeautifulSoup
from urllib import urlopen
import xlrd
import csv
import sys
import io


TireName=''
UrlFile='C:/Users/H620974/Desktop/test.txt'


try:
    URLText = open(UrlFile,'w')
    for i in range(141,143):
        page = urlopen('https://item.tuhu.cn/Tires/' + str(i) + '/f0-o5.html')
        html = page.read()


        bsobj = BeautifulSoup(html, "html5lib")
        namelist = bsobj.find_all("tr")
        #print namelist

        for name in namelist:
            URLText.write(name.a['href'] + '\n')
        URLText.close()

    for line in open(UrlFile):
        page = urlopen(line)
        html = page.read()
        bsobj = BeautifulSoup(html, "html5lib")
        TireName = bsobj.find("h1").string

        print TireName

finally:
    pass





