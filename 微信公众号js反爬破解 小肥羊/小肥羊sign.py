import hashlib
import time
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

"""
加密算法：sha256
加密参数：post请求中的全部参数，fiddler拦截内容中除sign以为的全部参数
加密方式：将dict按key=vlaue&key=vlaue&...的规律转换成str后在加上appSercet_key值，然后使用sha256算法加密
注意：req_time参数为发送请求时的参数
"""

appSercet_key = "d03adb2664fda5cef30117a6a51a2b7a"

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044705 Mobile Safari/537.36 MMWEBID/844 MicroMessenger/7.0.3.1400(0x27000389) Process/tools NetType/WIFI Language/zh_CN",
    "Content-Type": "application/json"
}


# sha256算法
def get_hash(data: bytes):
    m = hashlib.sha256()
    m.update(data)
    return m.hexdigest()

#生成sign函数
#传入规则：post请求中的全部参数
def getSignurature(parma_dict):
    # 参数类型是字典型（dict）
    parma_str = ""

    parma_dict_key_list = sorted(parma_dict.keys())

    for _key in parma_dict_key_list:
        if "sign" == _key:
            continue
        _v = str(parma_dict.get(_key)).strip()
        _k = _key.lower()
        cell = _k + '=' + _v + '&'
        parma_str += cell

    parma_str =  parma_str[:-1] + appSercet_key

    return get_hash(parma_str.encode("utf-8"))

# 测试获取城市列表
def test_getCityList():
    url = "https://littlesheep.e.verystar.net/Nearbystore/City/getCityList"
    parma_dict = {"ticket":"c24016c692fa11e9b9ca00163e0034e8","openid":"oNa69js4ef4uR5KK9mKxccHyEZOU","app_key":"aa590adbe613a1f675aa1f6551e50cdb","req_time":1560999666}
    parma_dict["req_time"] = int(time.time())
    parma_dict["sign"] = getSignurature(parma_dict)
    response = requests.post(url, headers=headers,json=parma_dict, timeout=30, verify=False)
    if response.status_code == 200:
        print(response.text)

# 测试获取店列表
def test_getStoreList():
    url = "https://littlesheep.e.verystar.net/Nearbystore/Store/getStoreList"
    parma_dict = {"ticket":"c24016c692fa11e9b9ca00163e0034e8","openid":"oNa69js4ef4uR5KK9mKxccHyEZOU","city_id":"42","lng":"113.94206","lat":"22.52749","app_key":"aa590adbe613a1f675aa1f6551e50cdb","req_time":1560999675,"sign":"ca2bb90973a6371c76d437e2e67e97ff3d5b2f9fced931fd9259132ba9e4f764"}
    parma_dict["req_time"] = int(time.time())
    parma_dict["sign"] = getSignurature(parma_dict)
    response = requests.post(url, headers=headers, json=parma_dict, timeout=30, verify=False)
    if response.status_code == 200:
        print(response.text)

if __name__ == '__main__':
    test_getCityList()
    test_getStoreList()
