import requests

main_domain=input("请输入要查询的主域名：")

url=f"https://crt.sh/?q={main_domain}&output=json"
headers={"Host":"crt.sh"}

res=requests.get(url,headers=headers)

url_list=[]
content=res.json()
for item in content:
    url_list.append(item["common_name"].replace('*.','')+'\n')

filename=main_domain.replace('.','_')+'.txt'
with open(filename,'w',encoding='utf-8') as f:
    f.writelines(url_list)