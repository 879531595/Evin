#- * - coding:utf-8 - * -
import execjs
import urllib
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
node = execjs



def GetParams(PostData):
    e = u"010001"
    f = u'00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    g = u'0CoJUm6Qyw8W8jud'
    d = PostData
    def get_js():
        codejs = ''
        try:
            f = open("core.js", 'r')
            line = f.readline()
            while line:
                codejs = codejs + line.decode('utf-8')
                line = f.readline()
        except Exception as ex:
            print ex.message
            return None
        return codejs
    codejs = get_js()
    ctx = execjs.compile(codejs)
    info = ctx.call("d", d, e, f, g )
    params = u"params=%s&encSecKey=%s" % (urllib.quote(info["encText"]), urllib.quote(info["encSecKey"]))
    return params.replace("/", "%2F")