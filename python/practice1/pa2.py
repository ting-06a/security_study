import requests
from lxml import etree

url="https://www.butian.net/Shop"
headers={"Host":"www.butian.net",
         "Cookie":"UM_distinctid=196fd0b47d21a4b-0686f9b808ff77-26011f51-13f3c8-196fd0b47d32088; wzws_sessionid=gTdkZGVkYaBogaVKgmJhNTI0NIAyMjMuMTU1LjkuNzA=; PHPSESSID=i2amhmt58plm9bq0kk0sjj1610; _currentUrl_=%2FMessage; __btu__=46deb800b2460e3e77b85393a34ed93181e31245; __btc__=8ee8e7e339dced55b6ede98c4290b486b610e8fa; __btuc__=924a7bf4deed23df4a233a91570cea26183321cf"
         }

res=requests.get(url,headers=headers)
html=etree.HTML(res.text)
content=html.xpath('//*[@id="numeral l_2"]/ul')[0]
i=1
for item in content:
    x=item.xpath(f'//*[@id="numeral l_1"]/ul/li[{i}]/div[2]/p/a/text()')
    print(x)
    i=i+1
