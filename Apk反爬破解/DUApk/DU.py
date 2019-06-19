# - * - coding: utf-8 - * -
# author: Evin
# E-mail: 879531595@qq.com
import requests
import hashlib
import json
from math import ceil
import xlwt

limit = 20

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

# 获取md5
def get_md5(_str):
    m1 = hashlib.md5()
    m1.update(_str)
    return m1.hexdigest()

# 获取sign
def get_sign(catId, page):

    param = {
        "catId": catId,
        "limit": limit,
        "loginToken": "ac24bd6e|28030497|dafdb1dc067ac1f9",
        "page": page,
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

    return get_md5(sign_code)

# 获取总页面
def get_ceil(nominator, denominator):
    try:
        return int(ceil(1.0*nominator/denominator))
    except Exception, e:
        return None

dataList = []

data = ['title', 'logoUrl', 'price', 'soldNum']

dataList.append(data)

def collect_products():
    catId = 2
    page_no = 0
    max_page = 100
    while page_no <= max_page:
        print("page_no: %s" % str(page_no))
        sign = get_sign(catId, page_no)
        _url = "https://du.hupu.com/search/list?size=[]&title=&typeId=0&catId={catId}&unionId=0&sortType=0&sortMode=1&page={page}&limit=20&sign={sign}".format(
            catId=catId, page=page_no, sign=sign)

        sour = requests.get(_url, headers=headers, verify=False).text
        jsoninfo = json.loads(sour)
        if "data" in jsoninfo:
            result = jsoninfo.get("data")
            if page_no == 0:
                total = result.get("total")
                max_page = get_ceil(total, limit)
                max_page = 50

            productList = result.get("productList")
            for product in productList:
                try:
                    title = product.get("title")
                    price = product.get("price")
                    logoUrl = product.get("logoUrl")
                    soldNum = product.get("soldNum")
                    data = [title, logoUrl, price, soldNum]
                    print(data)
                    dataList.append(data)
                except Exception as ex:
                    print(ex)
        page_no += 1

def save_info():
    file = xlwt.Workbook()
    table = file.add_sheet('sheet1')
    for _row , datainfo in enumerate(dataList):
        for _col , cell in enumerate(datainfo):
            table.write(_row, _col, cell)

    file.save("dome.xls")





if __name__ == '__main__':
    collect_products()

    save_info()
