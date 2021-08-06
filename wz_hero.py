# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 21:16
# @Author  : B612
# @File    : 爬取王者荣耀的皮肤.py

# http%3A%2F%2Fshp%2Eqpic%2Ecn%2Fishow%2F2735042818%2F1619604257%5F84828260%5F19751%5FsProdImgNo%5F2%2Ejpg%2F200
import urllib.parse
import urllib.request
hero_url = "http%3A%2F%2Fshp%2Eqpic%2Ecn%2Fishow%2F2735042818%2F1619604257%5F84828260%5F19751%5FsProdImgNo%5F2%2Ejpg%2F"
img_url = urllib.parse.unquote(hero_url)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.49"

}
req = urllib.request.Request(img_url, headers=headers)
# response = urllib.request.urlopen(req).read().decode()  # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte   # 'utf-8'编解码器无法解码位置0的0xff字节:无效的起始字节
response = urllib.request.urlopen(req).read()
# print(response)
with open("王者皮肤.png", "wb") as fl:
    fl.write(response)