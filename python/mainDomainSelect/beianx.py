"""
网站：https://www.beianx.cn/

"""
import requests
from lxml import etree

beian=input("请输入在倒数第一个‘-’前的网站备案号前缀：")

url=f"https://www.beianx.cn/search/{beian}"

headers={
    "Host": "www.beianx.cn",
    "Cookie": "__51vcke__JfvlrnUmvss1wiTZ=f16c0d7e-8d1c-58a2-ac92-47ef4828c386; __51vuft__JfvlrnUmvss1wiTZ=1747225008184; .AspNetCore.Antiforgery.OGq99nrNx5I=CfDJ8Hs-UzrrymBFq79b-csseefArTdXjl5hUaOdTYU5zZPZQ585HVsRFkAficudR9DRJ_NlSsjkBsBjL9bU8jUA7554cmrCNSbzoE1_yCdmEOOsci8JDmJQa-28ajvdA0wovJIs-N3O_DQhBmgyd2hXUIs; .AspNetCore.Session=CfDJ8Hs%2BUzrrymBFq79b%2Bcsseed5MQ%2FFiwoM5WrqHqUnqxTuk2nj7IyTl%2FFUoASBcNfZN2ZTLqJWXW6Re4vcGQ0186YBD2a0qKcosQyfAw7mt9yqJg6659FRf754iZroeK61fSQ4IfXS4aXlJMpR2w2EFo%2FtONR%2BFRx1ujLorjkTDoS%2B; acw_tc=0aef811617562556989097595e3def5cdfedf63016df019ed7ae20bd562ca7; __vtins__JfvlrnUmvss1wiTZ=%7B%22sid%22%3A%20%220271f2ac-0852-5592-b876-17ecc63a118c%22%2C%20%22vd%22%3A%201%2C%20%22stt%22%3A%200%2C%20%22dr%22%3A%200%2C%20%22expires%22%3A%201756257549944%2C%20%22ct%22%3A%201756255749944%7D; __51uvsct__JfvlrnUmvss1wiTZ=4; mac_string=27b0ac78af-df60-46aa-91fd-086fd3c7374c",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Referer": "https://www.beianx.cn/search/%E6%B5%99B2-20080224",
    "Priority": "u=0, i",
    "Connection": "keep-alive"
}

res=requests.get(url,headers=headers)

# 将HTML内容解析为lxml的Element对象（支持XML风格的XPath查询）
tree = etree.HTML(res.text)

# 编写XPath表达式，定位包含域名的<a>标签
# 规则：<td class="align-middle">下的<div>中的<a>标签，且href以"/seo/"开头
# XPath语法说明：
# //td[@class="align-middle"] ：匹配所有class为align-middle的td标签
# /div/a[starts-with(@href, '/seo/')] ：匹配td下div中的a标签，且href属性以/seo/开头
# 提取所有符合条件的文本（即域名）
domains = tree.xpath("//td[@class='align-middle']/div/a[starts-with(@href,'/seo/')]/text()")
#tree.xpath(xpath_expr)：执行 XPath 表达式，返回所有符合条件的文本内容，结果是一个列表。


# 去除重复域名（使用集合去重，再转回列表）
unique_domains = list(set(domains))

domain_list=[]
for domain in unique_domains:
    domain_list.append(domain+'\n')

with open('beianx.txt','w',encoding='utf-8') as f:
    f.writelines(domain_list)

