# - * - coding: utf-8 - * -
import requests
import json
import hashlib

headers = {
    "duuuid": "11b7eb652ea3df84",
    "duplatform": "android",
    "duchannel": "myapp",
    "duv": "3.4.800",
    "duloginToken": "ac24bd6e|28030497|dafdb1dc067ac1f9" ,
    "dudeviceTrait": "Nexus 5",
    "User-Agent": "duapp/3.4.800(android;6.0.1)" ,
    "Host": "du.hupu.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}
n = "3542e676b4c80983f6131cdfe577ac9b"
param = {
    "catId": "0",
    "limit": "20",
    "loginToken": "ac24bd6e|28030497|dafdb1dc067ac1f9",
    "page": 0,
    "platform": "android",
    "size": "[]",
    "sortMode": "1",
    "sortType": "0",
    "title": "",
    "typeId": "0",
    "unionId": "0",
    "uuid": "11b7eb652ea3df84",
    "v": "3.4.800",
    "n": "3542e676b4c80983f6131cdfe577ac9b"
}


sign_code = "catId{catId}limit{limit}loginToken{loginToken}page{page}platform{platform}size{size}sortMode{sortMode}" \
            "sortType{sortType}title{title}typeId{typeId}unionId{unionId}uuid{uuid}v{v}{n}".format(**param)

print sign_code

def get_md5(_str):
    m1 = hashlib.md5()
    m1.update(_str)
    return m1.hexdigest()

print get_md5(sign_code)






url = "https://du.hupu.com/search/list?size=[]&title=&typeId=0&catId=0&unionId=0&sortType=0&sortMode=1&page=0&limit=20&sign=0c5ded7ebc07d74198422c1acaced4db"

response = requests.get(url, headers=headers)
sour = response.text
jsoninfo = json.loads(sour)

print(jsoninfo)