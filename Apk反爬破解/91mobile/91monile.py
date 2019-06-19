import subprocess
import requests

"""
程序逻辑： 
    1. signKey.exe 执行时会打印加密 cookie
    2. subprocess执行 signKey.exe 返回 cookie
    3. signKey.java 代码并不参与程序运行，代码用于生成exe文件
"""





# 调用signKey.exe 生成cookies
def get_cookies():
    command_str = "signKey.exe"
    p1 = subprocess.Popen(["cmd", "/C",command_str],stdout=subprocess.PIPE)
    cookie = p1.communicate()[0]
    cookie = str(cookie.decode("utf-8")).strip()
    return cookie



# 测试请求
def Test_request():
    url = "https://api.91mobiles.com/nm/api/app/page/home?z=1&version=1.2&other_sections=true&"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Language": "en-US",
        "device_id": "22c4526c4bd629b2",
        "app_version_code": "330",
        "api_version_code": "1.2",
        "customerIdByDeviceId": "6121822",
        "userId": "6121822",
        "source": "APP",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus 5 Build/MMB29K)",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "Host": "api.91mobiles.com",
        "cookie": get_cookies()
    }



    response = requests.get(url, headers=headers, timeout=30, verify=False)
    if response.status_code == 200:
        print(response.text)



if __name__ == '__main__':
    for i in range(10):
        Test_request()