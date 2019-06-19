# - * - coding: utf-8 - * -
import requests
import json
from GetParams import GetParams
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


obj_url = "https://music.163.com/#/mv?id=10780167"

str_headers = '''Host: music.163.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Content-Length: 480'''

def ConvertToheaders(str_headers):
    headers = {}
    infoList = str_headers.split("\n")
    for line in infoList:
        data = line.split(": ")
        if data.__len__() != 2:
            continue
        headers[data[0]] = data[1]
    return headers
headers = ConvertToheaders(str_headers)


params = '{"rid":"R_SO_4_1333377232","offset":"80","total":"false","limit":"20","csrf_token":""}'
post_data = GetParams(params)

url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_1333377232?csrf_token="
html = requests.post(url, headers=headers, data=post_data, verify=False).text
print json.loads(html)
