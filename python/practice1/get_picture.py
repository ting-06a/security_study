import requests

url="https://pic1.afdiancdn.com/user/6cec6a62d69311ebbc3552540025c377/common/e8ebd7120e25a07fabd9850599f4f4c8_w1152_h490_s44.jpeg?imageView2/1/w/3000/h/800"

res=requests.get(url)

with open('afd_w2z.png','wb') as f:
    f.write(res.content)