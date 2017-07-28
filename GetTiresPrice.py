from bs4 import BeautifulSoup
from urllib.request import urlopen
import xlrd
import csv
import sys
import io

TireSpliteList = []
TireList = []
PriceList = []
dicTirePrice={}

for i in range(1,10):
    html = urlopen("https://item.tuhu.com/Tires/"+str(i)+"/au1-o1.html#Products")
    bsobj = BeautifulSoup(html)
    namelist = bsobj.find_all("tr")
    # print(bsobj)
    for name in namelist:
        Tire = str.replace(
            str.replace(str.replace(name.find("td", {"class": "td2"}).find("a").get_text(), "  ", "").strip(), u'\xa0',
                        u' '), '\r', '').split("\n")[0]
        Price = str.replace(name.find("td", {"class": "td3"}).find("strong").get_text(), "¥", "")
        dicTirePrice[Tire] = Price

#print(dicTirePrice)
print ("111")
#C:/Users/H620974/Desktop/TW/test.csv
csvFile = open("C:/Users/H620974/Desktop/TW/test.csv", "w",newline='')
writer = csv.writer(csvFile)

for x1 in dicTirePrice.items():
    writer.writerow(x1)

csvFile.close()
