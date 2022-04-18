import requests
import lxml
from bs4 import BeautifulSoup
import threading
import urljoin
import hashlib
import sys
from lxml import etree

requests.packages.urllib3.disable_warnings()

for pageid in range(1,84):
    url = 'https://www.free-powerpoint-templates-design.com/free-powerpoint-templates-design/page/%s/'%(pageid)


    res = requests.get(url, verify = False)
    html = etree.HTML(res.content )

    #print(htmldata)

    for i in [1,2,3] :
        for j in [1,2,3] :
            xpath_data = html.xpath('//*[@id="av_section_2"]/div[1]/div/div/div/div/div[1]/div[%s]/article[%s]/a/@href'%(i,j))
            print(xpath_data)



