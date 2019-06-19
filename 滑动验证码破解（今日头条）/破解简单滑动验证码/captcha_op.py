import requests
from RegisterImgUtil import get_move_step
import random
import time
import json

def _t():
    return str(int(time.time()) * 1000)
print(_t())



CAPTCHA_BG = "captcha_bg.png"
CAPTVHA_ICON = "captcha_icon.png"
captcha_init_url = "https://verify.snssdk.com/get?external=&fp={fp}&aid=24&lang=zh&app_name=web_search&iid=&vc=1.0&did=&uid=0&ch=pc_slide&os=2&challenge_code=1366&time={_t}"
captcha_send_url = "https://verify.snssdk.com/verify?external=&fp={fp}&aid=24&lang=zh&app_name=web_search&iid=&vc=1.0&did=&uid=0&ch=pc_slide&os=2&challenge_code=1366"

verify_headers = {

    "Host": "verify.snssdk.com",
    "Connection": "keep-alive",
    "Accept": "application/json",
    "Origin": "https://www.toutiao.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Referer": "https://www.toutiao.com/search/?keyword=%E8%85%BE%E8%AE%AF%E6%8E%A7%E8%82%A1",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
}

# 下载图片
def download_img(url, path):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
    }

    response = requests.get(url, headers=headers, timeout=10, verify=False)
    with open(path, "wb") as f:
        f.write(response.content)


def captcha_init_step1(fp):
    url = captcha_init_url.format(fp=fp, _t=_t())
    response = requests.get(url, headers=verify_headers, timeout=10, verify=False)
    _json = response.json()
    data = _json.get("data")
    _id = data.get("id")
    question = data.get("question")
    CAPTCHA_BG_url = question.get("url1")
    download_img(CAPTCHA_BG_url, CAPTCHA_BG) # download bg
    CAPTVHA_ICON_url = question.get("url2")
    download_img(CAPTVHA_ICON_url, CAPTVHA_ICON) # download icon
    tip_y = question.get("tip_y")
    return _id, tip_y




def gene_parma(_id, tip_x, tip_y):
    reply_cell_base = {"relative_time": 16, "x": 0, "y": 55}
    parma = {"modified_img_width": 268, "id": _id, "mode": "slide",
     "reply": [{"relative_time": 16, "x": 0, "y": 55}, {"relative_time": 55, "x": 5, "y": 55},
               {"relative_time": 76, "x": 14, "y": 55}, {"relative_time": 96, "x": 33, "y": 55},
               {"relative_time": 115, "x": 45, "y": 55}, {"relative_time": 136, "x": 69, "y": 55},
               {"relative_time": 156, "x": 84, "y": 55}, {"relative_time": 176, "x": 102, "y": 55},
               {"relative_time": 195, "x": 114, "y": 55}, {"relative_time": 216, "x": 130, "y": 55},
               {"relative_time": 235, "x": 137, "y": 55}, {"relative_time": 255, "x": 144, "y": 55},
               {"relative_time": 276, "x": 149, "y": 55}, {"relative_time": 295, "x": 155, "y": 55},
               {"relative_time": 315, "x": 161, "y": 55}, {"relative_time": 335, "x": 169, "y": 55},
               {"relative_time": 355, "x": 173, "y": 55}, {"relative_time": 376, "x": 181, "y": 55},
               {"relative_time": 396, "x": 184, "y": 55}, {"relative_time": 415, "x": 187, "y": 55},
               {"relative_time": 436, "x": 191, "y": 55}, {"relative_time": 456, "x": 194, "y": 55},
               {"relative_time": 476, "x": 196, "y": 55}, {"relative_time": 496, "x": 197, "y": 55},
               {"relative_time": 515, "x": 199, "y": 55}, {"relative_time": 535, "x": 201, "y": 55},
               {"relative_time": 555, "x": 203, "y": 55}, {"relative_time": 575, "x": 207, "y": 55},
               {"relative_time": 615, "x": 210, "y": 55}, {"relative_time": 634, "x": 211, "y": 55},
               {"relative_time": 676, "x": 212, "y": 55}]}
    x = 0
    relative_time = 16
    reply = []
    while True:
        reply_cell = reply_cell_base.copy()
        if  x > tip_x:
            reply_cell["relative_time"] = relative_time
            reply_cell["x"] = tip_x
            reply_cell["y"] = tip_y
            reply.append(reply_cell)
            break
        else:
            reply_cell["relative_time"] = relative_time
            reply_cell["x"] = x
            reply_cell["y"] = tip_y
            reply.append(reply_cell)
            x += random.randint(2, 8)
            relative_time += random.randint(10, 56)

    parma["reply"] = reply

    return parma


def verify(_id, tip_y, fp):
    url = captcha_send_url.format(fp=fp)
    tip_x = get_move_step(CAPTVHA_ICON, CAPTCHA_BG)
    parma = gene_parma(_id, tip_x, tip_y)
    parma = str(parma).replace("\'", "\"")

    response = requests.post(url, headers=verify_headers, data=str(parma), timeout=10, verify=False)
    print(response.text)

def run(fp):
    _id, tip_y = captcha_init_step1(fp)
    time.sleep(1)
    verify(_id, tip_y, fp)

    pass





if __name__ == '__main__':
    fp = "346346242ce9f8c2afa94c5e58ef02b4"
    run(fp)


