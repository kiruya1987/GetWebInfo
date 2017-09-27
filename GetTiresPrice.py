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
i=0
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


def IsNum(Num):
    try:
        int(Num)
        return True
    except:
        return False

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

        if IsNum(TyreType[0:3]):
            TyreSize = int(TyreType[0:3])
        else:
            TyreSize=0

        if IsNum(TyreType[4:6]):
            TyreR = int(TyreType[4:6])
        else:
            TyreR = 0

        if IsNum(TyreType[7:9]):
            TyreRim = int(TyreType[7:9])
        else:
            TyreRim=0

        for item in bsobj.find(class_="properties").ul.find_all("li"):
            if "轮胎花纹：" in item.text :
                TyreCategory = item.text.replace("轮胎花纹：",'')



        if bsobj.find(class_="person_shu")['data-quantity'] == '':
            Buyers =0
        else :
            Buyers =int(bsobj.find(class_="person_shu")['data-quantity'])

        sqli = "INSERT INTO TyreData VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        if TyreName != '' :
            cur.execute(sqli, (TyreName, TyreBrand,TyrePrice, TyreRim,TyreSize,TyreR,TyreType,TyreCategory,Buyers,CreateTime))

        i=i+1
        print TyreName,i
        # print TyrePrice

        # break

finally:
    cur.close()
    conn.commit()
    conn.close()
    URLText.close()




