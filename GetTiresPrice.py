#coding:utf-8

from bs4 import BeautifulSoup
from urllib import urlopen
import xlrd
import csv
import io
import re
import sys
import MySQLdb
import time

reload(sys)
sys.setdefaultencoding('utf8')

TyreName=''
TyreBrand=''
TyrePrice=0
TyreRim = 0
TyreSize = 0
TyreR = 0
TyreSpeed = ''
TyreType=''
TyreCategory = ''
Buyers = 0
CreateTime =time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

UrlFile='test.txt'

conn= MySQLdb.connect(
        host='42.159.249.108',
        port = 53306,
        user='root',
        passwd='root',
        db ='BigDataSample',
        charset="utf8"
        )
cur = conn.cursor()

try:
    URLText = open(UrlFile,'w')
    for i in range(1,143):
        page = urlopen('https://item.tuhu.cn/Tires/' + str(i) + '/f0-o6.html')
        html = page.read()


        bsobj = BeautifulSoup(html, "html5lib")
        namelist = bsobj.find_all("tr")
        #print namelist

        for name in namelist:
            URLText.write(name.a['href'] + '\n')


    for line in open(UrlFile):
        page = urlopen(line)
        html = page.read()
        bsobj = BeautifulSoup(html, "html5lib")

        TyreName = bsobj.find("h1").find(text=re.compile("/"))

        TyrePrice = float(bsobj.find(class_="price").strong.string.replace("¥",'').replace(",",''))

        TyreBrand = bsobj.find(class_="properties").ul.li.text.replace("轮胎品牌：",'')

        TyreType = bsobj.find(class_="properties").ul.find_all("li")[1].text.replace("产品规格：",'')

        TyreSize = int(TyreType[0:3])
        TyreR = int(TyreType[4:6])
        TyreRim = int(TyreType[7:9])

        for item in bsobj.find(class_="properties").ul.find_all("li"):
            if "轮胎花纹：" in item.text :
                TyreCategory = item.text.replace("轮胎花纹：",'')
        print TyreCategory


        if bsobj.find(class_="person_shu")['data-quantity'] == '':
            Buyers =0
        else :
            Buyers =int(bsobj.find(class_="person_shu")['data-quantity'])

        sqli = "INSERT INTO TyreData VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(sqli, (TyreName, TyreBrand,TyrePrice, TyreRim,TyreSize,TyreR,TyreType,TyreCategory,Buyers,CreateTime))


        # print TyrePrice

        # break

finally:
    cur.close()
    conn.commit()
    conn.close()
    URLText.close()





