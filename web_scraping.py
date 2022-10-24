import requests
import urllib.request
import time
import json
from bs4 import BeautifulSoup

#J'ai pris comme exemple coordonnées gps suivants
lat_origin='34.033333'
lat_dest='33.9715904'
long_origin='-5.000000'
long_dest='-6.8498129'

url='https://api.distancematrix.ai/maps/api/distancematrix/json?origins='+lat_origin+','+long_origin+'&destinations='+lat_dest+','+long_dest+'&key=7yiVUavyBZ2Ph0hKvA9UzEaBa9PVI'
response=requests.get(url)
rsp=response.content
soup=BeautifulSoup(response.text,"html.parser")

for e in soup : 
    e=e.text 
    index = e.find("distance")
    res=e[index+19:].split()[0]
#res presente la distance par route voulu
print(res)
#e presente le resultat obtenu par la recherche sur le site
print(e)
