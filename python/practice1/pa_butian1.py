import requests

url="https://www.butian.net/Reward/corps"
headers={
    "Host": "www.butian.net",
    "Content-Type":"multipart/form-data; boundary=----WebKitFormBoundaryJxDvuY3Nk5nM5vRX",
    "Referer":"https://www.butian.net/Reward/plan/2"
}
data="""
------WebKitFormBoundaryJxDvuY3Nk5nM5vRX
Content-Disposition: form-data; name="ajax"

1
------WebKitFormBoundaryJxDvuY3Nk5nM5vRX
Content-Disposition: form-data; name="name"


------WebKitFormBoundaryJxDvuY3Nk5nM5vRX
Content-Disposition: form-data; name="sort"

1
------WebKitFormBoundaryJxDvuY3Nk5nM5vRX--
"""

res=requests.post(url,headers=headers,data=data)
content=res.json()
print(content)
for item in content['data']['list']:
    print(item['company_name']+'赏金范围：'+str(item['min_reward'])+'-'+str(item['max_reward']))