#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
import time
import execjs
from base64 import b64decode
from base64 import b64encode
from Crypto.Cipher import AES, DES
import base64
import requests
import datetime
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")
url = "https://capi.luckincoffee.com/resource/m/shop/shopList"
payload = "q=tnZZHkZEFgZcXq2BrUQ3ACyLh4PjnoKbC_HVBSUSV8RRbj-j9p9fOi6amyqzkuOZSa4-g_1S73iAv217WlVL7Jv2IfJkWK2IJBX599DNfyoDWseYv_RYIXStJ4k82HjA_gXWT08PbAy5l-zg4SAmy8fOC_5CuGnFpx-Pgmz-082WTsnmOy4LmWTW2CDNyo9v&cid=210101&uid=b8c2aa5e-e2d4-4388-b691-ef0a04ad6dea1537945674714&sign=179820228816878384931513445643602912637&event_id=1539254525765"

headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'User-Agent': "okhttp/3.10.0"
}



# print(response.text)
# 抓包返回的和inspeckage看到的区别是减号变成加号，下划线变成斜杆


# Padding for the input string --not
# related to encryption itself.
BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


class DESCipher:
    """
    Tested under Python 3.x and PyCrypto 2.6.1.
    """

    def __init__(self, key):
        # 加密需要的key值
        self.key = key

    def encrypt(self, raw):
        raw = pad(raw)
        # 通过key值，使用ECB模式进行加密
        cipher = DES.new(self.key, DES.MODE_ECB)
        # 返回得到加密后的字符串进行解码然后进行64位的编码
        return base64.b64encode(cipher.encrypt(raw)).decode('utf8')

    def decrypt(self, enc):
        # 首先对已经加密的字符串进行解码
        enc = b64decode(enc)
        # 通过key值，使用ECB模式进行解密
        cipher = DES.new(self.key, DES.MODE_ECB)
        # print(unpad(cipher.decrypt(enc)).decode('utf8'))
        return unpad(cipher.decrypt(enc)).decode('utf8')


class AESCipher:
    """
    Tested under Python 3.x and PyCrypto 2.6.1.
    """

    def __init__(self, key):
        # 加密需要的key值
        self.key = key

    def encrypt(self, raw):
        raw = pad(raw)
        # print raw
        # 通过key值，使用ECB模式进行加密
        cipher = AES.new(self.key, AES.MODE_ECB)
        # 返回得到加密后的字符串进行解码然后进行64位的编码
        return base64.b64encode(cipher.encrypt(raw)).decode('utf8')

    def decrypt(self, enc):
        # 首先对已经加密的字符串进行解码
        enc = b64decode(enc)
        # 通过key值，使用ECB模式进行解密
        cipher = AES.new(self.key, AES.MODE_ECB)
        # print(unpad(cipher.decrypt(enc)).decode('utf8'))
        return unpad(cipher.decrypt(enc)).decode('utf8')




aescipher = AESCipher(b'dJLdCJiVnDvM9JUp')
text = '''aHEyoX9j_EG3SpWoVeXYJKYUEM_7Qw0tpHAxL2y2B0ZqTB38A4qyFO3ySgHQb1gWx9zufDBLO9YuLKqPwVSp0oiDlCVxeYkmEN97Sr6NWTNK_P2D27Ein20iSQbCI1JS_gXWT08PbAy5l-zg4SAmy8fOC_5CuGnFpx-Pgmz-082WTsnmOy4LmWTW2CDNyo9v'''
text = text.replace('-', '+').replace('_', '/')
print( aescipher.decrypt(text))

def show_byte(text, code):
    aescipher = AESCipher(code)
    text = text.replace('-', '+').replace('_', '/')
    return aescipher.decrypt(text)





def init_script(js_file):
    js_code = ''
    with open(js_file, 'r') as fp:
        for line in fp.readlines():
            js_code += line

    ctx = execjs.compile(js_code)
    return ctx


#
# text3 = '''B5kStEAb5qmF1eJB5NtgYYJiJL-vrxJ0ERH21nkk6dgBa_bAS97eQN20m7WNQ2i7lEO0hA_l9GkaA9V5gb-wu1B5WiJcp9ZY38xcPt_KzwzbV89eciLuLEECkxCyj5Ao1K1Zi0VrNZx39tHIYrqReM63suxltE2z6AydyiOaqb4'''
# print show_byte(text3, b"dJLdCJiVnDvM9JUp")
#
#
text2 = 'OGoneCaXN3O6R3_Y5gHZNSfhPJX3odI9M-5HePeSRRI='
#
text = '{"latitude":35.874499,"cityName":"杭州","appversion":"1950","longitude":120.043897,"channel":"GCJ-02","offset":0,"pageSize":15}'
# q = aescipher.encrypt(text).replace('+', '-').replace('/', '_')
# print(q)
#
print (show_byte(text2, b"dJLdCJiVnDvM9JUp"))

def get_sign(ctx, q):
    cid = "210101"
    sign_key = "dJLdCJiVnDvM9JUpsom9"
    uid = "dba652f3-339f-4b10-bf37-d98d803bb9611540007126971"
    # event_id = str(int(time.time() * 1000))
    event_id = "1540017114844"
    code = "cid={cid};event_id={event_id};q={q};uid={uid}{sign_key}".format(
        cid=cid, event_id=event_id, q=q, uid=uid, sign_key=sign_key)
    # return code

    sign_info = ctx.call("main", code)
    return sign_info



q = 'aHEyoX9j_EG3SpWoVeXYJLQY5GKk2zgwh3FgWTodyBWKJ48b-w27F3Hk4ZjXwq0tx9zufDBLO9YuLKqPwVSp0oiDlCVxeYkmEN97Sr6NWTNgbfi06140D6OWc1F1APtO_gXWT08PbAy5l-zg4SAmy8fOC_5CuGnFpx-Pgmz-082WTsnmOy4LmWTW2CDNyo9v'
ctx = init_script("luckin_sign.js")
print(get_sign(ctx, q))


