from os.path import basename
from urllib.parse import urlsplit, urlparse
from urllib.request import urlopen
import urllib.request
import ssl
import requests

ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()
requests.adapters.DEFAULT_RETRIES = 5  

def url2name(url):
    return basename(urlsplit(url)[2])

with open("Downloadurl2.txt", "r") as f: 
    try :
        while True:
            data = f.readline()
            if not data:
                break
            url = str(data).strip()
            path="PPTs/"+url2name(url)
            print(path)
            r=requests.get(url, verify = False)
            print("ok")
            with open(path,"wb") as ppt:
                ppt.write(r.content)
                ppt.close()

    finally :
        f.close()
