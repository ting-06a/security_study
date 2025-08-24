import requests
from lxml import etree
def get_data(page_number):
    url=f"https://www.butian.net/Shop/jd/cate/9987/p/{page_number}.html"
    headers={
    "Host":"www.butian.net",
    "Cookie":"UM_distinctid=196fd0b47d21a4b-0686f9b808ff77-26011f51-13f3c8-196fd0b47d32088; wzws_sessionid=gTdkZGVkYaBogaVKgmJhNTI0NIAyMjMuMTU1LjkuNzA=; PHPSESSID=i2amhmt58plm9bq0kk0sjj1610; _currentUrl_=%2FMessage; __btu__=46deb800b2460e3e77b85393a34ed93181e31245; __btc__=8ee8e7e339dced55b6ede98c4290b486b610e8fa; __btuc__=924a7bf4deed23df4a233a91570cea26183321cf"
    }
    res=requests.get(url,headers=headers)
    html=etree.HTML(res.text)
    i=1
    for item in html.xpath('//*[@id="numeral"]/ul')[0]:
        x=item.xpath(f'//*[@id="numeral"]/ul/li[{i}]/div[2]/p/a/text()')
        y=item.xpath(f'//*[@id="numeral"]/ul/li[{i}]/div[3]/p/span[1]/text()')
        z=item.xpath(f'//*[@id="numeral"]/ul/li[{i}]/div[3]/p/span[2]/text()')
        print(x[0]+"--->"+y[0]+"库币"+',已有'+str(z[0])+'人兑换')
        i=1+i

if __name__=='__main__':
    page_number=int(input("请输入想查看的页码："))
    if page_number < 1:
        print('页面必须大于0哦~')
    else:
        get_data(page_number)