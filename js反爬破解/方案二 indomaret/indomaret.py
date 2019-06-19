# - * - coding: utf-8 - * -
from tools import get_token_from_file,get_token_from_code,headerConvert_json
import requests
import re
key_url = "http://maps.googleapis.com/maps/api/js?libraries=places&sensor=false:formatted"
str_headers = '''Host: maps.googleapis.com
Proxy-Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9'''
js_code = '''var b = 'https://maps.googleapis.com/maps/api/place/js/PlaceService.QueryPlaces?1m6&1m2&1d-3.3298246405326473&2d114.85981736547387&2m2&1d-3.2399931121206955&2d114.94979673508055&2szh-CN&4sindomaret&29e3&36m1&2e1&1032e0',
ii = /'/g;
// key= 3631862890;

function kh(b)  {
    var a = {b:2147483647 },
        c = 0;
    for (var d = Array(b.length), e = 0, f = b.length; e < f; ++e)
        d[e] = b.charCodeAt(e);
    d.unshift(c);
    a = a.b;
    c = b = 0;
    for (e = d.length; c < e; ++c)
        b *= 1729,
            b += d[c],
            b %= a;
    return "_" + b.toString(36);
};


function main(b, key){
    b = b+ "&callback=_xdc_." + kh(b);
    b = b.replace(ii,"%27") + "";
    var c =  b + "&token=",
        mh = /(?:https?:\/\/[^/]+)?(.*)/;
    b = mh.exec(b);

    return c + kh2(b && b[1], key);
};

function kh2 (b,c) {
    var a = {b:131071};
    for (var d = Array(b.length), e = 0, f = b.length; e < f; ++e)
        d[e] = b.charCodeAt(e);
    d.unshift(c);
    a = a.b;
    c = b = 0;
    for (e = d.length; c < e; ++c)
        b *= 1729,
            b += d[c],
            b %= a;
    return b
};'''
key = ''

headers = headerConvert_json(str_headers)  # 将字符headers转成dict型

sour = requests.get(key_url,headers).text  # 下载

# 正则提取key
obj_key = re.search('maps.googleapis.com/maps-api-v.*?",".*?"\],\[(.*?)\],1,null,null', sour, re.S | re.I)
if obj_key:
        key = obj_key.group(1)

# 构建传入js参数 args[0]为待加密参数，args[1]为key值
args = ["https://maps.googleapis.com/maps/api/place/js/PlaceService.QueryPlaces?1m6&1m2&1d-3.242776710820551&2d114.56083995628524&2m2&1d-3.1529451824085992&2d114.65081158427142&2sen-US&4sindomaret&29e3&36m1&2e1&1032e0",
        key]
# 编译js_code中的js代码，调用main函数，传入args参数
token_url =  get_token_from_code(js_code, "main", *args)

print token_url





