"""
网站：https://crt.sh/
使用方式；
- 直接输入主域名即可，输出的文件名为 主域名_CRT.txt
"""
import requests

main_domain=input("请输入要查询的主域名：")

url=f"https://crt.sh/?q={main_domain}&output=json"
headers={"Host":"crt.sh"}

res=requests.get(url,headers=headers)

url_list=[]
content=res.json()
for item in content:
    url_list.append(item["common_name"].replace('*.','')+'\n')

filename=main_domain.replace('.','_')+'_CRT.txt'
with open(filename,'w',encoding='utf-8') as f:
    f.writelines(url_list)