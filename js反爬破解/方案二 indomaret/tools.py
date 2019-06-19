# - * - coding:utf-8 - * -

import execjs

def get_token_from_file(filepath, fun, *args):
    def get_js():
        codejs = ''
        try:
            f = open(filepath, 'r')
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
    info = ctx.call(fun, *args)
    return info

def get_token_from_code(code_info,fun, *args):
    ctx = execjs.compile(code_info)
    info = ctx.call(fun, *args)
    return info

# 转headers代码
def headerConvert_json(str_headers):
    json_headers = {}
    infolist = str(str_headers).split('\n')
    for line in infolist:
        info = line.split(':')
        if info.__len__() == 2:
            json_headers[str(info[0].strip())] = info[1].strip()

    return json_headers