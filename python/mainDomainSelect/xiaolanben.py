"""
爬取：https://sou.xiaolanben.com/
使用方式：需要抓取数据包来填入信息进行爬取
(数据包：GET /api.xiaolanben.com/xlb-gateway/blue-book/company/companyData?....)
"""
import requests

url=input("请从数据包中copy the url:")
Cookie=input("请从数据包中手动复制cookie:")

headers={
    "Host":"sou.xiaolanben.com",
    "Cookie":Cookie,
    "Authorization": "encrypt MjYwOTM2NTc0LXYx.A9BKEOr1GFkGxbDrYTezK5QI9EcUgB4-WlAUH5NjJmpxYJLiqx-aufGvF9Y-eipfrfv1stQ0MKoyVaB6z3WS9Q",
    "Userid":"260936574"
}

res=requests.get(url,headers=headers)
content=res.json()
print(content)  #查看返回数据

url_list=[]

for item in content:
    url_list.append(item['domain']+'\n')

with open('xiaolanben.txt','w',encoding='utf-8') as f:
    f.writelines(url_list)

