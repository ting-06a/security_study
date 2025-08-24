import requests
import time,random

id=input("请输入要查询的企业对应的id：")
size=int(input("请输入单页读取的条数："))

url_list = []   #用于存储爬取的主域名

url = f"https://capi.tianyancha.com/cloud-intellectual-property/intellectualProperty/icpRecordList?_=1756029159803&id={id}&pageSize={size}&pageNum=2"

headers = {
    "Host": "capi.tianyancha.com",
    "X-Auth-Token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTI3Mzk5NjAyOSIsImlhdCI6MTc1NjAyODIwMSwiZXhwIjoxNzU4NjIwMjAxfQ.nQgouVGqNQjPlf8_-Qj07321HcP8A_QJ1ZW7upIlbUgl7PFCBJW7LgWmZ9GVDQ-VzfkuFqCg-S0jonSexn45GQ",
    "Version": "TYC-Web"
}

res = requests.get(url, headers=headers)
print(res.json())
number=(res.json())["data"]["itemTotal"]  #获取该企业有多少条主域名
upper=number//size+1  #根据总条数整除要求每页读取的条数再加一，得一共应该读几页
print(f"共需读取{upper}页，每页读取{size}条")

def get_info(pageNumber):
    get_url =f"https://capi.tianyancha.com/cloud-intellectual-property/intellectualProperty/icpRecordList?_=1756029159803&id={id}&pageSize={size}&pageNum={pageNumber}"

    headers={
        "Host": "capi.tianyancha.com",
        "X-Auth-Token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTI3Mzk5NjAyOSIsImlhdCI6MTc1NjAyODIwMSwiZXhwIjoxNzU4NjIwMjAxfQ.nQgouVGqNQjPlf8_-Qj07321HcP8A_QJ1ZW7upIlbUgl7PFCBJW7LgWmZ9GVDQ-VzfkuFqCg-S0jonSexn45GQ",
        "Version":"TYC-Web"
    }

    res=requests.get(get_url,headers=headers)
    content=res.json()
    item= content["data"]["item"]
    for i in item:

        url_list.append(i['ym']+'\n')

for k in range(1,upper+1):
    delay=random.uniform(1,3)
    print(f"让我睡一会哈，等会就爬取第{k}页")  #减少需要人机验证的几率
    time.sleep(delay)
    get_info(k)


with open("result.txt","w",encoding='utf-8') as f:
    f.writelines(url_list)